# Session 4 — Instructor Notes: Water Electrolysis Deep Dive

**Audience:** instructors and TAs only. Pair with [lecture.md](lecture.md) and [experiment.md](experiment.md).

---

## Why this session exists

Students have plated metals. Now electricity splits **molecules** of water into elemental gases, and stoichiometry becomes visible as a **2:1 volume ratio**. This also introduces hydrogen as an energy carrier and sets up overnight electrolytic rust removal for Session 5.

---

## Atomic / molecular foundations

### Water’s bonding (instructor talking points)

- H₂O: oxygen shares electrons with two hydrogens (polar covalent bonds).
- Oxygen is more electronegative → partial negative charge on O, partial positive on H.
- Liquid water also has extensive hydrogen bonding (affects boiling point, solvation) — optional aside.
- Pure water has very few ions (autoionization): H₂O ⇌ H⁺ + OH⁻ with tiny [H⁺][OH⁻] = 10⁻¹⁴ at 25 °C. That is why **pure water is a poor conductor**.

### Why we add Na₂SO₄

Electrolysis needs mobile ions. **Sodium sulfate (Na₂SO₄)** dissolves into Na⁺ and SO₄²⁻ that carry current. It is a **supporting electrolyte** — it enables conduction without (ideally) being the main reactant consumed. This workshop uses **~0.1 M Na₂SO₄** in the U-tube cell.

Baking soda (NaHCO₃) is an acceptable emergency backup, but plan on sodium sulfate.

**Critical safety contrast:**

| Electrolyte | OK for classroom gas electrolysis? | Why |
|-------------|-------------------------------------|-----|
| Sodium sulfate | **Yes — planned** | Inert supporting electrolyte |
| Baking soda / NaHCO₃ | Yes (backup) | No chlorine evolution |
| Table salt NaCl | **NO** | Chloride oxidizes → **Cl₂ gas** (toxic) |

If anyone smells chlorine or sees greenish gas character — **stop immediately**, ventilate, replace electrolyte.

---

## Half-reactions — what to teach vs what is “true”

### Classroom-friendly version

**Cathode (−):**

```
2H₂O + 2e⁻ → H₂(g) + 2OH⁻
```
(or in acid: `2H⁺ + 2e⁻ → H₂`)

**Anode (+):**

```
2H₂O → O₂(g) + 4H⁺ + 4e⁻
```
(or in base: `4OH⁻ → O₂ + 2H₂O + 4e⁻`)

**Overall:**

```
2H₂O(l) → 2H₂(g) + O₂(g)
```

### Why the 2:1 ratio appears

Oxygen half-reaction involves **4 electrons** per O₂; hydrogen involves **2 electrons** per H₂. Balancing electrons requires twice as many H₂ molecules as O₂ molecules:

```
4e⁻ make 2 H₂ and 1 O₂  ⇒  V(H₂)/V(O₂) = 2
```

At the same T and P, gas volume ∝ moles (Avogadro / ideal gas). So volumes follow mole ratio.

### Electron bookkeeping (Faraday connection)

Same idea as Session 3: charge passed determines moles of e⁻, which determines moles of gas — but today students measure **volumes**, not mass.

---

## Thermodynamics (instructor background)

Water splitting is **non-spontaneous** under standard conditions. Rough minimum theoretical voltage for water electrolysis is ~1.23 V (thermodynamic), but real cells need more due to overpotentials and resistance — classroom 9 V packs are plenty. Students need only: *“We must push with a battery; water does not split by itself.”*

---

## U-tube apparatus coaching

### What students are looking at

Glass U-tube on an acrylic stand; graphite rods through rubber stoppers; side arms near the top of each limb; red/black leads with spade connectors to a DC supply. Fill with **Na₂SO₄**, not salt. Keep side arms open or vented so pressure does not build against sealed stoppers.

### Measuring the ratio

