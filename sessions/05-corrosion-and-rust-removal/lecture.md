# Session 5 — Lecture Notes: Corrosion, Galvanic Couples, and Reversing Rust

**Audience:** instructors / TAs — use this as your teaching script.
**Students** see the talking points, do the Part B predictions, and finish with the §5 capstone.

> Deep-dive chemistry, potentials, coaching traps: [instructor.md](instructor.md).
> Bench procedure: [experiment.md](experiment.md).

---

## 1. Where the week has got to

This is the synthesis day. Do not treat §1 as revision for its own sake — every idea listed here is load-bearing in today's lab.

| Session | The idea we need today |
|---------|------------------------|
| 1 — Fruit battery | Two different metals in an electrolyte make a **spontaneous** cell with a measurable voltage |
| 2 — Copper plating | Electricity can **force** a reaction that would not happen on its own; polarity decides everything |
| 3 — Silver plating | **Q = It, n = Q/nF.** Current is a rate of chemistry, and we can count atoms with it |
| 4 — Electrolysis | A driven cell splits water; hydrogen appears at whatever we make negative |

**The framing sentence for the whole day:**

*"Day 1 we made a battery on purpose. Today we are going to find one we did not want — and it has been eating iron for as long as there has been iron."*

### What is new today

- The same galvanic cell from Day 1, but now it is a **problem** instead of a demonstration
- We **predict** a cell voltage from a table before measuring it — and then account for why the measurement falls short
- Current is reinterpreted one last time: in Session 3 it was a plating rate, in Session 4 a gas rate, and today it is a **corrosion rate in grams per year**
- Everything the week has covered collapses onto one axis: spontaneous, or driven

---

## 2. Class plan (90 min)

| Time | Block | What you do | Student product |
|------|-------|-------------|-----------------|
| 0–15 min | **Part A** — the reveal | Open the cells; nail, control, before-photo, side by side | Observation sheet |
| 15–30 min | Teach today's concepts | §3; activity series on the board | Notes / vocab |
| 30–55 min | **Part B** — predict, measure, measure again | Predictions **before** meters are handed out | Prediction vs measurement table + corrosion rate |
| 55–68 min | **Part C** — corrosion jars | Rank A/B/C; link to their own Part B voltages | Jar sheet |
| 68–78 min | **Part D** — week table | Groups fill from memory, then compare | Completed week table |
| 78–90 min | **Capstone** + closing | §5 | Capstone worksheet |

**Pacing tip:** the reveal is the best fifteen minutes of the week and it is tempting to let it run. Don't — Part B needs its full twenty-five minutes, because the predict-then-measure gap is where the real chemistry of the day lives.

---

## 3. Detailed explanations to give students

### 3.1 Open with the reveal, not with talking

Hold up the treated nail and the control together, and say nothing for a moment. Then:

*"Same nail, same solution, same jar, same night. The only difference is that one of them had wires on it. What did the electricity do?"*

Take answers before correcting any of them. Then park the question — you will come back to it in §3.5 — and go and build the corrosion story first, because derusting only makes sense once they know what rusting *is*.

### 3.2 Rust is not dirt

The idea to dislodge, and most students hold it: that rust is a substance that lands on iron, like dust.

```
Fe → Fe²⁺ + 2e⁻                  at anodic sites
O₂ + 2H₂O + 4e⁻ → 4OH⁻           at cathodic sites
```

Then Fe²⁺ is oxidized further and precipitates as hydrated iron oxides.

**Rust is the iron.** It is the same atoms, further along, having given up electrons. Nothing arrived — something left. This is why a rusted-through bolt has lost material, and why rust weighs *more* than the iron it came from, not less.

Note what the cathodic half-reaction requires: **oxygen and water, both**. Iron does not rust in dry air, and does not rust in oxygen-free water. Ask why a car rusts at the wheel arches and a bicycle rusts where the paint chipped.

### 3.3 The activity series, and what it is really telling you

```
Mg  >  Al  >  Zn  >  Fe  >  (H)  >  Cu  >  Ag  >  Au
←  more eager to give up electrons          less eager  →
```

| Metal | E° (V) | Where you meet it |
|-------|--------|-------------------|
| Mg | −2.37 | Sacrificial anodes in water heaters |
| Al | −1.66 | Everything — because of its oxide film, see §3.6 |
| Zn | −0.76 | Galvanizing; ship hull anodes |
| Fe | −0.44 | The metal we are trying to save |
| Cu | +0.34 | Plumbing, wiring — and a menace next to steel |
| Ag | +0.80 | Session 3 |

