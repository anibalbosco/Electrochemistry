# Session 4 — Experiment: Water Electrolysis

> **Instructors:** electrolyte contrast, Faraday rate math, U-tube stoichiometry, H₂ balloon safety — [instructor.md](instructor.md).

**Session arc**

1. **Part A** — Graphite in a beaker of **tap water only** (slow / almost no reaction)
2. **Part B** — Add **Na₂SO₄**; measure **current**; link voltage and rate to Faraday’s law
3. **Part C** — Collect gases in the **U-tube**; measure volumes → **2:1 stoichiometry**
4. **Part D** — Separate demo: fill an **H₂ balloon** and pop it (instructor-led)
5. **Part E** — Start overnight **rust-removal** cells for Session 5

---

## Electrolyte — sodium sulfate (Na₂SO₄)

**Never use table salt (NaCl)** — chloride can produce toxic chlorine gas at the anode.

### Recipe — ~0.1 M Na₂SO₄

| Batch | Na₂SO₄ (anhydrous) | Water |
|-------|--------------------|-------|
| 250 mL | **~3.5 g** | Fill to 250 mL |
| 500 mL | **~7 g** | Fill to 500 mL |
| 1.0 L | **~14 g** | Fill to 1.0 L |

Stir until dissolved. Label **"0.1 M Na₂SO₄ electrolyte — NO SALT"**.

**Water:** start Parts A–B with plain **tap water** in the beaker; add solid Na₂SO₄ (or a concentrated aliquot) for Part B. Distilled water is unnecessary here.

**Baking soda backup only if Na₂SO₄ is unavailable:** 1–2 tsp NaHCO₃ per 500 mL.

---

## Part A — Tap water only (slow reaction) (20–30 min)

![Water electrolysis schematic](../../assets/figures/session4-water-electrolysis.svg)

*Figure 1 — Concept: H₂ at the cathode (−), O₂ at the anode (+). Without electrolyte, almost no current flows.*

### Materials (beaker cell)

- Beaker or clear cup (~200–400 mL)
- Two **graphite** rods (same rods you will use later in the U-tube if needed)
- DC supply or battery pack + leads (red +, black −)
- Multimeter (DC **mA** or A range) wired **in series**
- Multimeter or supply display for **voltage** across the cell
- Tap water only — **no salt, no Na₂SO₄ yet**
- Goggles

### Procedure

1. Fill the beaker with **tap water** only (~200–300 mL).
2. Clamp or hold two graphite rods so they are immersed, **2–4 cm apart**, not touching.
3. Connect: black (−) to one rod (cathode), red (+) to the other (anode).
4. Put the ammeter **in series** with one lead. Measure voltage across the two electrodes (or read the supply setpoint).
5. Power on for **2–3 minutes**. Watch carefully for bubbles.

### Expected observation

| What you look for | Typical result (tap water) |
|-------------------|----------------------------|
| Bubbles | None, or very few / slow |
| Current | Very small (often ≪ 1–10 mA depending on supply and meter) |
| Conclusion | Tap water has too few ions → poor conductor → slow electrolysis |

### Data — tap water

| Quantity | Value |
|----------|-------|
| Applied voltage V (V) | |
| Current I (mA) | |
| Bubbles visible? (Y/N, describe) | |
| Time observed (min) | |

**Talking point:** *Water itself is the reactant, but without mobile ions the circuit almost cannot run.*

---

## Part B — Add electrolyte; measure current and rate (30–45 min)

### Procedure

1. **Keep the same beaker and electrodes** (or reset with fresh tap water and the same spacing).
2. Add **Na₂SO₄** to make roughly **0.1 M** in the beaker:
   - For ~250 mL water: add **~3.5 g** anhydrous Na₂SO₄; stir until dissolved  
   - Or pour in a pre-measured aliquot of stock 0.1 M Na₂SO₄ and top up
3. Reconnect the circuit with the ammeter in series. Use the **same applied voltage** as Part A if possible (fair comparison).
4. Record current once it stabilizes (~10–30 s). Observe bubble rate at each electrode.
5. Optional: briefly raise/lower voltage and note how current (and bubbling) changes.

