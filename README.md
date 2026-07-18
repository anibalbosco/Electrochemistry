# One-Week Electrochemistry Lab Course

Five 90-minute sessions for science-oriented students, ages 15–16.

## Browse the workshop (HTML)

Open **[index.html](index.html)** in your browser for a navigable site with sidebar links to every session, lecture, experiment, materials list, and prep notes. Markdown sources (`.md`) are kept alongside the HTML.

To rebuild HTML after editing markdown:

```bash
python scripts/build_site.py
```

## GitHub

This project is a standalone git repository. To publish or clone:

```bash
# One-time: log in to GitHub (opens browser)
gh auth login

# Create the remote repo and push (from project root)
gh repo create Electrochemistry --public --source=. --remote=origin --push --description "One-week electrochemistry lab workshop for ages 15-16"
```

If the repo already exists on GitHub:

```bash
git remote add origin https://github.com/YOUR_USERNAME/Electrochemistry.git
git push -u origin main
```

## Course theme

Electrochemistry is chemistry controlled by electrons. Students will see that chemical reactions can produce electricity, use electricity to drive reactions, move atoms around, split molecules, store energy, and explain corrosion.

## Format

| Item | Detail |
|------|--------|
| Sessions | 5 × 90 minutes |
| Rhythm | ~20 min concept discussion + ~70 min hands-on work |
| Audience | Motivated high-school-age students (~15–16) |
| Goal | Maximize visible, entertaining experiments while building electrochemical concepts |

## Weekly sequence

| Session | Folder | Topic | Main hook |
|---------|--------|-------|-----------|
| 1 | [sessions/01-fruit-battery](sessions/01-fruit-battery) | Fruit Battery | Familiar objects make electricity |
| 2 | [sessions/02-copper-electroplating](sessions/02-copper-electroplating) | Copper Electroplating | Students visibly transform a metal object |
| 3 | [sessions/03-silver-plating-faraday](sessions/03-silver-plating-faraday) | Silver Plating + Faraday's Law | Estimate how many atoms were deposited |
| 4 | [sessions/04-water-electrolysis](sessions/04-water-electrolysis) | Water Electrolysis + Gas Collection | Split water and see a 2:1 stoichiometric ratio |
| 5 | [sessions/05-galvanic-corrosion-fuel-cell](sessions/05-galvanic-corrosion-fuel-cell) | Galvanic Corrosion + Electrolytic Rust Removal | Connect corrosion, sacrificial protection, and reversing rust with electricity |

## Folder structure (each session)

Each session folder contains:

- **README.md** — Overview, learning outcomes, and timed session plan
- **lecture.md** — Concept block: hooks, talking points, key questions, and visual aids
- **experiment.md** — Hands-on procedure, variables, observations, and data sheets
- **materials.md** — Per-session materials checklist
- **preparation.md** — Pre-class setup (overnight steps, solution prep, etc.)

## Reference

Full syllabus: [electrochemistry_lab_syllabus.docx](electrochemistry_lab_syllabus.docx)

Experiment schematics (SVG): [assets/figures/](assets/figures/)

Shared resources (add as needed):

- `shared/` — Safety notes, overall materials list, student handouts
- `shared/overall-materials-list.md` — Master equipment and chemicals list