**The rule, and it is the only one they need to memorise:** put two of these in contact in an electrolyte, and the one **higher in the list corrodes**. The other is protected.

Then the payoff:

```
Predicted voltage = E°(protected metal) − E°(corroding metal)
```

This is Session 1's fruit battery with the mystery removed. The lemon was never the point; the two different metals were.

### 3.4 The two consequences, which are the same fact

**Galvanic corrosion — the bad case.** Iron touching copper in saltwater. Copper is nobler, so iron becomes the anode of a real cell and corrodes *faster than it would alone*. Jar B. This ruins real structures: a copper pipe threaded into a galvanized fitting, a steel bolt in an aluminium panel, a bronze propeller on a steel shaft.

**Sacrificial protection — the good case.** Iron touching zinc. Now zinc is the more active metal, so zinc becomes the anode and iron becomes the cathode. Jar C. The iron is protected not by being covered but by being **electrically fed** — which is why a scratch in galvanized steel does not start rusting, while a scratch in painted steel does.

Ask this and let them sit with it:

*"Session 3, we silver-plated a copper coin. Suppose that silver layer gets scratched. Which metal corrodes now?"*

The copper. It is more active than silver, so the base metal underneath becomes the anode — and worse, it is a **small anode wired to a large cathode**, so the attack concentrates into a pit. A noble coating protects only while it is perfect. A sacrificial coating protects even when it is not. That is the whole difference between chrome plating and galvanizing, and it lands hard on students who assumed plating is plating.

### 3.5 Now come back to the nail

Rusting made iron the anode. So to reverse it, **make the iron the cathode** — and since that is not what it wants to do, you have to pay for it with a power supply. Session 4's driven cell, pointed at rust.

| | Rusting in jar B | Derusting overnight |
|--|------------------|---------------------|
| Iron is the | **Anode** — oxidized | **Cathode** — reduced |
| Driven by | Difference in metal activity | External power supply |
| Direction | Spontaneous, free, unstoppable | Forced, costs energy |
| Electrolyte | Saltwater | Washing soda, **no chloride** |
| Partner metal | Copper survives | The anode is consumed |

**And the polarity is the entire experiment.** Reverse the clips and you dissolve the nail rather than clean it. Same wires, same solution, same battery — opposite outcome. Nothing else this week makes the point so cheaply.

Then be honest about the mechanism, because students will ask: the current does not turn rust back into shiny steel atom for atom. Some oxide is reduced; hydrogen bubbling at the surface mechanically lifts the rest; loose material falls into the bath as the sludge they can see. Metal already lost to rust is not coming back. Derusting saves what remains — it does not undo history.

### 3.6 Why the measurements will disagree with the table

Warn them **before** Part B, so the gap is a finding and not a disappointment.

1. **The table assumes 1 M solutions of each metal ion.** Our jar has essentially no Zn²⁺ or Cu²⁺ in it at all.
2. **The copper is not doing what the table says.** In an open jar of saltwater, the reaction at the copper is oxygen reduction — O₂ + 2H₂O + 4e⁻ → 4OH⁻ — not Cu²⁺ + 2e⁻ → Cu. We are reading the wrong line of the table, deliberately, because it still gets the *direction* right.
3. **Aluminium lies.** Predicted at −1.66 V it should be ferocious. It will probably read below iron, because it is wearing an oxide film only a few nanometres thick that is chemically tough and self-repairing.

That third one is worth dwelling on: aluminium is thermodynamically one of the most reactive metals in daily use, and we make drink cans and aeroplanes out of it. The table tells you what *wants* to happen. It never tells you how fast — and engineering lives in that gap.

### 3.7 Corrosion as a rate

Last use of Faraday's law this week, and the most sobering:

```
mass of zinc lost per second = I × 65.4 / (2 × 96,485)
```

**A steady 1 mA consumes about 11 grams of zinc per year.**

Measure the short-circuit current of the Zn–Cu jar and you have measured a corrosion rate. Scale it up and you have sized a ship's sacrificial anode. This is not an analogy for real engineering — it *is* the calculation real engineers do.

### 3.8 Safety (brief)

- Salt is allowed today, and today only, and only in the corrosion jars
- Disconnect before touching any powered cell
- Rusty hardware is sharp; forceps or gloves
- Wash hands after handling saltwater and metals

