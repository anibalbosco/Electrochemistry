# Session 1 — Instructor Notes: Fruit Battery Deep Dive

**Audience:** instructors and TAs only. Students see the shorter [lecture.md](lecture.md) and [experiment.md](experiment.md). Use this page to answer “why?” with confidence.

---

## Why this session exists

Students already know “batteries make electricity.” The fruit cell makes the chemistry visible: two different metals, an acidic juice, a measurable voltage, and (with luck) a tiny load. Your job is to connect that demo to **electrons leaving metal atoms**, **ions moving in solution**, and the idea that **oxidation and reduction are always paired**.

---

## Atomic and electronic foundations

### Atoms, electrons, and valence shells (what students need)

Keep this brief but precise if students lack chemistry background:

1. Atoms have a **nucleus** (protons + neutrons) and **electrons** outside.
2. Chemistry of batteries is almost entirely about the **outermost (valence) electrons**.
3. Metals tend to **lose** valence electrons → become **positive ions** (cations).
4. In solution, those electrons do not vanish — they travel through a wire and are gained by something else (reduction).

### Zinc and copper electron structure (instructor level)

| Metal | Atomic number | Valence electrons (simplified) | Typical ion | What that means here |
|-------|---------------|--------------------------------|-------------|----------------------|
| Zn | 30 | 2 (4s²) | Zn²⁺ | Readily loses 2e⁻ → dissolves as Zn²⁺ |
| Cu | 29 | 1 (4s¹) in free atom; chemistry often treated as Cu²⁺/Cu | Cu²⁺ or Cu⁺ | Less eager than Zn to dissolve in this cell |

**Teaching tip:** You do **not** need full electron configurations with students. Say: *“Zinc holds its outer electrons less tightly than copper in this setup, so zinc is the metal that oxidizes.”*

### What “oxidation” means at the atom scale

At the zinc surface:

```
Zn(s) → Zn²⁺(aq) + 2e⁻
```

- The solid zinc atom leaves the metal lattice as Zn²⁺ into the juice.
- The two electrons stay in the metal and can travel through the external wire.
- That is why the zinc electrode is the **anode** (oxidation site) and, in a galvanic cell, the **negative** terminal (source of electrons into the external circuit).

At the copper surface (simplified classroom story for acidic fruit juice):

```
2H⁺(aq) + 2e⁻ → H₂(g)
```

- Protons from the acidic juice gain electrons and become hydrogen gas.
- Copper mainly provides a surface for reduction; it is **not** the main reactant being consumed (though real cells can have side reactions).

**Nuance for you (not always for students):** In some fruit cells, dissolved oxygen or other species also accept electrons. The H⁺ → H₂ story is the clean teaching model; bubbles may be subtle.

---

## Periodic trends and the electrochemical series

### Activity / reactivity series (classroom version)

More active metals oxidize **preferentially**:

```
Mg > Al > Zn > Fe > Sn > Pb > (H) > Cu > Ag > Au
```

**How to use this in Session 1:**

- Zn is above Cu → Zn oxidizes; Cu is the better cathode surface.
- Swap electrodes in discussion: if both metals are the same, ΔE ≈ 0.
- If students try Al or Mg: expect different voltages and often messy oxide layers (Al₂O₃ film can block current).

### Standard reduction potentials (instructor reference)

Approximate aqueous standard potentials (vs SHE, acidic):

| Half-reaction | E° (V) |
|---------------|--------|
| Zn²⁺ + 2e⁻ → Zn | −0.76 |
| 2H⁺ + 2e⁻ → H₂ | 0.00 |
| Cu²⁺ + 2e⁻ → Cu | +0.34 |

Cell potential (ideal Zn/H⁺ picture):

```
E°_cell ≈ E°_cathode − E°_anode(as oxidation)
       ≈ 0.00 − (−0.76) = +0.76 V
```

Students measure ~0.8–1.0 V — close enough for a lemon. Real fruit cells are **not** standard conditions (unknown [H⁺], mixed ions, internal resistance), so do not oversell exact E° matching.

**Key instructor point:** Voltage measures a **difference in chemical preference** for holding electrons, not “how much electricity is stored.”

---

## Lecture concepts — expanded

### Galvanic cell definition

A **galvanic (voltaic) cell** converts chemical energy into electrical energy spontaneously:

- Oxidation at anode, reduction at cathode
- Electrons flow **anode → cathode** in the external wire
- Ions migrate in the electrolyte to keep charge balanced

Without ion motion, the circuit is incomplete: electrons pile up on one side, charge separation stops the reaction.

