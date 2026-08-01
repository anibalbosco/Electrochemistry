#!/usr/bin/env python3
"""Build detailed instructor/TA PDF packets for each workshop session.

Produces two PDFs per session under pdfs/:
  - session-NN-<slug>-experiment.pdf  (prep + materials + experiment + safety)
  - session-NN-<slug>-lecture-notes.pdf  (overview + lecture + instructor notes)

Requires Google Chrome or Microsoft Edge (headless print-to-PDF).
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension

# Reuse figure inlining helpers from the HTML site builder.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import (  # noqa: E402
    ROOT,
    SESSIONS,
    inline_svg_figures,
    unwrap_block_figures,
)

PDF_DIR = ROOT / "pdfs"
BUILD_DIR = PDF_DIR / "_build"
CSS_PATH = ROOT / "assets" / "pdf.css"

MD = markdown.Markdown(
    extensions=[TableExtension(), FencedCodeExtension()],
    output_format="html5",
)

DOC_SPECS = {
    "experiment": {
        "label": "Experiment Packet",
        "filename_suffix": "experiment",
        "subtitle": "Bench instructions for instructors and TAs",
        "sections": [
            ("Session overview & plan", "README.md"),
            ("Preparation", "preparation.md"),
            ("Materials checklist", "materials.md"),
            ("Experiment procedure", "experiment.md"),
            ("Shared safety notes", None),  # shared/safety-notes.md
        ],
    },
    "lecture": {
        "label": "Lecture & Instructor Notes",
        "filename_suffix": "lecture-notes",
        "subtitle": "Teaching script, deep-dive notes, and coaching guidance",
        "sections": [
            ("Session overview & plan", "README.md"),
            ("Lecture talking points", "lecture.md"),
            ("Instructor deep-dive notes", "instructor.md"),
            ("Preparation reminders", "preparation.md"),
        ],
    },
}


def find_browser() -> Path:
    candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
        Path.home() / r"AppData\Local\Google\Chrome\Application\chrome.exe",
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path("/usr/bin/google-chrome"),
        Path("/usr/bin/chromium"),
        Path("/usr/bin/chromium-browser"),
        Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
        Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
    ]
    for path in candidates:
        if path.is_file():
            return path
    which = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("msedge")
    if which:
        return Path(which)
    raise FileNotFoundError(
        "Chrome or Edge not found. Install a Chromium-based browser to generate PDFs."
    )


def md_to_html(text: str, keep_h1: bool = False) -> str:
    MD.reset()
    html = MD.convert(text)
    if not keep_h1:
        html = re.sub(r"^\s*<h1[^>]*>.*?</h1>\s*", "", html, count=1, flags=re.DOTALL)
    # Neutralize internal .md links in print (keep text, drop broken file links).
    html = re.sub(
        r'<a href="([^"]+\.md)(#[^"]*)?">([^<]*)</a>',
        r"\3",
        html,
    )
    return html


def read_md(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def section_html(
    label: str,
    md_path: Path,
    html_anchor: Path,
) -> str:
    text = read_md(md_path)
    title = extract_title(text, label)
    body = unwrap_block_figures(inline_svg_figures(md_to_html(text), html_anchor))
    return f"""
<section class="section">
  <div class="section-label">{label}</div>
  <h1>{title}</h1>
  {body}
</section>
"""


def cover_html(
    session: dict,
    doc_key: str,
    section_titles: list[str],
) -> str:
    spec = DOC_SPECS[doc_key]
    contents = "\n".join(f"<li>{t}</li>" for t in section_titles)
    return f"""
<section class="cover">
  <p class="kicker">SigmaCamp · Electrochemistry Lab · Session {session["num"]}</p>
  <h1>{session["title"]}</h1>
  <p class="doc-type">{spec["label"]}</p>
  <div class="meta">
    <p><strong>Audience:</strong> instructors and teaching assistants</p>
    <p><strong>Purpose:</strong> {spec["subtitle"]}</p>
    <p><strong>Session hook:</strong> {session["hook"]}</p>
    <p><strong>Length:</strong> 90-minute lab block (~20 min concepts + ~70 min hands-on)</p>
  </div>
  <div class="contents">
    <h2>This packet includes</h2>
    <ol>{contents}</ol>
  </div>
  <p class="footer-note">
    Generated from the Electrochemistry workshop curriculum. Prefer the latest PDF from the
    course repository if procedures change mid-week.
  </p>
</section>
"""


def wrap_document(title: str, body: str, css_text: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>{css_text}</style>
</head>
<body>
{body}
</body>
</html>
"""


