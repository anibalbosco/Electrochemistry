# Session 1 — Experiment: Fruit Battery

**Main experiment:** Lemon/lime/potato battery — generating electricity from chemistry.

> **Instructors:** expected voltages, LED failure modes, and extension interpretation — [instructor.md](instructor.md).

![Single fruit cell schematic](../../assets/figures/session1-fruit-cell.svg)

*Figure 1 — Single galvanic cell: Zn anode (−), Cu cathode (+), electrons through the wire, ions through the fruit juice.*

---

## Materials checklist (per group)

| Item | Spec / notes |
|------|----------------|
| Fruit | 3–6 firm lemons, limes, potatoes, or apples |
| Zinc electrode | Galvanized nail or zinc strip (2+) |
| Copper electrode | Copper strip, stiff wire, or clean penny (2+) |
| Multimeter | DC voltage (and current if available) |
| Alligator clips | 4–6 leads |
| Load | Red LED (1.8–2.2 V forward) and/or 1.5–3 V buzzer |
| Optional | pH paper, table salt, aluminum foil |

---

## Part 1 — Build one cell (25–45 min)

### Procedure

1. Choose one fruit. **Roll** a citrus fruit firmly on the bench for 10–15 s (breaks juice sacs). For potato/apple, squeeze gently or make a shallow slit for better contact.
2. Insert the **zinc** electrode (galvanized nail or zinc strip) about halfway in — do not push all the way through.
3. Insert the **copper** electrode **2–3 cm away** from the zinc. Electrodes must **not touch** inside the fruit (touching shorts the cell → ~0 V).
4. Set the multimeter to **DC voltage** (V⎓), typically the 2 V or 20 V range.
5. Clip **red (VΩmA)** lead to **copper**; clip **black (COM)** to **zinc**.  
   - Expected: copper reads **positive** relative to zinc (~0.8–1.0 V for lemon).
6. Record the open-circuit voltage. Wait 2 minutes; record again (note drift).

### Expected results

| Fruit (typical) | Open-circuit voltage |
|-----------------|----------------------|
| Lemon / lime | ~0.8–1.0 V |
| Potato / apple | ~0.5–0.9 V (varies) |

### Observations to record

| Quantity | Value | Notes |
|----------|-------|-------|
| Fruit type | | |
| Electrode materials | Zn: ___ / Cu: ___ | |
| Electrode separation (cm) | | |
| Open-circuit voltage (V) | | |
| Voltage after 2 min (V) | | |
| Meter polarity (which metal +?) | | |

### Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| ~0 V | Electrodes touching | Separate inside the fruit |
| Very low V | Dry fruit, poor contact | Roll fruit; re-insert; try fresher fruit |
| Unstable reading | Loose clips | Secure alligator clips on bare metal |
| Negative voltage | Leads swapped | Swap clips or note polarity and continue |

---

## Part 2 — Series battery challenge (45–60 min)

![Cells in series schematic](../../assets/figures/session1-series-cells.svg)

*Figure 2 — Cells in series: connect Cu of one cell to Zn of the next; voltages add (~0.9 V each).*

### Procedure

1. Build **2–3** identical cells (one fruit each) the same way as Part 1.
2. Measure and record each cell’s voltage alone first.
3. Wire **in series**:
   - Copper of cell 1 → zinc of cell 2 (alligator lead)
   - Copper of cell 2 → zinc of cell 3
4. Measure total voltage between the **free copper** (positive end) and **free zinc** (negative end).
5. Compare measured total to the sum of the individual voltages.

### Challenge question

*"If each cell is 0.9 V, how many cells do you need for a 3 V buzzer? For a 1.5 V clock?"*

### Data table

| # cells in series | V₁ | V₂ | V₃ | V_total measured | V_sum individual | Match? |
|-------------------|----|----|----|------------------|------------------|--------|
| 1 | | — | — | | | |
| 2 | | | — | | | |
| 3 | | | | | | |

### Expected

3 lemon cells ≈ **2.4–3.0 V** open circuit (enough in voltage for many red LEDs; current may still be limiting).

---

## Part 3 — Power something (60–75 min)

### Load options (try in order)

1. Multimeter on **DC mA** current range (small load — should work)
2. **Red LED** — longer leg / flat side conventions: longer leg usually **+** (to copper end of series string). Needs ~2 V+ and a few mA. Use **3 cells** first.
3. Active buzzer rated **1.5–3 V DC** (with leads)
4. Low-voltage potato/lemon clock kit (if available)

### LED wiring reminder

- Series string: free **copper** → LED **anode (+)**; LED **cathode (−)** → free **zinc**
- If it does not light, reverse the LED once before concluding failure

### Measurements

| Load | # cells | Voltage under load (V) | Current (mA) | Works? |
|------|---------|------------------------|--------------|--------|
| Open circuit | | | — | |
| LED | | | | |
| Buzzer/clock | | | | |

### Discussion after attempt

- Did voltage **drop** when connected to a load? (Internal resistance)
- Why might the LED need more **current** than the fruit cell can supply?

---

## Extensions — Side experiments (75–85 min)

Students choose one or more:

### A. Compare fruits

Same Zn/Cu electrodes, different fruits → compare open-circuit voltage.

### B. Compare metals

Same fruit; replace Zn with aluminum foil, steel nail, or Mg (if available) vs. copper. Record V and note any oxide-film issues (especially Al).

### C. pH changes

After 10+ min under load, touch pH paper near each electrode. Hypothesis: cathode region may become less acidic.

### D. Salt addition

Add a **pinch** (~0.25 tsp) of table salt into a slit in the fruit; re-measure V and current under the same load.

### E. Parallel vs. series

Two cells in parallel (Cu–Cu and Zn–Zn tied): voltage ≈ one cell; compare current capability to series if meters allow.

### Extension report template

| Variable changed | Control | Result | Explanation (hypothesis) |
|------------------|---------|--------|--------------------------|
| | | | |

---

## Wrap-up (85–90 min)

1. Clean stations; fruit goes to waste (not food waste).
2. Quick share: best voltage, whether the LED lit, one surprising result.
3. Preview Session 2: *tomorrow we dissolve copper sulfate and use electricity to plate copper onto a nail.*

---

## Student handout — Quick reference

**Build:** Roll fruit → Zn + Cu, not touching → measure V  
**Series:** Cu of one cell to Zn of the next → voltages add  
**LED:** Needs ~3 cells + correct polarity; voltage may sag under load  
**Safety:** Do not eat experimental fruit; wash hands after metals

---

## Experiment status

- [ ] Procedure pilot-tested with actual fruit/electrodes
- [ ] Typical voltage range documented (record: ___ V)
- [ ] LED/buzzer compatibility verified (# cells needed: ___)
- [ ] Extension options ranked by time available
- [ ] Wrap-up / Session 2 preview timed
