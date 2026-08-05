# Session 5 — Experiment: Corrosion and Electrolytic Rust Removal

> **Instructors:** reveal protocol, why measured voltages fall short of predictions, jar narratives — [instructor.md](instructor.md).

**Session arc**

1. **Part A** — Open the overnight derusting cells (the reveal)
2. **Part B** — Metal-pair cells: **predict** the voltage, measure it, then measure the **current** and convert it into a corrosion rate
3. **Part C** — Corrosion jars A / B / C
4. **Part D** — The whole week on one table

---

## Solutions used today

### Saltwater — for corrosion and galvanic demos only

| Ingredient | Amount |
|------------|--------|
| Table salt (NaCl) | **25–50 g** per 500 mL |
| Water | 500 mL tap water |

That is roughly **5–10% w/v**. Label it: **"CORROSION DEMOS ONLY — NOT FOR ELECTROLYSIS OR DERUSTING."**

Today is the one day of the week salt is allowed in the room, and it is allowed only because nothing here is being driven hard enough to make chlorine. Keep it physically apart from the derusting jars.

### Derusting bath (mixed in Session 4)

| Ingredient | Amount |
|------------|--------|
| Washing soda (Na₂CO₃), preferred | **1 tbsp (~15 g) per 250 mL** warm water |
| or baking soda (NaHCO₃) | **1 tbsp per 250 mL** warm water |

---

## Part A — The reveal (0–15 min)

![Electrolytic rust removal](../../assets/figures/session5-electrolytic-derusting.svg)

*Figure 1 — Cells started at the end of Session 4: rusty iron on the cathode (−), sacrificial anode on (+), in washing soda solution.*

Do this before any teaching. It is the best visual of the week and it buys you fifteen minutes of attention.

### Procedure

1. **Disconnect the power before touching anything.** Every time, without exception.
2. Lift the treated nail out with forceps or gloved fingers and rinse it under running water.
3. A stiff brush or a wipe with a paper towel removes the loosened black film. Say what you are doing and why — the electrochemistry loosens the oxide, it does not vaporise it.
4. Put the treated nail, the **unpowered control nail**, and the **before photo** side by side.
5. Look at the rest of the cell too, not just the nail: the anode is pitted and dark, the solution is cloudy orange-brown, and there is sludge at the bottom. That material is the rust, relocated.

### Observation sheet

| Sample | Electrolyte | Powered? | Appearance after rinse | Cleaner than control? |
|--------|-------------|----------|------------------------|----------------------|
| Treated nail | Washing soda | Yes | | |
| Control nail | Same solution | **No** | | |
| Sacrificial anode | — | Yes | | |
| The bath itself | — | — | | |

The control is the point. Soaking a rusty nail in alkaline solution overnight does something all by itself, and without the control you cannot claim the electricity did anything.

### Discussion prompts

- Which electrode was the cathode? What happens at a cathode?
- How is this the same as Session 4's electrolysis? *(Same driven cell, same hydrogen at the negative electrode.)*
- Where did the rust actually go?
- What would have happened if we had reversed the clips? *(We would have dissolved the nail. This is the entire experiment in one wire swap.)*

---

## Part B — Metal-pair cells: predict, then measure (30–55 min)

![Zn–Cu galvanic cell in saltwater](../../assets/figures/session5-galvanic-cell.svg)

*Figure 2 — Two dissimilar metals in saltwater make a cell. Zinc corrodes as the anode; copper is the cathode and is protected.*

This is Session 1's fruit battery with the fruit removed and the chemistry made explicit — and this time we predict the answer before we measure it.

### B1 — Predict first (5 min, before touching any equipment)

Standard reduction potentials, in volts, versus the standard hydrogen electrode:

| Half-reaction | E° (V) |
|---------------|--------|
| Mg²⁺ + 2e⁻ → Mg | −2.37 |
| Al³⁺ + 3e⁻ → Al | −1.66 |
| Zn²⁺ + 2e⁻ → Zn | −0.76 |
| Fe²⁺ + 2e⁻ → Fe | −0.44 |
| 2H⁺ + 2e⁻ → H₂ | 0.00 |
| Cu²⁺ + 2e⁻ → Cu | +0.34 |
| Ag⁺ + e⁻ → Ag | +0.80 |