### Anode / cathode sign convention (the #1 confusion)

| Cell type | Anode process | Anode sign | Cathode process | Cathode sign |
|-----------|---------------|------------|-----------------|--------------|
| Galvanic (Session 1) | Oxidation | **−** | Reduction | **+** |
| Electrolytic (Session 2+) | Oxidation | **+** (connected to battery +) | Reduction | **−** |

Memory aid for instructors: *Anode = oxidation always. Sign depends on whether the cell is spontaneous or driven.*

### Voltage vs current vs power

| Quantity | What it is | Fruit cell reality |
|----------|------------|--------------------|
| Voltage (V) | Electrical potential difference | Often ~0.8–1.0 V per cell |
| Current (I) | Charge flow rate | Usually tiny (µA–mA) |
| Power (P = VI) | Energy per time | Too small for most loads unless many cells / good contacts |

Students often think “1 V is a lot.” Emphasize: a AA battery is ~1.5 V **and** can supply much higher current. Lemons fail LEDs more from **current / internal resistance** than from voltage alone.

### Internal resistance

Model a real cell as an ideal voltage source in series with resistance \(R_\text{int}\):

```
V_load = E − I·R_int
```

When a load draws current, measured voltage **drops**. Rolling fruit, clean metal, larger electrode area, and better juice contact all lower \(R_\text{int}\).

### Series vs parallel

- **Series:** voltages add; same current through each cell. Needed for LED (~2 V).
- **Parallel:** voltage stays ~one cell; current capacity increases (in ideal theory). Fruit cells rarely reward parallel setups because contacts and mismatches dominate.

---

## Experiment notes — what to watch for

### Build quality that actually matters

1. **Roll the fruit** — ruptures juice sacs; improves ion pathways.
2. **Gap between electrodes** — touching shorts the cell (0 V externally).
3. **Clean metal** — oxide/dirt raises resistance.
4. **Clip polarity** — decide a convention (e.g. red → Cu) and stick to it so series wiring is consistent.

### Typical numbers (pilot these yourself)

| Setup | Expected |
|-------|----------|
| Lemon + Zn + Cu | ~0.8–1.0 V open circuit |
| Potato / apple | Often slightly lower or similar |
| 3 cells in series | ~2.4–3.0 V open circuit |
| Voltage under LED load | Often collapses if current demand is high |

### Why the LED may fail even at “enough volts”

- LED needs both **forward voltage** (~1.8–2.2 V for red) **and** a few mA.
- Fruit cell can show 2.7 V open-circuit but sag under load.
- Wrong LED polarity → no light.
- Prefer **red diffused LEDs**; blue/white need higher voltage.

### Extension: metal comparisons (how to narrate results)

If students replace Zn with Fe or Al:

- Fe vs Cu: smaller voltage than Zn vs Cu (Fe less active than Zn).
- Al vs Cu: theoretically high activity, but Al₂O₃ film often suppresses performance — great teachable moment about **surface chemistry**, not just the activity table.

### Bridge to Session 2 (no overnight copper prep)

Session 2 uses **dissolved copper sulfate (CuSO₄)** mixed day-of (or shortly before). Do not start vinegar/salt copper jars at the end of Session 1. Preview only: tomorrow electricity will force Cu²⁺ ions onto a nail.

---

## Misconceptions to preempt

| Misconception | Better framing |
|---------------|----------------|
| “The lemon is the battery.” | The lemon is the **electrolyte**; the metals drive the chemistry. |
| “Electricity is stored in the lemon.” | Energy comes from the **chemical reaction**, mainly Zn oxidation. |
| “Electrons travel through the juice.” | Electrons travel in the **wire**; **ions** travel in the juice. |
| “Anode is always +.” | Only true for driven electrolytic cells; here anode is −. |
| “Higher voltage always means brighter LED.” | Current and internal resistance matter as much as voltage. |

---

## Board plan (20 min concept block)

1. Draw lemon + Zn + Cu; label anode/cathode.
2. Write Zn oxidation and H⁺ reduction half-reactions.
3. Draw external e⁻ path and internal ion path (two different arrows).
4. Show one cell vs three in series.
5. Preview Session 2: *tomorrow we reverse the idea — electricity moves metal atoms.*

---

## Optional enrichment (if a strong student asks)

- Nernst equation qualitatively: concentration and pH shift voltage.
- Salt bridges vs fruit electrolyte (why Daniell cells use two compartments).
- Why commercial batteries use solid electrolytes / pastes (leakage, shelf life, current density).
