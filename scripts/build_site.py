#!/usr/bin/env python3
"""Build HTML pages from Markdown for the Electrochemistry workshop site."""

from __future__ import annotations

import re
from pathlib import Path

import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension

ROOT = Path(__file__).resolve().parent.parent

SESSIONS = [
    {
        "num": 1,
        "slug": "01-fruit-battery",
        "title": "Fruit Battery",
        "hook": "Familiar objects make electricity",
    },
    {
        "num": 2,
        "slug": "02-copper-electroplating",
        "title": "Copper Electroplating",
        "hook": "Students visibly transform a metal object",
    },
    {
        "num": 3,
        "slug": "03-silver-plating-faraday",
        "title": "Silver Plating + Faraday's Law",
        "hook": "Estimate how many atoms were deposited",
    },
    {
        "num": 4,
        "slug": "04-water-electrolysis",
        "title": "Water Electrolysis",
        "hook": "Split water and see a 2:1 ratio",
    },
    {
        "num": 5,
        "slug": "05-galvanic-corrosion-fuel-cell",
        "title": "Galvanic Corrosion + Fuel Cell",
        "hook": "Corrosion, batteries, and hydrogen storage",
    },
]

SESSION_PAGES = [
    ("index", "Overview", "README.md"),
    ("lecture", "Lecture", "lecture.md"),
    ("experiment", "Experiment", "experiment.md"),
    ("materials", "Materials", "materials.md"),
    ("preparation", "Preparation", "preparation.md"),
]

SHARED_PAGES = [
    ("overall-materials-list", "Materials List", "overall-materials-list.md"),
    ("safety-notes", "Safety Notes", "safety-notes.md"),
]

MD = markdown.Markdown(
    extensions=[TableExtension(), FencedCodeExtension()],
    output_format="html5",
)

IMG_TAG_RE = re.compile(r"<img\s+[^>]*?>", re.IGNORECASE)
SRC_RE = re.compile(r'\ssrc="([^"]+)"', re.IGNORECASE)
ALT_RE = re.compile(r'\salt="([^"]*)"', re.IGNORECASE)


def uniquify_svg_ids(svg: str, prefix: str) -> str:
    """Avoid duplicate id clashes when several diagrams share one HTML page."""
    ids = re.findall(r'\bid="([^"]+)"', svg)
    for id_ in ids:
        new_id = f"{prefix}_{id_}"
        svg = svg.replace(f'id="{id_}"', f'id="{new_id}"')
        svg = svg.replace(f"url(#{id_})", f"url(#{new_id})")
    return svg


def inline_svg_figures(html_body: str, html_path: Path) -> str:
    """Replace external SVG img tags with inlined SVG (works on file:// pages)."""
    counter = 0

    def replace_img(tag: str) -> str:
        nonlocal counter
        src_match = SRC_RE.search(tag)
        if not src_match or not src_match.group(1).lower().endswith(".svg"):
            return tag

        src = src_match.group(1)
        alt_match = ALT_RE.search(tag)
        alt = alt_match.group(1) if alt_match else "Diagram"

        svg_path = (html_path.parent / src).resolve()
        if not svg_path.is_file():
            figures_root = ROOT / "assets" / "figures"
            candidate = figures_root / Path(src).name
            if candidate.is_file():
                svg_path = candidate
            else:
                print(f"  WARNING: missing figure {src} referenced from {html_path.relative_to(ROOT)}")
                return tag

        svg = svg_path.read_text(encoding="utf-8")
        svg = re.sub(r"<\?xml[^?]*\?\>", "", svg).strip()
        counter += 1
        svg = uniquify_svg_ids(svg, f"fig{counter}")
        if 'class="diagram"' not in svg:
            svg = svg.replace("<svg ", '<svg class="diagram" ', 1)

        return f'<figure class="figure-wrap" aria-label="{alt}">{svg}</figure>'

    return IMG_TAG_RE.sub(lambda m: replace_img(m.group(0)), html_body)