**The rule:** the metal with the **more negative** value is the one that corrodes. It is the anode.

```
Predicted cell voltage = E°(cathode metal) − E°(anode metal)
```

Fill in the predictions column **before** you get a multimeter.

### B2 — Measure the voltage

1. Pour ~50–100 mL of **5–10% saltwater** into a small jar.
2. Sand both metal strips lightly if they are dull or oxidized. Aluminium especially — it carries an invisible oxide film that will change your answer.
3. Immerse both metals to a similar depth, **not touching each other** in the solution.
4. Multimeter on DC volts. Touch one probe to each metal.
5. If the reading is negative, **swap the probes and note it** — the metal now on the red probe is the cathode, and the other one is corroding.
6. Wipe the electrodes between trials.

### B3 — Measure the current (this is the new part)

Open-circuit voltage tells you *whether* corrosion is favoured. It says nothing about *how fast*. For that you need current.

7. Switch the meter to **DC mA** and connect it **directly between the two metals**, so it completes the circuit.
8. The reading falls quickly at first as the surfaces polarize. Take the value after about 30 seconds and note that it is drifting.

**That current is the corrosion rate, in electrons per second.** It is the same Faraday's law from Sessions 3 and 4, pointed at a reaction nobody wanted.

### Data table

| Metal 1 | Metal 2 | **Predicted V** | Measured V | Which metal is (+)? | Anode (corrodes) | Short-circuit I (mA) |
|---------|---------|-----------------|------------|---------------------|------------------|----------------------|
| Zn | Cu | +1.10 | | | | |
| Fe | Cu | +0.78 | | | | |
| Al | Cu | +2.00 | | | | |
| Zn | Fe | +0.32 | | | | |
| Mg | Cu | +2.71 | | | | |

### B4 — Turn the current into a corrosion rate

For zinc, which needs 2 electrons per atom (M = 65.4 g/mol):

```
mass lost per second = I × 65.4 / (2 × 96,485)
```

Useful benchmark, worth putting on the board:

> **A steady 1 mA eats about 11 grams of zinc per year.**

| Quantity | Your value |
|----------|------------|
| Short-circuit current, Zn–Cu | ______ mA |
| Zinc consumed per hour | ______ g |
| Zinc consumed per year at this rate | ______ g |
| A 500 g sacrificial anode would last | ______ years |

That last line is real engineering. Sizing the zinc block on a ship's hull is exactly this calculation, run with a current measured on the actual structure.

### What you will find, and why it is interesting

**Your measured voltages will be lower than your predictions — sometimes much lower.** This is not sloppy work. Three reasons, and each is worth naming:

| Reason | What it does |
|--------|--------------|
| The E° table assumes 1 M metal-ion solutions at 25 °C. Our saltwater contains essentially **no** Zn²⁺ or Cu²⁺ to start with | Shifts every potential |
| The reaction actually happening at the copper is **oxygen reduction**, not Cu²⁺ → Cu. The table's copper line is the wrong half-reaction for this cell | The largest single reason |
| Aluminium carries a tough passive oxide film that stops it behaving like bare aluminium at all | Al almost always underperforms badly — often below iron |

**Aluminium is the star of this section.** It is predicted to be violently reactive, second only to magnesium, and it will probably read lower than iron. That gap is the whole reason aircraft and window frames are made of it. Ask the class to explain it before you do.

---

## Part C — Corrosion jars (55–68 min)

![Corrosion comparison jars](../../assets/figures/session5-corrosion-jars.svg)

*Figure 3 — Jar B: iron rusts faster when coupled to copper. Jar C: zinc protects the iron by corroding instead.*

### The jars (started Session 1 — see [shared/multi-day-setup.md](../../shared/multi-day-setup.md))

Same 5–10% saltwater in each, about 100–150 mL, and each jar only **half full** so the metals sit at the waterline where oxygen is plentiful.

| Jar | Contents | Expected after four days |
|-----|----------|--------------------------|
| A | Iron nail alone | Moderate, even rust |
| B | Iron **in firm contact with copper** | **Noticeably worse** rust on the iron |
| C | Iron **in firm contact with zinc** (or a galvanized nail) | Iron largely clean; the zinc dulls and powders |

