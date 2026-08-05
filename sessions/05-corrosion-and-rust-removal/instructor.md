# Session 5 — Instructor Notes: Corrosion and Rust Removal Deep Dive

**Audience:** instructors and TAs only. Pair with [lecture.md](lecture.md) and [experiment.md](experiment.md).

---

## Why this session exists

Four days of controlled electrochemistry, all of it something we did on purpose. Today the same chemistry turns up **uninvited**, doing billions of dollars of damage a year, and the students discover they already have every tool needed to explain it and to fight it.

Your job is to make **activity series**, **galvanic couples**, and **driven versus spontaneous** land as one idea rather than three demos. The organising question for the whole session: *is this reaction happening because it wants to, or because somebody is paying for it?*

---

## The reveal — protect it, then get out of it

The overnight cells are the strongest visual of the week. Two things make or break it:

**The control.** A rusty nail sitting in alkaline solution overnight changes appearance all by itself. Without the unpowered control in the same solution, you have shown the students a nail that looks different from a photo, and a sharp student will say so. With the control, you have an experiment.

**Disconnecting first.** Every time, before any hand goes near the jar. Make it visible and make it ritual — a TA disconnects, then the nail comes out.

Expect this to want to run long. Cap it at fifteen minutes. Part B is where the chemistry of the day actually lives.

### What "cleaning" means, honestly

Be straightforward, because the students will push:

- Some iron oxide at the surface is genuinely electrochemically reduced.
- A great deal of the visible effect is **mechanical**: hydrogen evolving at the surface undermines and lifts loosely adherent oxide, which falls into the bath as the sludge everyone can see.
- Metal already lost to rust is gone. Derusting recovers the surface, not the missing steel.
- The nail comes out grey-black and needs brushing and drying. It is also now bare, active steel with no oxide layer at all, so it will flash-rust within hours if left wet. That is a genuinely satisfying detail to end on — you cleaned it so thoroughly that it is now more vulnerable than when you started.

---

## Corrosion chemistry you should own

### Rust, properly

```
Fe → Fe²⁺ + 2e⁻                       anodic dissolution
O₂ + 2H₂O + 4e⁻ → 4OH⁻                cathodic oxygen reduction, neutral water
```

Fe²⁺ oxidizes further and precipitates as hydrated oxides and oxyhydroxides — the FeOOH / Fe₂O₃·nH₂O family. The exact mineralogy is genuinely complicated and depends on chloride, pH and oxygen; do not go there with this age group. What they need is: **rust is oxidized iron, not a deposit that landed on iron.**

Note the cathodic step needs **both** water and oxygen. This explains: oiled tools survive, fully submerged deoxygenated iron survives, and the waterline of a jar is the worst place of all because it has generous access to both.

### Why a lone nail rusts (jar A)

Local cells on a single piece of metal, arising from impurities and grain boundaries, cold-worked or stressed regions (a bent nail rusts at the bend), and above all **differential aeration** — a region with poorer oxygen access becomes anodic relative to one with better access. This is why rust starts under washers, inside crevices, and beneath a lifting paint edge, which are exactly the places that look most protected.

Differential aeration is counter-intuitive and worth thirty seconds: the sheltered spot corrodes *because* it is sheltered.

### The reference table

Standard reduction potentials, acidic, versus SHE:

| Half-reaction | E° (V) | Note for teaching |
|---------------|--------|-------------------|
| Mg²⁺ + 2e⁻ → Mg | −2.37 | Water heater rods |
| Al³⁺ + 3e⁻ → Al | −1.66 | Thermodynamically wild, kinetically tame |
| Zn²⁺ + 2e⁻ → Zn | −0.76 | Galvanizing, hull anodes |
| Fe²⁺ + 2e⁻ → Fe | −0.44 | The metal at risk |
| 2H⁺ + 2e⁻ → H₂ | 0.00 | Reference |
| Cu²⁺ + 2e⁻ → Cu | +0.34 | Noble relative to iron |
| Ag⁺ + e⁻ → Ag | +0.80 | Session 3 |
| O₂ + 4H⁺ + 4e⁻ → 2H₂O | +1.23 | **The real cathodic reaction in wet corrosion** |

