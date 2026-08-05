# Session 4 — Lecture Notes: Water Electrolysis and Stoichiometry

**Audience:** instructors / TAs — use this as your teaching script.
**Students** get the talking points during class and complete the §5 prediction sheet before the U-tube.

> Deep-dive chemistry, overpotential, and coaching traps: [instructor.md](instructor.md).
> Bench procedure: [experiment.md](experiment.md).

---

## 1. Summary of concepts from prior days

Spend **5–8 minutes** here. Today leans on all three previous sessions.

### Session 1 — Fruit battery (galvanic cell)

| Idea | What to remind them |
|------|---------------------|
| Spontaneous chemistry | The reaction **made** electricity by itself |
| Electron vs ion path | Electrons in the wire, ions in the juice — **both** are needed |
| Weak electrolyte | Fruit juice conducted poorly, so the current was feeble |

### Session 2 — Copper electroplating (electrolytic cell)

| Idea | What to remind them |
|------|---------------------|
| Electrolysis | Electricity **forces** a reaction that would not happen on its own |
| Polarity flips | Object to plate goes to battery **(−)** = cathode = reduction |
| Active anode | The copper anode dissolved and resupplied Cu²⁺ |

### Session 3 — Silver plating and Faraday's law

| Idea | What to remind them |
|------|---------------------|
| Q = I × t | Charge is current multiplied by time |
| n_e = Q/F | F = 96,485 C per mole of electrons |
| Electrons per atom | Ag needed 1 e⁻; Cu needed 2. **The number matters** |
| Inert anode | Graphite did not dissolve and did not resupply Ag⁺ |
| Current efficiency | We *assumed* 100% and could not really check it |

**One-sentence bridge:** *"For three days the thing being changed was a metal. Today it is the water itself."*

### What is new today

- The substance being split is the **solvent**, not something dissolved in it
- The products are **gases**, which means for the first time we can **measure** how much we made
- Two products, with **different electron counts** — 2 e⁻ per H₂, 4 e⁻ per O₂ — so the amounts must come out in a fixed ratio
- The salt we add is **not consumed**. It is a supporting electrolyte, a new idea

**One-sentence goal:** *"Today we predict how much gas we will make before we make it — and then we check."*

---

## 2. Class plan (90 min)

| Time | Block | What you do | Student product |
|------|-------|-------------|-----------------|
| **−5 min** | **TA starts the balloon generator** | See [experiment.md](experiment.md) Part D | — |
| 0–8 min | Review + hook | §1 and §3.1; two rods in distilled water, nothing happens | Oral answers |
| 8–18 min | Teach today's concepts | §3.2–3.6; board flowchart | Notes / vocab |
| 18–26 min | Quiz check + pre-lab | §4 questions, then §5 prediction sheet | Completed prediction sheet |
| 26–36 min | **Part A** — conductivity ladder | Fixed voltage, three liquids | Ladder table filled |
| 36–50 min | **Part B** — measure I, predict volume | Faraday arithmetic with **their** current | Predicted mL of H₂ |
| 50–72 min | **Part C** — U-tube | Ratio **and** prediction check | Gas log + efficiency % |
| 72–82 min | **Part D** — splint tests, balloon | Instructor demo | Gas identifications |
| 82–90 min | **Part E** — start derusting | Polarity called out as a class | Cells running |

**Pacing tip:** the prediction sheet in §5 is the gate. A group that has not written down a predicted volume has nothing to compare their U-tube data with, and Part C collapses into watching bubbles.

---

## 3. Detailed explanations to give students

### 3.1 Hook (say this)

Hold up a beaker of distilled water with two graphite rods in it, already wired to the supply.

*"This is pure water. Water is H₂O — the hydrogen and oxygen are already in there, we are not making anything exotic. I have several volts across these two rods. Watch."*

Switch on. Nothing happens.

*"Nothing. So what is missing? The reactant is right there. The voltage is right there. What else does a chemical reaction driven by electricity need?"*

Take answers. Steer toward: **charge has to be able to get across the gap**, and in a liquid that means **ions have to move**.

### 3.2 Why pure water barely conducts (board)

Water does ionize, a little:

```
H₂O ⇌ H⁺ + OH⁻          [H⁺][OH⁻] = 1.0 × 10⁻¹⁴ at 25 °C
```

so [H⁺] = 10⁻⁷ M. Put that next to the concentration of water itself, 55.5 M:

**About one molecule in 550 million is ionized at any moment.**

That is the whole of Part A rung 1. There is no road for the charge.