def unwrap_block_figures(html_body: str) -> str:
    """Markdown wraps images in <p>; block figures must not sit inside paragraphs."""
    html_body = re.sub(r"<p>\s*(<figure[^>]*>)", r"\1", html_body)
    html_body = re.sub(r"(</figure>)\s*</p>", r"\1", html_body)
    return html_body


def rel_prefix(html_path: Path) -> str:
    depth = len(html_path.parent.relative_to(ROOT).parts)
    return "../" * depth if depth else ""


def md_to_html_body(text: str, strip_leading_h1: bool = True) -> str:
    MD.reset()
    html = MD.convert(text)
    if strip_leading_h1:
        html = re.sub(r"^\s*<h1[^>]*>.*?</h1>\s*", "", html, count=1, flags=re.DOTALL)
    html = re.sub(
        r'href="([^"]+\.md)(#[^"]*)?"',
        lambda m: f'href="{m.group(1).replace(".md", ".html")}{m.group(2) or ""}"',
        html,
    )
    html = re.sub(
        r'href="(sessions/[^"/]+)(/?)"',
        r'href="\1/index.html"',
        html,
    )
    html = re.sub(
        r'href="README\.html"',
        "href=\"index.html\"",
        html,
    )
    return html


def page_id(html_path: Path) -> str:
    rel = html_path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "home"
    if rel.startswith("shared/"):
        return rel.replace(".html", "").replace("/", "-")
    match = re.match(r"sessions/([^/]+)/(.+)\.html", rel)
    if match:
        slug, page = match.groups()
        if page == "index":
            return f"session-{slug}"
        return f"session-{slug}-{page}"
    return rel


def nav_html(current_id: str, prefix: str) -> str:
    lines = [
        '<div class="sidebar-header">',
        f'  <a href="{prefix}index.html">Electrochemistry Lab<span class="subtitle">One-week workshop · ages 15–16</span></a>',
        "</div>",
        "<nav>",
        f'  <div class="nav-section"><a class="nav-link{" active" if current_id == "home" else ""}" href="{prefix}index.html">Home</a></div>',
        '<div class="nav-section">',
        '  <div class="nav-section-title">Shared</div>',
    ]
    for slug, label, _ in SHARED_PAGES:
        pid = f"shared-{slug}"
        lines.append(
            f'  <a class="nav-link sub{" active" if current_id == pid else ""}" href="{prefix}shared/{slug}.html">{label}</a>'
        )
    lines.append("</div>")

    for session in SESSIONS:
        slug = session["slug"]
        sid = f"session-{slug}"
        active_session = current_id == sid or current_id.startswith(f"session-{slug}-")
        lines.append('<div class="nav-section">')
        lines.append(
            f'  <a class="nav-link session-title{" active" if active_session and current_id == sid else ""}" '
            f'href="{prefix}sessions/{slug}/index.html">Session {session["num"]}: {session["title"]}</a>'
        )
        for page_slug, label, _ in SESSION_PAGES:
            pid = f"session-{slug}" if page_slug == "index" else f"session-{slug}-{page_slug}"
            href = f"{prefix}sessions/{slug}/index.html" if page_slug == "index" else f"{prefix}sessions/{slug}/{page_slug}.html"
            lines.append(
                f'  <a class="nav-link sub{" active" if current_id == pid else ""}" href="{href}">{label}</a>'
            )
        lines.append("</div>")

    lines.extend(["</nav>", '<div class="sidebar-footer">', "  Markdown sources kept alongside HTML.", "</div>"])
    return "\n".join(lines)


