# Session 3 — Instructor Notes: Silver Plating + Faraday Deep Dive

**Audience:** instructors and TAs only. Pair with [lecture.md](lecture.md) and [experiment.md](experiment.md).

---

## Why this session exists

Students saw copper move in Session 2. Now they **quantify** electrodeposition: charge → moles of electrons → moles of metal → mass → thickness. Silver is ideal because Ag⁺ + e⁻ → Ag is 1:1 (simpler stoichiometry than Cu²⁺ + 2e⁻). This is the week’s heaviest math session — go slowly on units.

---

## Atomic / electronic foundations for silver

### Silver ion and electron count

```
Ag⁺(aq) + e⁻ → Ag(s)
```

- Silver atom (Ag, Z = 47) loses one valence electron → Ag⁺.
- Plating reverses that: one electron returns → one Ag atom deposited.
- Therefore: **n_Ag = n_e** (moles silver = moles electrons) when plating is 100% efficient.

Compare with copper from Session 2:

```
Cu²⁺ + 2e⁻ → Cu    ⇒   n_Cu = n_e / 2
```

Mention this contrast so students see why the electron count in the half-reaction matters.

### Why dilute AgNO₃

Silver nitrate provides Ag⁺. Classroom concentration **0.01 M** keeps:

- Cost down
- Staining / hazard manageable
- Thin films that still look metallic

**Safety (non-negotiable):** AgNO₃ stains skin/clothes permanently dark; gloves + goggles; collect all silver waste.

---

## Faraday’s law — instructor mastery

### Charge from current and time

```
Q = I × t
```

| Symbol | Unit | Meaning |
|--------|------|---------|
| I | ampere (A) = C/s | Current |
| t | second (s) | Time |
| Q | coulomb (C) | Total charge passed |

**Trap:** students record mA but forget to convert. 20 mA = 0.020 A.

### Faraday constant

```
F = 96,485 C/mol e⁻ ≈ 9.65 × 10⁴ C/mol
```

Meaning: one mole of electrons carries ~96,485 C.

```
n_e = Q / F
```

### Stoichiometry factor (general form)

For a reduction requiring **z** electrons per metal ion:

```
n_metal = n_e / z = Q / (z F)
```

| Metal ion | z | Example |
|-----------|---|---------|
| Ag⁺ | 1 | Session 3 |
| Cu²⁺ | 2 | Session 2 |
| Al³⁺ | 3 | not used here |

### Mass and thickness

```
m = n × M
V = m / ρ
d = V / A
```

| Quantity | Silver value |
|----------|--------------|
| Molar mass M | 107.87 g/mol |
| Density ρ | 10.49 g/cm³ |
| A | geometric plated area (cm²) — **biggest student error source** |

---

## Worked example (memorize this board version)

Given: I = 0.020 A, t = 300 s, A = 10 cm², Ag plating, z = 1.

| Step | Math | Result |
|------|------|--------|
| Q | 0.020 × 300 | 6.0 C |
| n_e | 6.0 / 96485 | 6.22 × 10⁻⁵ mol |
| n_Ag | = n_e | 6.22 × 10⁻⁵ mol |
| m | 6.22e−5 × 107.87 | 6.71 × 10⁻³ g |
| V | m / 10.49 | 6.40 × 10⁻⁴ cm³ |
| d | V / 10 | 6.4 × 10⁻⁵ cm = **0.64 µm** |

**Sense-check:** visible silver films are often tenths of a micrometer to a few micrometers — students’ numbers should be in that ballpark if I, t, A are sane.

### Average current when I drifts

If students log I every 30–60 s:

```
I_avg ≈ (I₀ + I₁ + … + Iₙ) / (n+1)
```

or trapezoidal estimate. Then Q ≈ I_avg × t_total.

Do **not** use only the first reading if current falls (common as concentration polarization / surface changes).

---

## Ideal vs real plating (current efficiency)

Faraday assumes **every** electron reduces Ag⁺. Reality:

```
current efficiency η = (charge used for Ag plating) / (total charge) ≤ 1
```

Loss channels:

- H₂ evolution
- Impurity reductions
- Non-uniform current (edges plate more — “dog-boning”)
- Flaky deposit that rinses off

If calculated thickness looks “too thick” vs visual: area underestimate or optimistic η = 1. If “too thin”: efficiency < 1, area overestimate, or current logged wrong.

---

## Electrochemical series note for Ag

| Couple | E° (V) |
|--------|--------|
| Ag⁺/Ag | +0.80 |
| Cu²⁺/Cu | +0.34 |
| H⁺/H₂ | 0.00 |

Ag⁺ is a strong oxidant relative to H⁺ and Cu²⁺ — silver plates readily. That is why even dilute AgNO₃ works visually. It is also why silver ions are “eager” to reduce and why waste must be handled carefully (and why Ag stains via reduction on skin/organics).

**Anode choice:**

- **Silver anode:** replenishes Ag⁺ (like Cu anode in Session 2).
- **Inert anode:** Ag⁺ depletes; oxygen evolution possible; calculations still OK for short runs if solution starts with enough Ag⁺.

---

## Experiment coaching

### Area estimation — coach aggressively

| Object | Reasonable approach |
|--------|---------------------|
| Coin face | A = π(r)² per face; ×2 if both faces plate |
| Washer | π(R² − r²) |
| Irregular | Length × width of immersed region; say so |

Students who invent a huge area get absurdly small thickness and think Faraday “failed.”

### Ammeter in series

Multimeter must be **in series** on DC current range — not across the cell like a voltmeter (that shorts / misreads). Walk each station once.

### Timing discipline

Start stopwatch when current is flowing and stable. Stop when disconnected. Gaps in logging → poor I_avg.

### What success looks like

- Whitish / silvery sheen on copper object
- Not necessarily mirror-bright (classroom baths lack brighteners)
- Calculation completed with units at every step

---

## Misconceptions

| Misconception | Correction |
|---------------|------------|
| “Q = I + t” | Q = I × t |
| “Use mA directly in Q = It” | Convert to amperes |
| “Cu and Ag use the same z” | Ag⁺ needs 1e⁻; Cu²⁺ needs 2e⁻ |
| “Thickness must match a ruler” | Micrometers are invisible to a ruler; appearance is qualitative |
| “Faraday is wrong if deposit looks thin” | Efficiency and area errors dominate |

---

## Board plan

1. Write Ag⁺ + e⁻ → Ag; circle “1 electron per atom.”
2. Flowchart: I,t → Q → n_e → n_Ag → m → V → d.
3. Full numerical example with units.
4. Discuss why I_avg beats a single reading.
5. Bridge to Session 4: next we count **gas molecules** by volume ratio, not metal atoms by charge.

---

## Optional enrichment

- Derive z from half-reaction for Cu plating retroactively (Session 2 data).
- Mention electrolysis mass production (Al from Hall–Héroult — huge Faraday consumer).
- Introduce faradaic efficiency formally if a student is ready.