That last row is the one instructors most often skip and most need. In an open jar, the copper electrode is not reducing Cu²⁺ — there is barely any Cu²⁺ present. It is a surface on which **dissolved oxygen** is reduced. The Cu²⁺/Cu line still predicts the right *direction* for the couple, which is why we use it, but it is not the reaction taking place, and it is a large part of why measured voltages disagree with predictions.

---

## Part B coaching — the predict-then-measure gap

**Collect the predictions before you hand out a single multimeter.** The pedagogical value is entirely in the commitment.

Expected behaviour:

| Pair | Predicted | Typically measured | Comment |
|------|-----------|--------------------|---------|
| Zn–Cu | +1.10 V | 0.9–1.1 V | The well-behaved one |
| Fe–Cu | +0.78 V | 0.4–0.7 V | Reasonable |
| Zn–Fe | +0.32 V | 0.2–0.4 V | Small but correctly signed |
| Mg–Cu | +2.71 V | 1.4–1.7 V | Large shortfall; Mg also reacts directly with water |
| **Al–Cu** | **+2.00 V** | **0.3–0.9 V, erratic** | **The teaching moment** |

Three reasons for the shortfall, in order of size:

1. **Wrong half-reaction at the cathode.** Oxygen reduction, not metal deposition. What students measure is a **mixed potential** — the compromise where the anodic and cathodic rates match — not a thermodynamic cell potential.
2. **Not standard conditions.** No 1 M metal ions anywhere; Nernst shifts everything.
3. **Surface films.** Passive oxides, corrosion product build-up, and area ratios.

Do not grade on closeness to E°. Grade on whether they got the **direction** right — which metal corrodes — and whether they can name a reason for the gap.

### Aluminium is the lesson, not the outlier

Al is predicted second only to Mg and will usually read below iron. It carries a passive Al₂O₃ film a few nanometres thick that is adherent, insulating and self-repairing. This is why we build aircraft and window frames from a metal that is thermodynamically eager to burn.

Push the class to the general principle: **the table tells you what wants to happen, never how fast.** Everything students will meet later in kinetics, catalysis, and materials engineering lives in that gap. It is also the same distinction they met yesterday as overpotential — the same idea, wearing different clothes.

If someone sands the aluminium hard and immediately immerses it, they may briefly see a much larger voltage that then decays as the film reforms. That is worth stopping the room for.

### The short-circuit current — do not skip it

Open-circuit voltage says whether corrosion is favoured. Current says how fast. This is the step that turns Day 5 from qualitative into a real measurement, and it reuses Faraday's law for the third time in three days.

```
mass rate of Zn loss = I × 65.4 / (2F)          1 mA ≈ 11 g of zinc per year
```

The reading decays over the first half-minute as the electrodes polarize. That decay is itself informative — corrosion current depends on how easily the cathodic reaction can be supplied with oxygen, which is why stirring or aerating speeds it up. Take a value at ~30 s and note that it is not stable.

Sizing a ship's anode is exactly this calculation performed on a hull. Say so.

---

## Corrosion jars — narrative and failure modes

| Jar | Setup | What they should see | Story |
|-----|-------|----------------------|-------|
| A | Fe alone | Moderate, even rust | Local cells on one metal |
| B | Fe + Cu in firm contact | **Worse** rust on the iron | Galvanic couple: Fe anode, Cu cathode |
| C | Fe + Zn in firm contact | Iron clean; zinc dull and powdery | Sacrificial protection |

**Failure mode, and it is the common one:** the contact slips. No electron path, no couple, no difference between B and A. Wire the metals together tightly and check them on the day you set them up and again mid-week. A jar B that looks like jar A is not a subtle result, it is a disconnected circuit.

Second failure mode: jars filled to the brim. Fill them **half full** so the metals cross the waterline, where oxygen supply is best and the effect is most visible.

Have a photograph of a properly developed set of jars available as a backup. If this year's jars underperform, showing what they should look like and explaining why yours did not is a perfectly good lesson — and considerably better than pretending.

### Chloride's role