def breadcrumb(html_path: Path, title: str, prefix: str) -> str:
    parts = ['<div class="breadcrumb">', f'<a href="{prefix}index.html">Home</a>']
    rel = html_path.relative_to(ROOT)
    if rel.parts[0] == "shared":
        parts.append(' / <a href="' + prefix + 'shared/' + rel.stem + '.html">Shared</a>')
    elif rel.parts[0] == "sessions" and len(rel.parts) >= 2:
        slug = rel.parts[1]
        session = next(s for s in SESSIONS if s["slug"] == slug)
        parts.append(
            f' / <a href="{prefix}sessions/{slug}/index.html">Session {session["num"]}</a>'
        )
    if rel.name not in ("index.html",) or rel.parts[0] == "shared":
        if rel.name != "index.html" or rel.parts[0] == "shared":
            page_name = title.split("—")[-1].strip() if "—" in title else title
            if rel.name != "index.html":
                parts.append(f" / {page_name}")
    parts.append("</div>")
    return "".join(parts)


def wrap_page(html_path: Path, title: str, body: str, badge: str | None = None) -> str:
    prefix = rel_prefix(html_path)
    current_id = page_id(html_path)
    badge_html = f'<span class="badge">{badge}</span>' if badge else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Electrochemistry Workshop</title>
  <link rel="stylesheet" href="{prefix}assets/site.css">
</head>
<body>
  <button class="menu-toggle" type="button" aria-label="Open menu" onclick="document.querySelector('.sidebar').classList.toggle('open')">☰</button>
  <div class="layout">
    <aside class="sidebar">
{nav_html(current_id, prefix)}
    </aside>
    <main class="content">
{breadcrumb(html_path, title, prefix)}
      <header class="page-header">
        <h1>{title}</h1>
        <div class="page-meta">{badge_html}</div>
      </header>
      <article class="main-article">
{body}
      </article>
    </main>
  </div>
</body>
</html>
"""


def extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def build_md_page(md_path: Path, html_path: Path, badge: str | None = None) -> None:
    text = md_path.read_text(encoding="utf-8")
    title = extract_title(text, html_path.stem.replace("-", " ").title())
    body = unwrap_block_figures(inline_svg_figures(md_to_html_body(text), html_path))
    html_path.write_text(wrap_page(html_path, title, body, badge), encoding="utf-8")
    print(f"  {html_path.relative_to(ROOT)}")


def build_home_extras(body: str, prefix: str) -> str:
    cards = ['<div class="session-cards">']
    for session in SESSIONS:
        slug = session["slug"]
        cards.extend(
            [
                f'  <a class="session-card" href="{prefix}sessions/{slug}/index.html">',
                f'    <div class="num">Session {session["num"]}</div>',
                f'    <h3>{session["title"]}</h3>',
                f'    <p>{session["hook"]}</p>',
                "  </a>",
            ]
        )
    cards.append("</div>")
    insert = "\n".join(cards)
    return body.replace("<h2>Weekly sequence</h2>", insert + "\n<h2>Weekly sequence</h2>", 1)


def main() -> None:
    print("Building site...")
    (ROOT / "assets" / "site.css").touch(exist_ok=True)

    # Root index
    md_path = ROOT / "README.md"
    text = md_path.read_text(encoding="utf-8")
    title = extract_title(text, "Electrochemistry Lab Course")
    body = inline_svg_figures(build_home_extras(md_to_html_body(text), ""), ROOT / "index.html")
    (ROOT / "index.html").write_text(wrap_page(ROOT / "index.html", title, body, "Course overview"), encoding="utf-8")
    print("  index.html")

    # Shared
    for slug, _, md_name in SHARED_PAGES:
        build_md_page(ROOT / "shared" / md_name, ROOT / "shared" / f"{slug}.html", "Shared resource")

    # Sessions
    for session in SESSIONS:
        session_dir = ROOT / "sessions" / session["slug"]
        badge = f"Session {session['num']}"
        for page_slug, _, md_name in SESSION_PAGES:
            md_path = session_dir / md_name
            html_name = "index.html" if page_slug == "index" else f"{page_slug}.html"
            build_md_page(md_path, session_dir / html_name, badge)

    print("Done.")


if __name__ == "__main__":
    main()
