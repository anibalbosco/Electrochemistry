# Session 3 — Experiment: Silver Plating + Calculations

> **Instructors:** bath design, the displacement problem, limiting current, live entry — [instructor.md](instructor.md).

**Session arc**

1. **Part A** — Estimate the plated area
2. **Part B** — Build the cell: series resistor sets the current, live entry protects the copper
3. **Part C** — Timed plating run, with a **no-power control coin** running alongside
4. **Part D** — Faraday calculations, compared against the prediction
5. **Part E** — Compare plated vs control; measure the pH change and check it against the charge

---

## The bath — 0.05 M AgNO₃ in 0.2 M KNO₃

Two dissolved things, doing two different jobs. Students should be able to say which is which.

| Component | Job | Consumed? |
|-----------|-----|-----------|
| **AgNO₃, 0.05 M** | Supplies the Ag⁺ that becomes the coating | **Yes** — it is the reactant |
| **KNO₃, 0.2 M** | Supporting electrolyte: carries current through the solution | **No** — spectator, like Session 4's sulfate |

### Recipe

**Distilled water only.** Tap chloride precipitates AgCl and ruins the bath.

| Batch | AgNO₃ (0.05 M) | KNO₃ (0.2 M) |
|-------|----------------|--------------|
| 250 mL | **2.12 g** | **5.05 g** |
| 500 mL | **4.25 g** | **10.11 g** |

Sodium nitrate works identically if you have it instead: **4.25 g / 250 mL**, **8.50 g / 500 mL**.

**Half-strength option** if silver is tight: 0.025 M AgNO₃ (1.06 g / 250 mL) with the same KNO₃, and halve the target current to about 1 mA.

**Mixing order:** dissolve the KNO₃ first, then add the AgNO₃ and stir until clear. Label `0.05 M AgNO₃ / 0.2 M KNO₃ — gloves — silver waste only` with the date.

### Chloride check on the KNO₃ — 30 seconds, do it before mixing a full batch

Any chloride contamination in your nitrate salt will fog the bath with AgCl. Put a few drops of your dissolved KNO₃ into a few drops of AgNO₃ solution on a watch glass.

- **Stays clear** → good, proceed.
- **Goes milky white** → your nitrate is contaminated. Find a purer grade; do not use it.

### Volume per group

**30–40 mL** — enough to cover the object with the electrodes 2–3 cm apart.

---

## Part A — Estimate the plated area (42–47 min)

You cannot calculate a thickness without an area, and area is where most groups go wrong.

**Coin, one face:** measure diameter *d* in cm → A = π(d/2)².
**Both faces plate:** A = 2π(d/2)².
**Washer, one side:** A ≈ π(R²outer − R²inner).
**Irregular:** approximate the immersed part as length × width and write down that you approximated.

| Dimension | Value (cm) | Formula used | Area A (cm²) |
|-----------|------------|--------------|--------------|
| | | | |

**Tip:** a typical coin face is 2–4 cm². If you calculated 12 cm², you used the diameter where the radius belongs.

---

## Part B — Build the cell (47–52 min)

![Silver plating with ammeter in series](../../assets/figures/session3-silver-plating.svg)

*Figure 1 — Object on (−) as the cathode, graphite anode on (+), ammeter in series, and a resistor that fixes the current.*

### The circuit

| Part | Connects to |
|------|-------------|
| **Object to plate** | Battery **(−)** — this makes it the cathode |
| **Graphite anode** | Battery **(+)** |
| **1 kΩ resistor** | In series, on either lead — **required, not optional** |
| **Multimeter on DC mA** | In series |

### Why the resistor is not optional

Last year this cell was run by setting a voltage and hoping. It does not work, because the current then depends on how deep the electrodes are, how far apart they are, and how the solution is behaving — so every group gets a different current and half of them get a bad deposit.

With 0.2 M KNO₃ the solution barely resists current at all, so a **1 kΩ resistor in series completely dominates the circuit and sets the current for you**:

```
I ≈ (3 V − about 1 V across the cell) / 1000 Ω  ≈  2 mA
```

Change the resistor to change the current, and nothing else matters much. That is what makes this experiment reproducible across eight benches.

| Resistor (3 V pack) | Approximate current |
|---------------------|---------------------|
| 2.2 kΩ | ~1 mA |
| **1 kΩ** | **~2 mA — use this** |
| 470 Ω | ~4 mA |

### Target current density — the number that decides whether it works

Aim for **0.5–1.0 mA/cm²**, which for a typical 3 cm² coin means about **2–3 mA**.