Tap water is better — dissolved minerals give it real ions — but still hundreds of times worse than what we are about to make.

### 3.3 The supporting electrolyte — a genuinely new idea

Dissolve Na₂SO₄ and the solution fills with Na⁺ and SO₄²⁻. Current can now cross.

But here is the part worth slowing down for, because it is not obvious and students will get it wrong on a test:

**Neither Na⁺ nor SO₄²⁻ reacts.** Sodium is far too hard to reduce and sulfate is already fully oxidized. They ferry charge through the solution and are exactly as abundant at the end as at the start. **Water is still the only thing being split.**

Contrast with what they have already seen:

| Session | The dissolved salt | Its fate |
|---------|--------------------|----------|
| 2 | CuSO₄ | Cu²⁺ was **consumed** — it became the plating |
| 3 | AgNO₃ | Ag⁺ was **consumed** and slowly ran out |
| 4 | Na₂SO₄ | **Not consumed.** It only carries charge |

Ask: *"If the sulfate is not used up, could we run this cell forever?"* — until the water runs out, essentially yes. That is what an industrial electrolyzer does.

**Why not table salt:** chloride is easier to oxidize than water, so at the anode you would get **Cl₂ gas** instead of oxygen. This is not a rule for the sake of rules — it is a competing half-reaction, and it wins.

### 3.4 The two voltages

- **1.23 V** — the thermodynamic minimum. Below it, nothing, ever.
- **What you actually need** — usually **1.6–2.0 V** before you see anything, and more to go fast.

The gap is **overpotential**: an electrode surface can be thermodynamically willing and kinetically slow. Making an O₂ molecule requires assembling two oxygen atoms and breaking four O–H bonds on a surface that is not especially good at it, and that clumsiness costs voltage.

*"This is why the platinum in a fuel cell is worth its price — not because it changes the chemistry, but because it makes the same chemistry faster at lower voltage."*

### 3.5 Rate from current — Faraday, third time

Same law as Session 3, with the electron count changed:

```
Cathode (−):  2H₂O + 2e⁻ → H₂ + 2OH⁻        2 electrons per H₂
Anode (+):    2H₂O → O₂ + 4H⁺ + 4e⁻          4 electrons per O₂

ṅ(H₂) = I / (2F)          ṅ(O₂) = I / (4F)
```

**Say this clearly, it is the intellectual core of the day:** the same current passes through both electrodes — it has nowhere else to go. So the number of electrons arriving at one is the number leaving the other. If hydrogen costs 2 electrons and oxygen costs 4, then **twice as much hydrogen must appear.** The 2:1 ratio is not a coincidence of this experiment; it falls out of counting.

Then convert to something they can see:

```
V̇(H₂) in mL/min ≈ 7.6 × I        (I in amperes, room conditions)
```

**Board this:** *one amp ≈ 7.5 mL of hydrogen per minute.*

### 3.6 The flowchart (draw it)

```
I (A)
   → ṅ(H₂) = I/(2F)  mol/s
   → × 24,450 mL/mol → mL/s
   → × 60 → mL/min
   → × t → PREDICTED VOLUME
                              ↓
                    compare with the U-tube
                              ↓
              measured ÷ predicted = current efficiency
```

That last box is what Session 3 could not do. Silver film was too thin to weigh; gas is easy to measure.

### 3.7 How the U-tube works (show the apparatus while you say this)

Point at the physical parts:

| Part | Role |
|------|------|
| Stopper + graphite rod | Seals the top of each limb; gas collects underneath |
| The dome under the stopper | Where the gas accumulates |
| The side arm | The **vent**. Displaced liquid rises into it |
| Both limbs, same bore | So centimetres of column can be compared directly |

**The one instruction that decides success:** *fill until the liquid stands part-way up both side arms.* Fill below them and the gas escapes out of the side arm, and the apparatus looks like it is working while collecting nothing.

### 3.8 Set expectations before they measure

Tell them **in advance** that the ratio will probably come out a little **above** 2, and why:

- Oxygen is about twice as soluble in water as hydrogen, so some of it quietly dissolves
- The graphite anode is slowly eaten, and some oxygen leaves as CO₂, which is very soluble indeed
- Oxygen evolution is slower to get going

Announcing this beforehand converts "our experiment was wrong" into "we predicted the direction of our own error." **A ratio below 2 is the one that means something is broken** — almost always a leak on the hydrogen side.

### 3.9 Safety (brief and firm)

- No table salt in any bath in this room today. Chloride makes chlorine
- Ammeter in series, never across the supply
- The U-tube is **never** sealed — side arms stay open
- Flame is instructor-only, and the balloon is untied only when it is well away from every cell that is still making hydrogen

