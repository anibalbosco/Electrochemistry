# One-Week Electrochemistry Lab Course

Five 90-minute sessions for science-oriented students, ages 15–16.

## Browse the workshop (HTML)

Open the **[workshop home](index.html)** in your browser for a navigable site with sidebar links to every session, lecture, experiment, materials list, and prep note. Markdown sources (`.md`) are kept alongside the HTML.

To rebuild HTML after editing markdown:

```bash
python scripts/build_site.py
```

Instructor/TA printable PDFs (experiment packet + lecture/instructor notes for each day) live in **[pdfs/](pdfs/)**. Regenerate after content changes:

```bash
python scripts/build_pdfs.py
```

## Read these first

| Document | Why |
|----------|-----|
| **[Multi-day setup calendar](shared/multi-day-setup.md)** | Two demos need days to develop and are both revealed on Day 5. Read this **before Session 1**, not before Session 5 |
| [Safety notes](shared/safety-notes.md) | Applies to every session |
| [Overall materials list](shared/overall-materials-list.md) | Includes the buy-ahead list of things that stop a session dead |
| [Next-year notes](shared/next-year-notes.md) | Changes to make before running the course again |
| [Teaching log](shared/teaching-log.md) | Fill in after each session, while it is fresh |

## Course theme

Electrochemistry is chemistry controlled by electrons. Students see that chemical reactions can produce electricity, that electricity can drive reactions, that atoms can be counted with a stopwatch and an ammeter, that molecules can be pulled apart, and that the same chemistry quietly destroys iron whether anybody wants it to or not.

The through-line for the week is one question, asked five times: **is this reaction happening because it wants to, or because somebody is paying for it?**

## Format

| Item | Detail |
|------|--------|
| Sessions | 5 × 90 minutes |
| Rhythm | ~20 min concept discussion + ~70 min hands-on work |
| Audience | Motivated high-school-age students (~15–16) |
| Goal | Maximize visible, memorable experiments while building real quantitative electrochemistry |

## Weekly sequence

| Session | Folder | Topic | Main hook |
|---------|--------|-------|-----------|
| 1 | [sessions/01-fruit-battery](sessions/01-fruit-battery) | Fruit Battery | Familiar objects make electricity |
| 2 | [sessions/02-copper-electroplating](sessions/02-copper-electroplating) | Copper Electroplating | Students visibly transform a metal object |
| 3 | [sessions/03-silver-plating-faraday](sessions/03-silver-plating-faraday) | Silver Plating + Faraday's Law | Count the atoms you deposited |
| 4 | [sessions/04-water-electrolysis](sessions/04-water-electrolysis) | Water Electrolysis + Gas Collection | Predict a gas volume, then go and measure it |
| 5 | [sessions/05-corrosion-and-rust-removal](sessions/05-corrosion-and-rust-removal) | Corrosion + Electrolytic Rust Removal | Find the battery nobody wanted, then run it backwards |

## The quantitative spine

Faraday's law appears on three consecutive days, pointed at three different things. This is deliberate — it is what turns a week of demonstrations into a course.

| Session | Current means | What students compute |
|---------|---------------|-----------------------|
| 3 | A plating rate | Mass, thickness, and number of silver atoms deposited |
| 4 | A gas production rate | Predicted mL of H₂, then measured — and so, for the first time, a real current efficiency |
| 5 | A corrosion rate | Grams of zinc lost per year, which is how sacrificial anodes are actually sized |

## Multi-day dependencies

| Demo | Start | Reveal |
|------|-------|--------|
| Corrosion jars A / B / C | **End of Session 1** | Session 5 |
| Electrolytic rust removal | **End of Session 4** | Session 5, opening |

Details in [shared/multi-day-setup.md](shared/multi-day-setup.md). Neither can be rescued on the day.

## Folder structure (each session)

- **README.md** — Overview, learning outcomes, and timed session plan
- **lecture.md** — Teaching script: prior-day review, explanations, quiz questions, pre-lab activity
- **experiment.md** — Bench procedure, data sheets, troubleshooting
- **instructor.md** — Deep-dive notes: chemistry, coaching, misconceptions, board plan
- **materials.md** — Per-session checklist, plus a pilot-notes table to fill in
- **preparation.md** — Pre-class setup, including anything that must happen days ahead

## Reference

Full syllabus: [electrochemistry_lab_syllabus.docx](electrochemistry_lab_syllabus.docx)

Experiment schematics (SVG): [assets/figures/](assets/figures/)

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