def html_to_pdf(browser: Path, html_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    # Write to a temp file first so a failed run does not leave a truncated PDF.
    with tempfile.TemporaryDirectory(prefix="echem-pdf-") as tmp:
        tmp_pdf = Path(tmp) / pdf_path.name
        cmd = [
            str(browser),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--disable-extensions",
            "--allow-file-access-from-files",
            f"--print-to-pdf={tmp_pdf}",
            html_path.resolve().as_uri(),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0 or not tmp_pdf.is_file() or tmp_pdf.stat().st_size < 1000:
            raise RuntimeError(
                "PDF generation failed for "
                f"{html_path.name}\nstdout: {result.stdout}\nstderr: {result.stderr}"
            )
        shutil.copyfile(tmp_pdf, pdf_path)


def build_packet(session: dict, doc_key: str, css_text: str, browser: Path) -> Path:
    spec = DOC_SPECS[doc_key]
    session_dir = ROOT / "sessions" / session["slug"]
    html_anchor = session_dir / "index.html"

    parts: list[str] = []
    section_titles: list[str] = []

    for label, md_name in spec["sections"]:
        if md_name is None:
            md_path = ROOT / "shared" / "safety-notes.md"
        else:
            md_path = session_dir / md_name
        if not md_path.is_file():
            print(f"  WARNING: missing {md_path.relative_to(ROOT)}")
            continue
        section_titles.append(label)
        parts.append(section_html(label, md_path, html_anchor))

    cover = cover_html(session, doc_key, section_titles)
    title = f"Session {session['num']} — {session['title']} — {spec['label']}"
    html = wrap_document(title, cover + "\n".join(parts), css_text)

    stem = f"session-{session['slug']}-{spec['filename_suffix']}"
    html_path = BUILD_DIR / f"{stem}.html"
    pdf_path = PDF_DIR / f"{stem}.pdf"
    html_path.write_text(html, encoding="utf-8")
    html_to_pdf(browser, html_path, pdf_path)
    print(f"  {pdf_path.relative_to(ROOT)} ({pdf_path.stat().st_size // 1024} KB)")
    return pdf_path


def write_index(pdf_paths: list[Path]) -> None:
    lines = [
        "# Instructor / TA PDF packets",
        "",
        "Detailed printable packets for teaching each day of the workshop.",
        "",
        "Regenerate after editing markdown:",
        "",
        "```bash",
        "python scripts/build_pdfs.py",
        "```",
        "",
        "| Session | Experiment packet | Lecture & instructor notes |",
        "|---------|-------------------|----------------------------|",
    ]
    by_session: dict[str, dict[str, Path]] = {}
    for path in pdf_paths:
        name = path.name
        m = re.match(r"session-(.+)-(experiment|lecture-notes)\.pdf$", name)
        if not m:
            continue
        slug = m.group(1)
        kind = m.group(2)
        by_session.setdefault(slug, {})[kind] = path

    for session in SESSIONS:
        files = by_session.get(session["slug"], {})
        exp = files.get("experiment")
        lec = files.get("lecture-notes")
        exp_link = f"[Download]({exp.name})" if exp else "—"
        lec_link = f"[Download]({lec.name})" if lec else "—"
        lines.append(
            f"| {session['num']}. {session['title']} | {exp_link} | {lec_link} |"
        )

    lines.extend(
        [
            "",
            "## Packet contents",
            "",
            "**Experiment packet:** session overview, preparation, materials checklist, "
            "full experiment procedure, and shared safety notes.",
            "",
            "**Lecture & instructor notes:** session overview, lecture talking points, "
            "instructor deep-dive notes, and preparation reminders.",
            "",
        ]
    )
    (PDF_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  {PDF_DIR.relative_to(ROOT)}/README.md")

    # Simple HTML index for local browsing / site links.
    rows = []
    for session in SESSIONS:
        files = by_session.get(session["slug"], {})
        exp = files.get("experiment")
        lec = files.get("lecture-notes")
        exp_cell = f'<a href="{exp.name}">{exp.name}</a>' if exp else "—"
        lec_cell = f'<a href="{lec.name}">{lec.name}</a>' if lec else "—"
        rows.append(
            f"<tr><td>Session {session['num']}: {session['title']}</td>"
            f"<td>{exp_cell}</td><td>{lec_cell}</td></tr>"
        )
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Instructor / TA PDFs | Electrochemistry Workshop</title>
  <link rel="stylesheet" href="../assets/site.css">
</head>
<body>
  <main class="content" style="margin-left:0;max-width:900px">
    <p class="breadcrumb"><a href="../index.html">Home</a> / PDFs</p>
    <header class="page-header">
      <h1>Instructor / TA PDF packets</h1>
      <div class="page-meta"><span class="badge">Printable</span></div>
    </header>
    <article class="main-article">
      <p>Detailed printable packets for teaching each day of the workshop.</p>
      <table>
        <thead><tr><th>Session</th><th>Experiment packet</th><th>Lecture &amp; instructor notes</th></tr></thead>
        <tbody>
{"".join(rows)}
        </tbody>
      </table>
      <p>Regenerate with <code>python scripts/build_pdfs.py</code> after editing markdown.</p>
    </article>
  </main>
</body>
</html>
"""
    (PDF_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"  {PDF_DIR.relative_to(ROOT)}/index.html")


def main() -> None:
    browser = find_browser()
    print(f"Using browser: {browser}")
    css_text = CSS_PATH.read_text(encoding="utf-8")

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    # Remove prior PDFs so renamed files do not linger.
    for old in PDF_DIR.glob("session-*.pdf"):
        old.unlink()

    pdf_paths: list[Path] = []
    for session in SESSIONS:
        print(f"Session {session['num']}: {session['title']}")
        for doc_key in ("experiment", "lecture"):
            pdf_paths.append(build_packet(session, doc_key, css_text, browser))

    write_index(pdf_paths)
    print("Done.")


if __name__ == "__main__":
    main()