---

## 4. Quiz questions (before the lab)

Cold call, pair-share, or a 3-minute written check. Answers in *italics*.

### A. Review from Days 1–3

**Q1.** In Session 3, what did Q = I × t give us, and what did we divide it by to get moles of electrons?
*Q was total charge in coulombs; divide by F = 96,485 C/mol.*

**Q2.** Silver needed one electron per atom, copper needed two. Same charge through both cells — which gives more moles of metal?
*Silver. Each atom is cheaper in electrons.*

**Q3.** Why was the graphite anode in Session 3 called "inert"?
*It did not dissolve, so it did not resupply Ag⁺ to the bath.*

### B. Today's concepts

**Q4.** Pure water is 55.5 M in H₂O but only 10⁻⁷ M in H⁺. Roughly what fraction of molecules is ionized?
*About one in 550 million — which is why it barely conducts.*

**Q5.** We add Na₂SO₄. Which of Na⁺, SO₄²⁻, or H₂O gets split?
*Water. The sulfate is a spectator that only carries charge — it is there at the end, unchanged.*

**Q6.** So why bother adding it?
*Without mobile ions, charge cannot cross the solution and no current flows, so no reaction happens at either electrode.*

**Q7.** Why is table salt forbidden here?
*Chloride is oxidized more easily than water, so the anode would make Cl₂ gas instead of O₂.*

**Q8.** Write both half-reactions and say how many electrons each gas costs.
*2H₂O + 2e⁻ → H₂ + 2OH⁻ (2 e⁻ per H₂); 2H₂O → O₂ + 4H⁺ + 4e⁻ (4 e⁻ per O₂).*

**Q9.** The same current flows through both electrodes. Explain in one sentence why that forces a 2:1 volume ratio.
*Equal electrons at both electrodes, but hydrogen costs half as many per molecule, so twice as many H₂ molecules form — and equal numbers of gas molecules occupy equal volumes.*

**Q10.** A cell runs at 0.40 A. How many mL of H₂ per minute, roughly?
*7.6 × 0.40 ≈ 3.0 mL/min.*

**Q11.** Water needs 1.23 V. Your supply is set to 4 V. Is the extra 2.8 V wasted?
*Largely yes — it pays for overpotential and solution resistance, and ends up as heat. It buys speed, not extra product per coulomb.*

### C. Stretch

**Q12.** Your U-tube gives V(H₂)/V(O₂) = 2.4. Is the experiment wrong?
*No — and the direction is predictable. O₂ is more soluble, and graphite anodes lose some oxygen as CO₂. A ratio below 2 would be the worrying one, because it usually means the hydrogen side is leaking.*

**Q13.** You collect 82% of your predicted hydrogen. Where did the other 18% go?
*Dissolved in solution, leaked past a stopper, or lost to side reactions on the graphite. This is exactly the current efficiency we had to assume was 100% in Session 3.*

---

## 5. Interactive activity + prediction sheet (required before Part C)

### Activity name: "Predict the gas"

**Format:** pairs or groups of 3–4. **10–15 minutes.**
**Goal:** every group writes down a **number in millilitres** before they collect anything — the direct sequel to Session 3's "Predict before you plate," except this time the prediction is checkable.

### Part 1 — Station card

| Parameter | Value |
|-----------|-------|
| Planned current I | **0.30 A** (300 mA) |
| Planned collection time t | **600 s** (10 min) |
| Gas of interest | H₂ at the cathode (−) |
| U-tube internal diameter | **2.0 cm** |

### Part 2 — Live prompts

1. **Unit police (1 min).** Hold up a meter reading "300" on the mA range. *"What number goes into the formula?"* Chorus: **0.300 A**. Every year, someone divides by 2F using 300.

2. **The two-for-one (2 min).** *"Same current at both electrodes. Hydrogen costs 2 electrons, oxygen costs 4. Which side fills faster, and by exactly how much?"* Push until someone says it without hedging: **hydrogen, exactly twice**.

3. **Human flowchart (3 min).** Four volunteers hold signs: `I` → `ṅ = I/2F` → `mL/min` → `mL in 10 min`. The class shouts what connects each pair.

4. **Order-of-magnitude bet (1 min).** Before any arithmetic: *"Will 10 minutes at 300 mA give us a teaspoon, a soda can, or a bathtub?"* Let them commit out loud. Then calculate. A teaspoon is 5 mL and the answer is about 23 mL — most classes badly overestimate, which is exactly the useful surprise.