Gas collected in each limb displaces liquid downward. Compare gas column heights (or graduated volumes) once bubbling is steady. Equal arm geometry matters for a fair ratio.

### Identifying H₂ vs O₂ without a pop test

| Clue | H₂ side | O₂ side |
|------|---------|---------|
| Rate | Faster (2× volume) | Slower |
| Electrode | Cathode (−) / black | Anode (+) / red |
| Optional | Pop test (instructor) | Relights glowing splint (advanced / careful) |

Default classroom ID: **faster = H₂ = cathode**.

### Why ratios drift from 2.0

| Cause | Effect |
|-------|--------|
| O₂ more soluble than H₂ | O₂ volume low → ratio high |
| Leaks / escaped bubbles | Either side low |
| Unequal electrode area / current distribution | Skewed rates |
| Air left in tube at t = 0 | Systematic error |
| Electrode oxidation / side reactions | Extra gases or lost current |

Accept **1.6–2.2** as a successful classroom result; discuss systematics rather than demanding perfection.

---

## Pop test protocol (instructor only)

1. Collect a **tiny** volume of H₂ in a separate small tube.
2. Move away from the main tub and from faces.
3. Brief flame → soft “pop.”
4. Never ignite sealed containers or mixed H₂/O₂.
5. Skip entirely if venue rules forbid open flame.

---

## Hydrogen as energy storage (end-of-session talk)

Frame carefully:

1. Renewables make electricity intermittently.
2. Extra electricity can electrolyze water → H₂.
3. H₂ can be stored and later oxidized in a **fuel cell** → electricity + water.
4. H₂ is an **energy carrier**, not a source — the energy came from the electricity (ultimately the sun/wind).
5. Round-trip efficiency < 100% always (heat losses).

You are **not** running a fuel cell demo this week (Session 5 uses rust removal instead). Keep fuel cells as a conceptual bridge only.

---

## Part E — Start electrolytic rust removal (handoff to Session 5)

### Correct polarity (students reverse this)

| Electrode | Connection | Role |
|-----------|------------|------|
| Rusty iron (object to clean) | Battery **−** (cathode) | Reduction / cleaning |
| Sacrificial steel or graphite | Battery **+** (anode) | Oxidizes / sacrifices |
| Electrolyte | Washing soda or baking soda | **Not NaCl** |

### What is happening chemically (simplified)

Rust is largely Fe₂O₃·nH₂O / FeOOH mixtures. At the cathode, electrochemical reduction and associated chemistry loosen / reduce oxide layers toward metallic iron; H₂ evolution often accompanies the process. The anode corrodes or evolves O₂ depending on material.

**Teaching link:** same “electricity drives non-spontaneous change” idea as water electrolysis — applied to undoing corrosion.

### Overnight logistics

- Label cells; photograph “before.”
- Keep a no-power control nail in water.
- Confirm venue policy for leaving batteries connected overnight (prep room preferred).

---

## Misconceptions

| Misconception | Correction |
|---------------|------------|
| “Bubbles are steam.” | They are **H₂ and O₂ gases**, not water vapor from boiling. |
| “Salt makes electrolysis better.” | Salt makes **chlorine** — forbidden here. |
| “Ratio must be exactly 2.000.” | Classroom data have solubility and collection errors. |
| “Hydrogen is a fuel like oil.” | It’s a **carrier**; energy was put in by electrolysis. |

---

## Board plan

1. Write overall 2H₂O → 2H₂ + O₂; circle 2:1.
2. Assign cathode/anode gases with signs.
3. Sketch displacement tubes; emphasize “no air at start.”
4. Safety slide: no NaCl.
5. Preview energy carrier concept + start derusting cells before dismissal.

---

## Optional enrichment

- Pourbaix diagrams for Fe–H₂O (why rust forms / removes — advanced).
- Overpotential differences for H₂ vs O₂ on graphite.
- Industrial alkaline electrolyzers vs PEM electrolyzers (names only).