**Contact is not optional.** The metals must physically touch or be clipped together, or there is no electron path and no couple. A jar where the wire has slipped shows nothing, and it is the most common way this demo fails.

### Today's task

1. Line up A, B and C. Look at the **iron** in each, not the jar as a whole.
2. Note where the rust concentrates: at the waterline, and near the contact point.
3. Rank the three jars by how badly the iron has corroded.
4. Explain the ranking using your Part B data — you have just measured the voltages that drive exactly these couples.

### Observation sheet

| Jar | Iron appearance | Partner metal appearance | Which metal corroded? | Matching pair from Part B |
|-----|-----------------|--------------------------|-----------------------|---------------------------|
| A | | — | | — |
| B | | Cu | | Fe–Cu, ______ V |
| C | | Zn | | Zn–Fe, ______ V |

### The question to end on

*Jar A had no partner metal at all. So why did it rust?*

Because a single piece of iron is **already** a collection of tiny cells: impurities, stressed regions, and scratches are slightly anodic, and areas with better oxygen access are cathodic. A bent nail rusts fastest at the bend for exactly this reason. You do not need two metals to corrode — two metals just make it worse and make it predictable.

---

## Part D — The whole week on one table (68–78 min)

Students fill this in from memory, in groups, then compare.

| | Fruit battery | Copper plating | Silver plating | Water electrolysis | Rust in jar B | Derusting |
|--|---------------|----------------|----------------|--------------------|---------------|-----------|
| Session | 1 | 2 | 3 | 4 | 5 | 5 |
| Needs external power? | | | | | | |
| Produces electricity? | | | | | | |
| Spontaneous or driven? | | | | | | |
| What is oxidized? | | | | | | |
| What is reduced? | | | | | | |
| Metal moved? | | | | | | |
| Gas produced? | | | | | | |
| Useful or unwanted? | | | | | | |

### Answer key (instructor)

| | Fruit battery | Copper plating | Silver plating | Electrolysis | Rust (jar B) | Derusting |
|--|---------------|----------------|----------------|--------------|--------------|-----------|
| Needs external power? | No | Yes | Yes | Yes | No | Yes |
| Produces electricity? | Yes | No | No | No | Yes* | No |
| Spontaneous or driven? | Spontaneous | Driven | Driven | Driven | Spontaneous | Driven |
| Oxidized | Zn | Cu anode | Water at the graphite anode | Water → O₂ | Fe | Anode metal |
| Reduced | H⁺ / O₂ at Cu | Cu²⁺ → Cu | Ag⁺ → Ag | Water → H₂ | O₂ → OH⁻ | Iron oxide, and H⁺ → H₂ |
| Metal moved? | No | Yes | Yes | No | Yes, into solution | Yes, off the surface |
| Gas produced? | Trace | Little | Little | **Yes, both** | No | Yes, H₂ |
| Useful or unwanted? | Useful | Useful | Useful | Useful | **Unwanted** | Useful |

\* Jar B genuinely generates electricity — that is precisely the problem. Corrosion is a battery discharging itself for free, using your bridge as the anode.

**The single sentence the week has been building toward:** every one of these is the same process. Electrons leave something and arrive somewhere else. The only questions are which direction, and whether we are paying for it or paying to stop it.

---

## Safety

- Saltwater corrosion demos: wash hands afterwards; gloves optional
- Keep saltwater **physically apart** from the derusting jars and from anything left over from Session 4
- Derusting: washing soda or baking soda only — **never NaCl**
- Disconnect powered cells before touching electrodes, and whenever the room is unsupervised
- Rusty hardware is sharp and often tetanus-relevant. Forceps or gloves, and no bare-handed scrubbing
- No open flames near any gas-evolving setup

---

## Experiment status

- [ ] Derusting cells still powered this morning; before photos located
- [ ] Control nail present and clearly labeled
- [ ] Saltwater mixed and labeled for corrosion use only
- [ ] Corrosion jars available, contacts verified intact
- [ ] Metal strips sanded and labeled
- [ ] E° prediction table printed with the predictions column **blank**
- [ ] Capstone worksheets printed