Saltwater is the right choice here: it supplies ions, and chloride actively breaks down passive films, which is why marine environments are so aggressive and why road salt destroys cars. It is also exactly why chloride is banned from the derusting bath and from Session 4. Same property, opposite desirability. Making that explicit stops "no salt" sounding like an arbitrary safety rule.

---

## Electrolytic derusting — the polarity point

| Piece | Terminal | Role |
|-------|----------|------|
| Rusty object | **−** cathode | Reduced, cleaned |
| Sacrificial steel or graphite | **+** anode | Oxidized, consumed, sludges |
| Electrolyte | Washing soda (or baking soda) | Alkaline, **no chloride** |

Reversing the clips dissolves the workpiece. This is the cheapest, sharpest demonstration of the week's central idea and it costs nothing to state: same jar, same battery, same solution, opposite outcome, decided entirely by which wire went where.

Graphite anodes shed carbon and blacken the bath. Steel anodes produce more sludge but are cheaper and more robust. Stainless steel is sometimes suggested online and should be avoided — it can release chromium compounds into the bath.

### Overnight practicalities

- **Not a 9 V alkaline.** ~500 mAh against a cell drawing a few hundred mA is roughly two hours. Use a mains supply or a 5 V USB brick. This is the most common reason a Session 5 reveal disappoints.
- **Hydrogen all night.** Jars open, room ventilated, no ignition sources. A capstone question (§5 B2) has students calculate that an overnight cell can generate a couple of litres of H₂ — worth doing, because it converts the rule into arithmetic.
- Secure the wiring so nothing can tip or short.

---

## Misconceptions

| Misconception | Correction |
|---------------|------------|
| "Rust is a coating that lands on iron." | Rust **is** the iron, oxidized. Nothing arrived; electrons left. |
| "Copper attacks iron chemically on contact." | Copper does nothing. It provides a cathode surface, and the iron becomes the anode of a real cell. |
| "Zinc protects steel by sealing it." | It does seal, but it also **sacrifices**. That is why a scratch in galvanizing does not rust and a scratch in paint does. |
| "Any coating protects. Plating is plating." | A noble coating (silver, chrome) must be perfect — a breach makes a small anode under a large cathode and pits fast. A sacrificial coating protects through the breach. |
| "The measured voltage should match the table." | It should not. Non-standard conditions, oxygen reduction at the cathode, and surface films. The direction is what the table gets right. |
| "Aluminium is unreactive." | It is one of the most reactive metals in use. Its oxide film is what is unreactive. |
| "Derusting turns rust back into steel." | Some oxide is reduced; much is mechanically lifted by hydrogen. Lost metal is lost. |
| "Salt is the best electrolyte." | Best for corrosion demos, forbidden for anything driven — chlorine and pitting. |
| "Stainless steel can't corrode." | Its passive Cr₂O₃ film can be broken by chloride, and it pits in crevices. |

---

## Board plan

1. Treated nail vs control, held up. Say nothing for a beat.
2. `Fe → Fe²⁺ + 2e⁻` and `O₂ + 2H₂O + 4e⁻ → 4OH⁻`. Write "rust IS the iron."
3. Activity series, left to right, large. Leave it up all session.
4. Jars A / B / C sketched, with the anode labelled in each.
5. Two-column table: rusting (spontaneous, Fe = anode) vs derusting (driven, Fe = cathode).
6. `1 mA ≈ 11 g Zn per year`, circled.
7. The six experiments in a row, one arrow under all of them, for the closing.

---

## Optional enrichment

- **Crevice corrosion and differential aeration** — why bolted joints and washers fail first.
- **Stainless steel passivation** — Cr₂O₃, and why "stainless" fails in seawater and in crevices.
- **Impressed-current cathodic protection** — pipelines and jetties; the industrial version of the derusting cell.
- **Pourbaix diagrams for iron** — for a TA or a strong student who wants to know why pH matters.
- **Ferroxyl indicator** (potassium hexacyanoferrate(III) plus phenolphthalein), if you can get it for next year. It stains anodic sites blue and cathodic sites pink within **minutes**, on a bent nail or a Fe–Cu couple, and would let this session show corrosion happening live instead of relying on jars started days earlier. It is a standard school reagent; the rules are never to acidify it and never to heat it. This is the single best upgrade available to Session 5.