Go much above that and you exceed the rate at which Ag⁺ can diffuse to the surface. Then the deposit stops being a coating and starts being a **dendrite** — a grey fluffy tree that grows off the tips and falls off. Gentle stirring raises the ceiling, so stir if you can.

### Clean the object

1. Sand or steel-wool until bright metal shows all over.
2. Rinse with distilled water, pat dry.
3. **Do not touch the surface to be plated.** Handle by the edge with forceps. Finger oil ruins adhesion.

### Live entry — the step that decides whether the coating sticks

**Connect the circuit and confirm current is flowing BEFORE the object touches the solution.**

Here is why. Copper spontaneously reacts with silver ions the instant they meet, with no power at all:

```
Cu(s) + 2Ag⁺(aq) → Cu²⁺(aq) + 2Ag(s)        E° = +0.46 V
```

That reaction deposits a loose, powdery, badly stuck layer of silver — and anything you plate on top of it flakes off along with it. Powering the object first makes it a cathode from the moment it gets wet, which stops the copper dissolving and stops the loose layer forming.

**The sequence, in order:**

1. Wire everything up with the object held **above** the solution.
2. Switch on. Confirm the ammeter reads a small current (it will read near zero until the circuit closes through the liquid).
3. **Lower the object in while powered.** Start the stopwatch as it goes under.
4. At the end: **lift the object out while still powered**, then switch off.

Never let the object sit in the bath unpowered. Not before, not after, not "just for a second."

### Setup record

| Item | Value |
|------|-------|
| Object | |
| Area A (cm²) | |
| Bath | **0.05 M AgNO₃ / 0.2 M KNO₃** |
| Solution volume (mL) | |
| **Starting pH** | |
| Anode | Graphite |
| Series resistor (Ω) | |
| Supply voltage | |
| Target time (s) | **900 s (15 min)** |
| Initial current (mA) | |
| Current density (mA/cm²) | I/A = |

---

## Part C — Timed run, plus the control (52–70 min)

### Set the control going at the same moment

Take a **second, identically cleaned coin**. Drop it into a small dish of the same bath with **no wires attached at all**, at the same time you start plating. Leave it the full 15 minutes.

This coin is the experiment's most valuable single piece of data. It shows you exactly what the copper does on its own, so that at the end you can tell the difference between silver you *plated* and silver that simply *arrived*.

### The plating run

1. Start the stopwatch as the powered object enters the solution.
2. Log the current every 60 s.
3. Stir gently every couple of minutes, or leave a slow stirrer running.
4. At 900 s, lift the object out **while powered**, then switch off.
5. Rinse with distilled water, pat dry. Do not scrape it.
6. **Burnish** lightly with a soft cloth or a soft brush. A matte deposit comes up noticeably brighter — this is normal practice, not cheating.

### Current log

| Time (s) | I (mA) | I (A) = mA ÷ 1000 | Notes |
|----------|--------|-------------------|-------|
| 0 | | | |
| 180 | | | |
| 360 | | | |
| 540 | | | |
| 720 | | | |
| 900 | | | |

**Average current:** I_avg = ______ mA = ______ **A**

With the resistor in place the current should be nearly flat. **A steady current is itself a result** — last year's cell, without a resistor and without supporting electrolyte, drifted all over the place.

---

## Part D — Faraday calculations (70–80 min)

Use **I_avg in amperes** and **t in seconds**.

| Quantity | Value |
|----------|-------|
| Faraday constant F | 96,485 C/mol |
| Molar mass Ag | 107.87 g/mol |
| Density ρ(Ag) | 10.49 g/cm³ |
| Electrons per Ag⁺ | **z = 1** |

| Step | Formula | Your calculation | Result |
|------|---------|------------------|--------|
| 1. Charge | Q = I_avg × t | | ______ C |
| 2. Moles e⁻ | n_e = Q / 96,485 | | ______ mol |
| 3. Moles Ag | n_Ag = n_e (since z = 1) | | ______ mol |
| 4. Mass Ag | m = n_Ag × 107.87 | | ______ g |
| 5. Volume Ag | V = m / 10.49 | | ______ cm³ |
| 6. Thickness | d = V / A | | ______ cm |
| 7. In micrometres | d × 10,000 | | ______ **µm** |
| 8. Atoms | n_Ag × 6.022×10²³ | | ______ atoms |

### Worked check (instructor board version)

I = 0.0020 A, t = 900 s, A = 3.14 cm²:

Q = **1.80 C** → n_e = **1.87×10⁻⁵ mol** → m = **2.01 mg** → V = 1.92×10⁻⁴ cm³ → d = **0.61 µm** → **1.1×10¹⁹ atoms**

