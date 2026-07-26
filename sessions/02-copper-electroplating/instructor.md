# Session 2 — Instructor Notes: Copper Electroplating Deep Dive

**Audience:** instructors and TAs only. Pair with [lecture.md](lecture.md) and [experiment.md](experiment.md).

---

## Why this session exists

Session 1 made electricity from chemistry. Session 2 **forces** chemistry with electricity: copper ions become solid metal on a student’s object. Visually dramatic, conceptually the reverse of a galvanic cell. Students must leave knowing: **cathode = reduction = object being plated**, and the power supply — not spontaneous chemistry — drives the process.

---

## Atomic / ionic picture of plating

### What Cu²⁺ is

Copper metal atoms have valence electrons that can be removed:

```
Cu(s) → Cu²⁺(aq) + 2e⁻   (oxidation / dissolution)
Cu²⁺(aq) + 2e⁻ → Cu(s)   (reduction / plating)
```

Cu²⁺ in water is typically a hydrated complex (often written Cu²⁺(aq) or [Cu(H₂O)₆]²⁺). The blue color of many copper solutions comes from these hydrated ions (and related species). Students only need: *blue liquid ≈ dissolved copper ions ready to plate.*

### Why two electrons matter

Each Cu²⁺ needs **two** electrons to become one Cu atom. Faraday’s law (Session 3) makes this quantitative; here it explains rate qualitatively:

- Higher current → more electrons per second → more Cu atoms deposited per second
- Too high current density → ions cannot arrive / arrange orderly → powdery, dark deposits

### Valence and periodic context

| Element | Common ion in this lab | Notes |
|---------|------------------------|-------|
| Cu | Cu²⁺ | Transition metal; d-electrons give colored solutions |
| Fe (nail) | Fe²⁺ / Fe³⁺ possible side products | Steel cathode is a **substrate**, not the ion being plated |
| H | H⁺ | Competing reduction → H₂ bubbles if overpotential / acidity allows |

Copper sits **below** hydrogen and iron in the activity series for many contexts — which is why Cu²⁺ is relatively easy to reduce onto steel. That is also why iron nails rust when left wet, but copper plating can stick if the surface is clean.

---

## Galvanic vs electrolytic — master the signs

| Feature | Session 1 galvanic | Session 2 electrolytic plating |
|---------|--------------------|--------------------------------|
| Energy direction | Chemical → electrical | Electrical → chemical |
| Spontaneous? | Yes | No |
| Anode | Zn oxidizes (− terminal) | Cu oxidizes (**+** of battery) |
| Cathode | H⁺ reduced (+ terminal) | Cu²⁺ reduced (**−** of battery) |
| Who supplies energy? | Chemical reactants | Battery / supply |

**Classroom one-liner:** *“Yesterday zinc wanted to give away electrons. Today we force copper ions to take electrons by connecting the object to the negative terminal.”*

---

## Half-reactions in the plating bath

### Preferred teaching set (copper anode)

**Cathode (−) — object:**

```
Cu²⁺(aq) + 2e⁻ → Cu(s)
```

**Anode (+) — copper metal:**

```
Cu(s) → Cu²⁺(aq) + 2e⁻
```

**Net:** copper is transferred from anode to cathode. Solution Cu²⁺ concentration stays roughly constant if the anode is copper (idealized).

### If the anode is *not* copper (graphite, steel)

Anode reaction may become water oxidation or anode metal dissolution:

```
2H₂O → O₂ + 4H⁺ + 4e⁻   (water oxidation, simplified)
```

Then Cu²⁺ in solution is **consumed** and not replenished — bath depletes, plating slows, quality suffers. Emphasize why a copper anode is preferred.

### Competing cathode reaction

```
2H⁺ + 2e⁻ → H₂(g)
```

Bubbles on the object mean some current is wasted on hydrogen instead of copper. Acidic baths and high current density increase this. Dark/powdery deposits often correlate with high current and side reactions.

---

## Electrochemical series connection

Approximate E° values:

| Couple | E° (V) |
|--------|--------|
| Cu²⁺/Cu | +0.34 |
| H⁺/H₂ | 0.00 |
| Fe²⁺/Fe | −0.44 |
| Zn²⁺/Zn | −0.76 |

Plating Cu onto Fe is thermodynamically reasonable: Cu²⁺ is a stronger oxidant than Fe²⁺ (Cu²⁺ more easily reduced). Students do not need the calculation; you can say: *“Copper ions are ‘eager’ to become metal compared with iron ions — so copper coats the nail when we supply electrons.”*

---

## Current density and deposit quality

**Current density** ≈ current / cathode area.

| Too low | Just right | Too high |
|---------|------------|----------|
| Very slow, thin coat | Smooth, adherent, coppery | Burnt, black, powdery, treeing |

**Instructor controls if groups struggle:**

- Series resistor (100–500 Ω) with 9 V pack
- Larger anode–cathode distance
- Shorter plating times (2–5 min first)
- Cleaner surface prep

### Why cleaning matters (surface chemistry)

Oils and oxides:

- Block electron transfer
- Prevent metallic bonding of new Cu atoms to the substrate
- Cause peeling or patchy color

Protocol: sand → rinse → handle by edges → plate immediately. Fingerprints are a real failure mode.

---

## Experiment coaching notes

### Homemade vinegar/salt copper solution

- Often weaker and less blue than CuSO₄.
- May contain mixed copper species; still plates if enough Cu²⁺ is present.
- Keep backup CuSO₄ for demos or failed jars.
- **Waste:** collect copper solutions; do not pour casually down drains.

### Wiring checklist (walk the room)

1. Object on **battery negative (−)**
2. Copper strip/wire on **battery positive (+)**
3. Electrodes not touching
4. Both immersed in solution
5. Optional ammeter in series

Students reverse polarity constantly. A reversed cell can etch the object or plate onto the “wrong” electrode.

### What good vs bad looks like

| Appearance | Interpretation |
|------------|----------------|
| Bright salmon/copper color | Good reduction, moderate current |
| Dark brown / black powder | Too much current; wipe/stop/reduce I |
| Patchy | Dirty surface or poor immersion |
| Bubbling heavily on object | Competing H₂ evolution |

### Variable tests (how to interpret group data)

- **Time:** thicker coat, then roughness if too long
- **Distance:** closer → higher current → faster but riskier
- **Resistor:** lower current → slower, often prettier
- **Surface prep:** dirty control looks obviously worse — best demo variable

---

## Misconceptions to preempt

| Misconception | Correction |
|---------------|------------|
| “The battery stores the copper.” | Battery supplies **electrons**; copper comes from ions / anode. |
| “Positive terminal plates the object.” | Object must be **negative** (cathode). |
| “Color in solution is paint.” | Color is from **dissolved Cu²⁺ ions**. |
| “More voltage always better.” | Excess driving force → burnt deposits. |

---

## Board plan

1. Draw Session 1 cell vs Session 2 cell side by side (energy arrows opposite).
2. Label anode/cathode signs for **electrolytic** case.
3. Write both half-reactions; circle “object = cathode.”
4. Show photo timeline: 0 / 2 / 5 min plating.
5. Bridge: next time we **count** atoms with Faraday’s law using silver.

---

## Optional enrichment

- Overpotential and why real plating baths use additives (levelers, brighteners).
- Hull cell concept for current-density mapping (advanced).
- Industrial electroplating: chrome, nickel, PCB copper deposition.