### Expected observation

| What you look for | Typical result (with Na₂SO₄) |
|-------------------|------------------------------|
| Bubbles | Much faster at both electrodes |
| Current | Much larger than Part A |
| Conclusion | Electrolyte ions carry charge → higher I → faster water splitting |

### Data — with Na₂SO₄

| Quantity | Value |
|----------|-------|
| Applied voltage V (V) | |
| Current I (mA) → convert to A: I = ___ A | |
| Qualitative bubble rate vs Part A | |
| Theoretical minimum for water splitting | **~1.23 V** (thermodynamic; real cells need more) |

### Calculations — voltage, current, and rate

**1. Voltage needed (classroom framing)**

- Ideal minimum to split water: **E° ≈ 1.23 V**
- Your supply must provide **at least** that, usually **more** (overpotential + resistance). Record the **applied V** you actually use.
- Optional: if the supply is adjustable, find the lowest V where bubbles become clearly visible.

**2. Reaction rate from current (Faraday)**

Charge of electrons: Faraday constant **F ≈ 96485 C/mol e⁻**

Hydrogen half-reaction uses **2 e⁻ per H₂**:

```
rate of H₂ production (mol/s) = I / (2 F)
```

with **I in amperes** (A = C/s).

Oxygen uses **4 e⁻ per O₂**:

```
rate of O₂ production (mol/s) = I / (4 F)
```

So the mole rate of H₂ is always **twice** the mole rate of O₂ for the same current — foreshadowing the volume ratio.

**3. Optional volume rate at room conditions**

At ~25 °C, 1 atm, molar volume ≈ **24.5 L/mol** (or use 22.4 L/mol at STP if your instructor prefers):

```
rate of H₂ (L/s) ≈ [I / (2 F)] × 24.5
rate of H₂ (mL/min) ≈ [I / (2 F)] × 24.5 × 1000 × 60
```

### Worked example (fill in your I)

| Step | Expression | Your value |
|------|------------|------------|
| I | ___ A | |
| ṅ(H₂) = I/(2F) | ___ mol/s | |
| ṅ(O₂) = I/(4F) | ___ mol/s | |
| Approx. H₂ volume rate | ___ mL/min | |

**Check:** ṅ(H₂) / ṅ(O₂) should equal **2** from the electron count alone.

---

## Part C — Collect gas; measure stoichiometry (45–70 min)

![Hoffman-style U-tube electrolysis apparatus with graphite electrodes](../../assets/figures/session4-hoffman-utube-apparatus.png)

*Figure 2 — U-tube apparatus for collecting H₂ and O₂ separately and comparing volumes.*

### Materials

- Hoffman-style **glass U-tube** with side arms + acrylic stand
- Graphite electrodes + rubber stoppers
- Red (+) / black (−) leads with spade connectors
- DC supply
- **0.1 M Na₂SO₄** (fill the U-tube)
- Ruler or limb graduations
- Goggles

### Build / run

1. Fill the U-tube with **Na₂SO₄** electrolyte (liquid covers electrode tips; sits below side-arm ports).
2. Insert graphite electrodes through stoppers; seal tops; keep side arms **open or vented**.
3. Connect: **black (−) = H₂ limb**, **red (+) = O₂ limb**.
4. Power on. Mark starting liquid levels.
5. Every **2–3 min**, record gas column height or volume in each limb.

### Gas volume log

| Time (min) | V_H₂ (mL or cm) | V_O₂ (mL or cm) | Ratio V_H₂/V_O₂ |
|------------|-----------------|-----------------|-----------------|
| 0 | 0 | 0 | — |
| 3 | | | |
| 6 | | | |
| 9 | | | |
| 12 | | | |
| 15 | | | |

### Expected result

V_H₂ / V_O₂ ≈ **2** (ideal). Classroom range **1.6–2.2** is a success.

Connect to Part B: the same **2:1** appears in Faraday rates **and** in collected volumes — that is the stoichiometry of

```
2H₂O(l) → 2H₂(g) + O₂(g)
```

### Pre-run checklist