### Part 3 — Prediction sheet

Groups complete this before touching the U-tube. A TA initials one line per group.

**Constants:** F = 96,485 C/mol e⁻; molar volume ≈ 24,450 mL/mol at 25 °C

| Step | Formula | Work | Answer + unit |
|------|---------|------|---------------|
| 1. Current in amperes | mA ÷ 1000 | | ______ A |
| 2. Mole rate of H₂ | I / (2F) | | ______ mol/s |
| 3. Mole rate of O₂ | I / (4F) | | ______ mol/s |
| 4. Check | rate H₂ ÷ rate O₂ | | should be **2** |
| 5. H₂ volume rate | step 2 × 24,450 × 60 | | ______ mL/min |
| 6. **H₂ in 10 min** | step 5 × 10 | | ______ mL |
| 7. **O₂ in 10 min** | step 6 ÷ 2 | | ______ mL |
| 8. Column height of H₂ | step 6 ÷ 3.14 mL/cm | | ______ cm |

**Target answers for the card above (for you):**

| Step | Result |
|------|--------|
| I | **0.300 A** |
| ṅ(H₂) | 0.300 / 192,970 ≈ **1.55 × 10⁻⁶ mol/s** |
| ṅ(O₂) | ≈ **7.77 × 10⁻⁷ mol/s** |
| Ratio check | **2.00** |
| H₂ rate | ≈ **2.28 mL/min** |
| **H₂ in 10 min** | ≈ **22.8 mL** |
| **O₂ in 10 min** | ≈ **11.4 mL** |
| H₂ column in a 2.0 cm tube | ≈ **7.3 cm** |

**Sense-check to say:** *"About 23 mL — five teaspoons — after ten minutes. Splitting water is not hard, but it is slow. Remember that number when you read about hydrogen cars: an industrial electrolyzer is not doing anything cleverer than this, it is just doing it thousands of amps at a time."*

### Part 4 — Prediction statement (1 min)

Each group writes one sentence:

> "Running at about ______ A for ______ minutes, we expect ______ mL of hydrogen and ______ mL of oxygen, a ratio of 2:1."

After the run they recalculate with their **actual** current and time, and divide measured by predicted to get their current efficiency.

### Gate before the U-tube

- [ ] Prediction sheet complete, ratio check equals 2
- [ ] TA has initialled the predicted volume
- [ ] Group can point to: cathode (−) = H₂ limb, anode (+) = O₂ limb, ammeter in series
- [ ] Group can state the fill rule: **liquid part-way up both side arms**
- [ ] Goggles on

---

## 6. During and after the experiment — what to emphasize

1. Make them **name the fast limb before reading the wires**. If the fast limb is not on (−), the leads are swapped and everything downstream is backwards.
2. The 2–3 minute pre-saturation run before t = 0 is not optional. Groups that skip it get the worst ratios and blame the apparatus.
3. When a group reports 2.3, resist calling it error. Ask: *"Which of our three reasons would push it that way?"*
4. When a group reports 1.4, treat it as a fault to find: leaking stopper, or gas venting out of the side arm.
5. Debrief questions:
   - Did the sulfate get used up? How do you know?
   - What was your current efficiency, and where did the missing gas go?
   - Session 3 assumed 100% efficiency. Was that assumption safe?
   - Where did the energy in the balloon pop come from?

---

## 7. Bridge to Session 5

*"Today electricity forced water apart — a reaction that would never happen on its own. Tomorrow we look at the opposite: a reaction that happens whether we want it or not. Iron rusting. And then, with the cells we are starting in the next ten minutes, we will have spent a night forcing that one backwards."*

Start the derusting cells per [experiment.md](experiment.md) Part E, and make the whole class say the polarity out loud: **rusty iron on negative.**

---

## 8. Vocabulary checklist

- [ ] Electrolysis
- [ ] Supporting electrolyte (vs a reactant salt)
- [ ] Spectator ion
- [ ] Overpotential
- [ ] Current efficiency
- [ ] Molar volume of a gas
- [ ] Stoichiometry — as a volume ratio and as an electron count
- [ ] Energy carrier vs energy source

---

## 9. Materials you need in hand while teaching

- Beaker of **distilled** water with two graphite rods, pre-wired, for the opening hook
- The three ladder beakers, labeled
- A meter showing mA, for the unit-police moment
- Board space for the flowchart
- Printed prediction sheets (§5 Part 3)
- The U-tube, filled correctly, to point at while explaining §3.7
- Splints, and the balloon generator that has been running since before class
