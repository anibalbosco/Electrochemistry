# Session 4 — Instructor Notes: Water Electrolysis Deep Dive

**Audience:** instructors and TAs only. Pair with [lecture.md](lecture.md) and [experiment.md](experiment.md).

---

## Why this session exists

Students have plated metals. Today they discover that **splitting water needs ions in solution**, quantify **rate from current** (Faraday), prove **2:1 stoichiometry** by gas collection, and see a dramatic **H₂ balloon pop**. Overnight electrolytic rust removal still starts at the end for Session 5.

---

## Teaching sequence (keep this order)

1. **Tap water beaker** — expect disappointment (almost no bubbles). That disappointment is the lesson.
2. **Add Na₂SO₄** — same voltage → much larger current → fast bubbles. Measure I.
3. **Calculate** ṅ = I/(nF) and discuss why applied V > 1.23 V.
4. **U-tube volumes** — same 2:1 that Faraday already predicted.
5. **Balloon** — qualitative ID of H₂ (instructor only).
6. **Derusting cells** — handoff to Session 5.

---

## Atomic / molecular foundations

### Why tap water fails

- Autoionization: H₂O ⇌ H⁺ + OH⁻ with [H⁺][OH⁻] = 10⁻¹⁴ at 25 °C — vanishingly few ions.
- Tap water adds some minerals, but still a **poor conductor** compared with 0.1 M Na₂SO₄.
- Without current, half-reactions barely run → “slow reaction.”

### Why Na₂SO₄ works

- Dissolves to Na⁺ and SO₄²⁻ — **supporting electrolyte**.
- Water remains the species oxidized/reduced (classroom story).
- **Never NaCl** → Cl₂ risk at the anode.

| Electrolyte | OK? | Why |
|-------------|-----|-----|
| Sodium sulfate | **Yes — planned** | Inert supporting electrolyte |
| Baking soda | Backup only | No chlorine |
| Table salt NaCl | **NO** | Cl₂ gas |

---

## Half-reactions and the 2:1 ratio

**Cathode (−):** `2H₂O + 2e⁻ → H₂ + 2OH⁻`  
**Anode (+):** `2H₂O → O₂ + 4H⁺ + 4e⁻` (or base form with OH⁻)  
**Overall:** `2H₂O → 2H₂ + O₂`

Electron balance: 4e⁻ make **2 H₂** and **1 O₂** ⇒ volume ratio 2:1 at same T, P.

---

## Faraday coaching (Part B)

```
ṅ(H₂) = I / (2F)     ṅ(O₂) = I / (4F)
F ≈ 9.65×10⁴ C/mol
```

- Students must convert **mA → A** before dividing.
- Emphasize: **same I** already implies ṅ(H₂) = 2 ṅ(O₂) — volumes later confirm chemistry, not a new idea.
- Optional volume rate: use ~24.5 L/mol at ~25 °C (or 22.4 L/mol at STP — pick one and stay consistent).

### Voltage talking points

- Thermodynamic minimum ≈ **1.23 V**.
- Graphite + solution resistance + overpotentials → classroom cells often need **several volts**.
- “Voltage needed” = discuss 1.23 V floor + record **applied V**; if supply is adjustable, hunt the onset of visible bubbling.

**Pilot tip:** note typical I (tap) vs I (Na₂SO₄) at your fixed V so TAs know what “good” looks like.

---

## U-tube coaching (Part C)

Glass U-tube, graphite through stoppers, side arms vented, Na₂SO₄ fill. Black (−) = faster H₂ limb. Accept ratio **1.6–2.2**.

| Ratio error cause | Effect |
|-------------------|--------|
| O₂ more soluble | Ratio high |
| Escaped bubbles / leaks | Skew either way |
| Air at t = 0 | Systematic error |

---

## H₂ balloon pop (Part D) — safety first

This is a **demo**, not a free-for-all.

1. Feed **cathode gas only** into a **small** balloon (anode vents separately).
2. Modest inflation — not a large balloon.
3. Tie off; move away from the bath and faces.
4. Long lighter; arm’s length; clear space; extinguisher ready.
5. Skip if venue forbids open flame.

**Never** inflate with mixed H₂/O₂. **Never** use a rigid sealed vessel.

Loud pop startles — warn the room; protect ears if needed.

---

## Part E — Rust removal handoff

| Role | Connection |
|------|------------|
| Rusty iron | Battery **−** (cathode) |
| Sacrificial steel/graphite | Battery **+** (anode) |
| Electrolyte | Washing soda or baking soda — **not NaCl** |

Photograph before; control nail without power; overnight policy confirmed.

---

## Misconceptions

| Misconception | Correction |
|---------------|------------|
| “Bubbles are steam.” | H₂ and O₂ gases, not boiling. |
| “Salt makes it better.” | Salt makes chlorine — forbidden. |
| “We need huge voltage because water is special.” | Minimum ~1.23 V; extras are kinetics/resistance. |
| “Current and stoichiometry are unrelated.” | Faraday **is** the stoichiometry in electron language. |
| “Hydrogen is a fuel like oil.” | It’s a **carrier**; energy came from electricity. |

---

## Board plan

1. Sketch beaker + two graphite rods; label “few ions.”
2. Add Na₂SO₄; write I↑ → rate↑.
3. Write ṅ = I/(nF) and 1.23 V note.
4. Write 2H₂O → 2H₂ + O₂; circle 2:1.
5. Safety: no NaCl; balloon = instructor only.
6. Start derusting before dismissal.

---

## Optional enrichment

- Conductivity of tap vs 0.1 M Na₂SO₄ (if you have a meter).
- Overpotential on graphite vs platinum (names only).
- Industrial alkaline vs PEM electrolyzers (names only).
