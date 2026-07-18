# Session 3 — Lecture: Faraday's Law and Silver Plating

**Target duration:** ~20 minutes

---

## Opening hook (0–10 min)

Show a dull copper coin or washer.

*"If we plate this with silver for exactly 5 minutes at 0.02 A, can we calculate how many silver **atoms** landed on the surface — without weighing it?"*

Answer preview: **Yes — with Faraday's law.**

---

## Core concepts (10–25 min)

### 1. Silver reduction

```
Ag⁺(aq) + e⁻ → Ag(s)
```

- Each silver ion needs **one electron** to become silver metal
- So: **moles of electrons = moles of silver deposited** (1:1)

### 2. Charge, current, and time

| Symbol | Meaning | Units |
|--------|---------|-------|
| **I** | Current | Amperes (A) = C/s |
| **t** | Time | Seconds (s) |
| **Q** | Charge | Coulombs (C) |

**Q = I × t**

Example: 0.020 A for 300 s → Q = 6.0 C

### 3. Faraday constant

**F = 96,485 C/mol** — charge of one mole of electrons

**n_e = Q / F**

Example: 6.0 / 96,485 = 6.22 × 10⁻⁵ mol e⁻

### 4. From moles to mass to thickness

1. n_Ag = n_e (1 electron per Ag⁺)
2. m_Ag = n_Ag × 107.87 g/mol
3. Volume V = m_Ag / ρ_Ag  (ρ_Ag = 10.49 g/cm³)
4. Thickness d = V / A  (A = plated area in cm²)

### 5. Worked example (on board)

| Step | Calculation | Result |
|------|-------------|--------|
| Q | 0.020 A × 300 s | 6.0 C |
| n_e | 6.0 / 96,485 | 6.22 × 10⁻⁵ mol |
| m_Ag | n × 107.87 | 0.00671 g |
| V | m / 10.49 | 6.40 × 10⁻⁴ cm³ |
| d (A = 10 cm²) | V / A | 6.4 × 10⁻⁵ cm ≈ **0.64 µm** |

### 6. Ideal vs. real plating

Faraday gives the **maximum** if every electron plates silver.

Reality may differ because:

- Side reactions consume current (H₂ evolution, etc.)
- Deposit may be porous or non-uniform
- Current may drift over time
- Not all surface area plates equally

---

## Wrap-up (80–90 min)

- How close was your calculated thickness to what you see?
- What would happen with a **silver anode** vs. inert anode?
- Where else is Faraday's law used? (electrolysis industry, battery design, analytical chemistry)

---

## Visual aids

- [ ] Flowchart: I, t → Q → n → m → d
- [x] Plating setup (see experiment page and figure below)

![Silver plating cell with ammeter](../../assets/figures/session3-silver-plating.svg)

- [ ] Optional: stacked-atom illustration for "thickness"

---

## Vocabulary

- [ ] Faraday constant
- [ ] Coulomb
- [ ] Stoichiometry of electron transfer
- [ ] Current efficiency (introductory)

---

## Bridge to Session 4

*"We've moved metal atoms with electricity. Next we split **water molecules** into hydrogen and oxygen — and measure the gases to prove the 2:1 ratio."*