Two milligrams of silver, six tenths of a micrometre thick, eleven billion billion atoms. All three of those numbers describe the same object.

---

## Part E — Compare with reality (80–86 min)

### E1 — Your coin versus the control coin

Put them side by side.

| | Plated coin (powered) | Control coin (no power) |
|--|----------------------|-------------------------|
| Colour | | |
| Even or patchy? | | |
| Shiny or matte/grey? | | |
| Does it survive a firm rub with a cloth? | | |

The control will have picked up silver too — that is the displacement reaction — but it should be **duller, greyer, patchier, and it should rub off**. The powered coin should be more even and should stay put. If they look the same, your live entry did not work, and the honest conclusion is that most of your coating arrived chemically rather than electrically.

### E2 — Check the pH against the charge

The graphite anode is splitting water and releasing protons:

```
2H₂O → O₂ + 4H⁺ + 4e⁻
```

So the moles of H⁺ released should equal the moles of electrons you already calculated in step 2.

| Quantity | Value |
|----------|-------|
| Moles of e⁻ (from step 2) | ______ mol |
| Bath volume in litres | ______ L |
| Predicted [H⁺] added = mol / L | ______ M |
| **Predicted pH** = −log[H⁺] | ______ |
| **Measured final pH** | ______ |

For the worked example above in 30 mL, this predicts **pH ≈ 3.2**, down from about 7.

If your measurement lands near the prediction, you have just confirmed that essentially every electron did the job you assigned it. If the measured pH is much *higher* than predicted, then something at the cathode was consuming protons instead of depositing silver — which is exactly what happens when a bath is run too hard or for too long and runs out of Ag⁺.

### Discussion prompts

1. Can you *see* a layer 0.6 µm thick? What does the calculation actually predict you will observe?
2. Did your current stay flat? What would have made it drift?
3. Your coin and the control coin both gained silver. Which process do you trust, and why?
4. What would happen if you left this running overnight?

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Grey fluffy growth instead of a coating | Current density too high — you are past the diffusion limit | Bigger resistor; stir; check your area estimate |
| Coating rubs straight off | Displacement layer underneath — object entered unpowered | Re-clean and repeat with live entry |
| Deposit black rather than silvery | Very fine silver, from too much current | Lower the current; burnish afterwards |
| Bath cloudy white from the start | Chloride — tap water, or contaminated KNO₃ | Remake with distilled water and tested nitrate |
| Bath turns faintly blue over the day | Cu²⁺ from displacement | Expected; a reason not to leave objects sitting in the bath |
| Current much lower than expected | Bad clip, meter fuse, electrodes not both immersed | Check the fuse first |
| Current drifting downward | Poor contact, or bath running low on silver | Check clips; at 0.05 M depletion is under 2% per run, so suspect the contact |
| Calculated thickness absurd | mA not converted to A, or area wrong | Recheck both; 0.1–2 µm is the sane window |

---

## Safety

- **Gloves and goggles mandatory.** AgNO₃ stains skin and clothing dark brown-black and the stain is effectively permanent — it is metallic silver forming in your skin
- Instructor prepares and dilutes all silver solutions; students never handle solid AgNO₃
- Small volumes only, 30–40 mL per group
- Keep the bath out of direct light; silver nitrate is light-sensitive
- **Never add ammonia to silver nitrate.** Ammoniacal silver solutions form explosive silver nitride on standing. Online "silver mirror" recipes use exactly this — do not follow them
- All silver-bearing liquid goes to the labeled **silver waste** container, never down the drain

### Silver recovery — worth doing, and it teaches something

Drop a coil of bare copper wire into the silver waste bottle and leave it. The same displacement reaction that spoiled last year's overnight run will strip essentially every silver ion out of the waste and leave it as grey metallic fluff on the wire, which you can filter and keep. The equilibrium constant is about 3×10¹⁵, so it goes to completion.

The reaction that was the problem in the cell is the standard industrial method for recovering silver from spent solution. That is worth pointing out.

---

## Experiment status

- [ ] KNO₃ chloride-tested against AgNO₃ (stayed clear)
- [ ] 0.05 M AgNO₃ / 0.2 M KNO₃ mixed with distilled water and labeled
- [ ] 1 kΩ resistors, one per station
- [ ] Pilot run done: current ______ mA, appearance ______
- [ ] Live entry rehearsed by every TA
- [ ] Second cleaned coin per group, for the no-power control
- [ ] pH meter or paper checked against a known buffer
- [ ] Silver waste container labeled; copper coil in it for recovery