- [ ] Electrolyte is **Na₂SO₄** — **not salt**
- [ ] Polarity marked; side arms vented
- [ ] Goggles on

---

## Part D — H₂ balloon fill and pop (70–80 min)

**Instructor-led demo** (students observe; do not hand students lit flames). Use a **separate** cathode setup from the U-tube if needed so stoichiometry data are already recorded.

### Idea

Collect hydrogen from the **cathode (−)** into a small balloon, then ignite for a loud **pop** — qualitative proof that the fast gas is combustible H₂.

### Materials (demo station)

- Beaker or bottle with **Na₂SO₄** + two graphite electrodes (or cathode tubing from a dedicated H₂ generator)
- Small balloon (party balloon)
- Tubing / stopper so H₂ from the cathode feeds the balloon (O₂ must **not** mix into the balloon)
- Long lighter / candle on a stick
- Fire extinguisher nearby; clear area; eye protection for everyone nearby

### Procedure (instructor)

1. Set up electrolysis so **only cathode gas** enters the balloon (anode vents separately to air).
2. Run until the balloon is **modestly** inflated (small volume — do not make a large balloon).
3. Tie off; move **away** from the electrolysis bath and from faces.
4. Ignite with a long lighter at arm’s length → sharp pop.
5. Never ignite a balloon that may contain mixed H₂/O₂; never use a sealed rigid container.

### Safety (non-negotiable)

- [ ] Instructor only handles flame
- [ ] Small balloon only; outdoor or well-cleared indoor space per venue rules
- [ ] No salt electrolyte
- [ ] Skip entirely if open flame is forbidden

---

## Part E — Start electrolytic rust removal (80–90 min)

![Electrolytic rust removal setup](../../assets/figures/session5-electrolytic-derusting.svg)

*Figure 3 — Start cells now; reveal cleaned nails at opening of Session 5.*

### Derusting electrolyte

| Ingredient | Amount |
|------------|--------|
| **Washing soda** (Na₂CO₃) preferred | **1 tbsp (~15 g) per ~250 mL** warm water |
| **or baking soda** | **1 tbsp per ~250 mL** warm water |

**Do NOT use NaCl.** Separate bath from the Na₂SO₄ electrolysis.

### Setup steps

1. Dissolve washing soda (or baking soda); pour into a small jar.
2. Rusty iron → battery **cathode (−)**.
3. Sacrificial steel or graphite → battery **anode (+)**.
4. Immerse without touching; confirm gentle bubbling.
5. Label; photograph **before**; set a control nail in plain water (no battery).
6. Leave powered overnight per venue rules.

### End-of-class checklist

- [ ] Derusting cells bubbling / current confirmed
- [ ] Controls labeled; before photos taken
- [ ] Overnight power policy confirmed

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| No bubbles in Part A | Expected if current tiny | Proceed to add Na₂SO₄ |
| Still no bubbles in Part B | Bad contacts / wrong polarity | Check clips; raise V slightly; remake ~0.1 M Na₂SO₄ |
| Current barely rises after salt… wait, **Na₂SO₄** | Not dissolved / too dilute | Stir; add more sulfate (not NaCl) |
| Chlorine smell | **Salt used** | Stop; dump; remake Na₂SO₄ |
| Ratio far from 2:1 | Leaks; late start; unequal arms | Reseat stoppers; restart after steady bubbling |
| Balloon won’t inflate | Leak; wrong electrode to balloon | Confirm cathode feed only |
| Graphite crumbling | High current / long run | Lower voltage; replace rods |

---

## Safety checklist

- [ ] No NaCl in any electrolysis bath
- [ ] Ammeter in **series** (never short the supply)
- [ ] Flames only for instructor balloon / tiny pop demo
- [ ] U-tube side arms vented (no overpressure)
- [ ] Goggles on for wet work

---

## Experiment status

- [ ] Part A/B beaker contrast pilot-tested (I before vs after Na₂SO₄)
- [ ] Faraday rate worksheet numbers checked with pilot current
- [ ] U-tube 2:1 visible in pilot
- [ ] Balloon demo rehearsed safely (or cancelled per venue)
- [ ] Rust-removal jars staged for Part E