---

## 4. Quiz questions

Cold call or a 3-minute written check, before Part B. Answers in *italics*.

**Q1.** Rust weighs more than the iron it formed from. Why?
*The iron is still there, combined with oxygen and water. Nothing left; oxygen joined.*

**Q2.** Iron needs two things to rust. Name both.
*Water and oxygen. Remove either and rusting stops — which is why oiled tools and submerged-in-boiled-water samples survive.*

**Q3.** Zinc and iron are in contact in saltwater. Which corrodes, and how do you know?
*Zinc — it is more active, E° = −0.76 V versus −0.44 V for iron.*

**Q4.** Predict the voltage of a Zn–Cu cell from the table.
*0.34 − (−0.76) = +1.10 V.*

**Q5.** Your measured Zn–Cu voltage is 0.95 V, not 1.10 V. Has something gone wrong?
*No. The table's conditions (1 M ions, 25 °C) are not our conditions, and the copper electrode is actually reducing oxygen rather than copper ions.*

**Q6.** In the derusting cell, which terminal did the rusty nail go to, and why that one?
*Negative. It makes the iron the cathode, so it is reduced instead of oxidized.*

**Q7.** What would have happened had we connected the nail to positive?
*It would have become the anode and dissolved — accelerated corrosion, in a jar.*

**Q8.** Why washing soda and not salt in the derusting bath?
*Chloride would be oxidized at the anode to chlorine gas, and it drives pitting.*

**Q9.** Jar A has only one metal in it. Why does that nail rust at all?
*A single piece of iron already has anodic and cathodic regions — impurities, stress, scratches, and differences in oxygen access. Two metals only make it worse and more predictable.*

**Q10.** A galvanized bucket gets scratched down to the steel. Does it start rusting there?
*Not straight away. The surrounding zinc is still electrically connected and still more active, so it keeps protecting the exposed steel.*

---

## 5. Capstone challenge (78–90 min)

Print this. Groups of 2–3, then discuss as a class. Section C is the part worth the time.

### Section A — The week in one line each

1. Which session **made** electricity from chemistry?
2. Which sessions **spent** electricity to force chemistry?
3. Which session **moved metal atoms** from one place to another?
4. Which session **split a molecule**?
5. In every single experiment: where did the **electrons** travel, and where did the **ions** travel?

### Section B — Calculations

**B1.** Your Zn–Cu jar drew a short-circuit current of 4 mA. Using 1 mA ≈ 11 g of zinc per year, how much zinc would that couple consume in a year?

**B2.** A derusting cell ran overnight at 0.4 A for 12 hours.
&nbsp;&nbsp;(a) How much charge passed?
&nbsp;&nbsp;(b) How many moles of electrons is that?
&nbsp;&nbsp;(c) If all of that made hydrogen, what volume of H₂ was produced? (24.45 L/mol)
&nbsp;&nbsp;(d) Why does that answer make "keep the jar open and the room ventilated" a rule rather than a suggestion?

**B3.** A water electrolysis cell runs at 0.25 A for 8 minutes. How many mL of H₂ and of O₂? (Use ≈ 7.6 mL/min per amp of H₂.)

### Section C — Applied scenarios

**C1.** A boatyard fits **steel** screws into an **aluminium** hull. Six months later something is badly corroded. Which metal, and why? What would you do instead?

**C2.** A plumber joins a **copper** pipe directly to a **galvanized steel** pipe. Which side fails, and where exactly?

**C3.** A domestic water heater contains a **magnesium rod** that must be replaced every few years. What is it for, and what starts happening once it is fully consumed?

**C4.** A friend plans to derust an antique tool using **saltwater** because it is cheaper. Give them two specific reasons not to.

**C5.** A silver-plated copper spoon gets scratched through the silver. Which metal corrodes — and why is a scratch in silver plating more dangerous than a scratch in galvanizing?

**C6.** You are asked to protect a wrought-iron gate that stands outdoors for thirty years. Propose a strategy, name the electrochemistry behind each element of it, and say what maintenance it needs.

### Answer key

**Section A.** (1) Session 1, and jar B in Session 5 — corrosion is a battery discharging for free. (2) Sessions 2, 3, 4, and the derusting cell. (3) Sessions 2 and 3, and arguably corrosion, which moves iron into solution. (4) Session 4. (5) Electrons through the metal and wires; ions through the solution. Always both, always in a loop.

**B1.** 4 mA × 11 g/year per mA ≈ **44 g of zinc per year**.

**B2.** (a) Q = 0.4 × 43,200 = **17,280 C**. (b) 17,280 / 96,485 = **0.179 mol e⁻**. (c) 0.0895 mol H₂ × 24.45 L/mol ≈ **2.2 litres**. (d) Two litres of hydrogen accumulated overnight in a sealed container is an explosive hazard; in an open jar in a ventilated room it disperses harmlessly. The rule follows from the arithmetic.

**B3.** H₂: 7.6 × 0.25 × 8 = **15.2 mL**. O₂: half that, **7.6 mL**.

**C1.** The **aluminium hull** corrodes, and it concentrates around each screw. Aluminium is far more active than steel, so it becomes the anode — and a large anode area would be survivable, but here you have a large aluminium anode feeding small steel cathodes, so the damage spreads around every fastener. Fix: aluminium or compatible fasteners, insulating washers and sleeves, or a sealant that breaks the electrical path. Accept any answer that identifies aluminium as anodic and proposes breaking either the electron path or the electrolyte path.

**C2.** The **galvanized steel** side, right at the joint. Zinc goes first, then the steel underneath. Real plumbing codes require a dielectric union between copper and galvanized steel precisely for this. Credit for noting that the damage is worst *at* the junction, where the two metals and the water all meet.

**C3.** It is a **sacrificial anode**: magnesium is far more active than the steel tank, so it corrodes preferentially and keeps the tank cathodic. Once it is consumed the tank itself becomes the anode and starts to corrode from the inside — which is why the rod is cheap maintenance and the tank is an expensive failure.

**C4.** First, chloride is oxidized at the anode to **chlorine gas**, in a bucket, indoors. Second, chloride drives **pitting** — it breaks down passive films and attacks locally, so even where it does clean, it damages the surface it is meant to save. Washing soda costs almost nothing and does neither.

**C5.** The **copper** corrodes, because it is more active than silver. The danger is geometry: a scratch exposes a **tiny anode** connected to a **large cathode** of intact silver, so all the corrosion current concentrates into that one small spot and drills a pit. Galvanizing is the opposite arrangement — the coating itself is the anode, so a scratch is protected by the surrounding zinc instead of being attacked by it. A noble coating must be perfect to work; a sacrificial coating does not.

**C6.** Look for a **layered** answer rather than one silver bullet: a barrier (paint or powder coat) to keep water and oxygen off, ideally over a **galvanized** base so that any breach in the paint still has sacrificial protection underneath; attention to **crevices and joints**, where water sits and oxygen is scarce and corrosion concentrates; drainage so the base does not stand in a puddle; and inspection every few years, with touch-up before rust gets under the coating and lifts it. Strong answers mention that paint is *not* electrochemical — it works by denying the reaction its reactants — while galvanizing is, and that combining the two mechanisms is exactly why it is done that way in practice.

---

## 6. Closing

Put the week's six experiments on the board in one row, and draw a single arrow under all of them.

*"Every experiment this week was the same experiment. Electrons leaving something and arriving somewhere else. On Monday we let it happen and measured the voltage. On Tuesday and Wednesday we paid for it and got silver and copper where we wanted them. On Thursday we paid for it and pulled water apart. Today we found the same reaction running without permission, eating iron — and last night we paid to run it backwards.*

*The chemistry never changed. All that ever changed was who was paying."*

---

## 7. Vocabulary — full week review

- [ ] Oxidation / reduction
- [ ] Anode / cathode, and how the signs differ between galvanic and electrolytic cells
- [ ] Electrolyte; supporting electrolyte; spectator ion
- [ ] Galvanic cell vs electrolytic cell; spontaneous vs driven
- [ ] Activity series; standard reduction potential
- [ ] Faraday's constant; current efficiency
- [ ] Sacrificial anode; cathodic protection; passivation
- [ ] Energy carrier vs energy source

---

## 8. Materials you need in hand while teaching

- The treated nail, the control nail, and the printed before-photo
- Jars A, B and C, arranged where everyone can see them
- Activity series written large enough to stay on the board all session
- A galvanized nail and a plain iron nail, to pass around
- A photo of a ship's hull anode or a water-heater rod
- Printed E° prediction tables with the predictions column **blank**
- Printed capstone worksheets
