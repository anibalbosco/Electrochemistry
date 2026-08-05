# Session 3 — Lecture Notes: Silver Plating & Faraday's Law

**Audience:** instructors / TAs — use this as your teaching script.
**Students** see the shorter talking points during class; they do the worksheet in §5 before plating.

> Deep-dive chemistry, bath design, and coaching traps: [instructor.md](instructor.md).
> Bench procedure: [experiment.md](experiment.md).

---

## 1. Summary of concepts from prior days

Spend **5–8 minutes** refreshing these. Students need them today.

### Session 1 — Fruit battery (galvanic cell)

| Idea | What to remind them |
|------|---------------------|
| Oxidation / reduction | Oxidation = lose e⁻; reduction = gain e⁻ (OIL RIG) |
| Anode / cathode (galvanic) | Anode = oxidation = **negative (−)** terminal; cathode = reduction = **positive (+)** |
| Electron vs ion path | Electrons travel in the **wire**; ions travel in the **juice** |
| Series cells | Voltages add; current is still limited by the weak fruit electrolyte |
| Spontaneous chemistry | The reaction **makes** electricity — no battery required |

**One-sentence bridge:** *"Day 1: chemistry pushed electrons through a wire, all by itself."*

### Session 2 — Copper electroplating (electrolytic cell)

| Idea | What to remind them |
|------|---------------------|
| Electrolysis | Electricity **forces** a non-spontaneous reaction |
| Anode / cathode (electrolytic) | Signs **flip**: the object to plate goes on battery **(−)** = cathode = reduction |
| Cu²⁺ → Cu | Copper ions gain electrons and become solid metal on the object |
| Copper anode | The metal anode **dissolved** and replenished Cu²⁺ in the bath |
| Current & quality | Higher current → faster plating, but powdery or burnt deposits |
| Surface prep | Dirty or oily surfaces plate badly |

**One-sentence bridge:** *"Day 2: electricity pushed copper atoms onto a nail — but we watched, we didn't count."*

### What is new today

- Same electrolytic plating idea as Day 2
- The metal is **silver**: Ag⁺ + e⁻ → Ag, so **one electron per atom** — the simplest possible arithmetic
- The anode is **graphite (inert)** — it does **not** replenish Ag⁺, unlike Day 2's copper anode
- The bath contains a second salt, **KNO₃**, that is not a reactant at all
- Students **measure current and time**, then **calculate** moles, mass, atoms and thickness

**One-sentence goal:** *"Today we count how much silver we deposit, using electricity as a measuring stick."*

---

## 2. Class plan (90 min)

| Time | Block | What you do | Student product |
|------|-------|-------------|-----------------|
| 0–8 min | Prior-days review + hook | §1; show a dull copper coin | Oral answers |
| 8–18 min | Teach today's concepts | §3; board flowchart | Notes / vocab |
| 18–26 min | **Quiz check** | §4, cold call or mini-whiteboard | Quick answers |
| 26–42 min | **Interactive pre-lab** | §5 activity + worksheet | Completed pre-lab sheet (**required** before plating) |
| 42–52 min | Setup | Area; clean; wire with **resistor**; rehearse **live entry** | Setup table filled |
| 52–70 min | Plate | 15 min run + no-power control coin | Current log |
| 70–80 min | Post-lab calc | Same pipeline with **their** I_avg | Thickness + atom count |
| 80–86 min | Compare | Plated vs control; pH vs prediction | Comparison sheet |
| 86–90 min | Debrief + bridge | Efficiency; preview Session 4 | Exit ticket |

**Pacing tip:** do not start plating until the §5 pre-lab is checked. Groups that skip it stall later and wire the ammeter wrong.

---

## 3. Detailed explanations to give students

### 3.1 Hook (say this)

*"Yesterday copper appeared on a nail. Today we plate silver — and I want more than 'it looks shiny.' If we run 2 milliamps for 15 minutes, can we work out how many silver atoms landed, without weighing anything?"*

Answer: **yes**, if we know how charge relates to electrons, and electrons to atoms. That is **Faraday's law**.

### 3.2 The silver half-reaction (board)

```
Ag⁺(aq) + e⁻ → Ag(s)
```

- One Ag⁺ ion needs **exactly one electron** to become one silver atom.
- So **moles of Ag deposited = moles of electrons**, if every electron does that job.

**Contrast with Day 2:**

```
Cu²⁺ + 2e⁻ → Cu     ⇒  TWO electrons per copper atom
Ag⁺  +  e⁻ → Ag     ⇒  ONE electron per silver atom
```

Ask: *"Same number of electrons — more moles of Ag or of Cu?"* → **Ag**, because each atom is cheaper.

### 3.3 Two salts in the bath, doing two different jobs

This is a concept students have not met yet, and it comes back tomorrow in Session 4.

| Component | Job | Used up? |
|-----------|-----|----------|
| **AgNO₃, 0.05 M** | Supplies Ag⁺, which becomes the coating | **Yes** — the reactant |
| **KNO₃, 0.2 M** | **Supporting electrolyte** — carries current across the solution | **No** — a spectator |

*"Why add a salt that does nothing?"* Because without it the solution barely conducts. Charge has to physically cross the gap between the electrodes, and in a liquid that means ions moving. Dilute silver nitrate alone is a poor conductor, so most of your applied voltage is wasted pushing current through the liquid instead of driving chemistry — and the current concentrates on whatever sticks out furthest.

Tomorrow the sulfate in Session 4 does exactly the same job. Naming it now means it costs nothing to explain then.

**Water:** distilled only. Tap chloride precipitates AgCl and fogs the bath.

### 3.4 What current and time mean

| Symbol | Meaning | Units |
|--------|---------|-------|
| **I** | Current — how fast charge flows | ampere (A) = coulomb per second |
| **t** | Time current flows | seconds (s) |
| **Q** | Total charge passed | coulomb (C) |

```
Q = I × t
```

**Trap to say out loud:** meters read **mA**. 2 mA = 0.002 A. Forget the conversion and you are wrong by 1000×, and it will look perfectly reasonable on your calculator.

### 3.5 Faraday's constant

```
F = 96,485 C/mol e⁻  ≈  9.65 × 10⁴ C per mole of electrons
n_e = Q / F
```

Then for silver, since z = 1:

```
n_Ag = n_e
m_Ag = n_Ag × 107.87 g/mol
```

### 3.6 From mass to thickness

Silver density **ρ = 10.49 g/cm³**.

```
V = m / ρ           d = V / A
```

**A** = plated area in cm², estimated from the geometry.

**Say clearly:** the answer will be under a micrometre. You will not measure it with a ruler. The calculation predicts an invisibly thin film; your eyes only tell you it looks more silvery.

### 3.7 The full pipeline (draw as a flowchart)

```
I (A), t (s)
    →  Q = I × t
    →  n_e = Q / F
    →  n_Ag = n_e
    →  m = n_Ag × 107.87
    →  d = m / (ρ × A)
    →  N = n_Ag × 6.022×10²³
```

### 3.8 Why the current must be small — and why there is a resistor

This is new this year, and it is the difference between a coating and a mess.

Silver ions have to **travel** to the surface before they can be reduced. Near the coin they get used up, so more must diffuse in from the bulk. That sets a speed limit — a **maximum current the bath can support**, around **4 mA per cm²** for our stirred bath.

Push past it and the surface starts starving. Any bump that pokes out further reaches into fresher solution, so it grows faster, so it pokes out further still. That runaway is a **dendrite** — a grey fluffy tree that grows off the tips and eventually falls off.

*(If you have last year's photo of the failed overnight run, show it here. It is the perfect illustration.)*

So we aim for roughly a **quarter** of the speed limit: **0.5–1.0 mA/cm²**, about **2 mA on a coin**.

And rather than setting a voltage and hoping, we put a **1 kΩ resistor in series**. Since the bath now conducts well, the resistor dominates the circuit:

```
I ≈ (3 V − ~1 V across the cell) / 1000 Ω ≈ 2 mA
```

*"The resistor decides the current, not the chemistry."* That is why every bench will get the same answer.

### 3.9 The reaction that happens without us — and live entry

**Do not skip this.** It is the reason last year's attempt failed.

Copper metal and silver ions react on contact, with no battery involved at all:

```
Cu(s) + 2Ag⁺(aq) → Cu²⁺(aq) + 2Ag(s)        E° = +0.46 V
```

Copper is more reactive than silver, so it hands over electrons directly. This is **spontaneous, fast, and it goes essentially to completion** — the equilibrium constant is about 3×10¹⁵.

Ask: *"So if I just drop a copper coin in silver nitrate and walk away, what happens?"*

It gets coated in silver — but as a **loose grey powder that rubs straight off**, because the deposit forms wherever it likes with nothing controlling it. And anything you then plate on top comes off with it.

**The fix is embarrassingly simple: turn the power on first.**

Powering the object makes it a cathode from the instant it gets wet. Its own electrons stop leaving, so the copper cannot dissolve, so the loose layer never forms. Platers call it **live entry**.

1. Wire up with the object held **above** the bath
2. Switch on
3. Lower it in **while powered** — start the clock as it goes under
4. Lift it out **while still powered**, then switch off

*"The object is never in the liquid without a current. Not before, not after, not for a second."*

Each group also runs a **control coin** with no wires at all, so they can see for themselves what the copper does when left to its own devices.

### 3.10 Ideal vs real (set expectations before they plate)

Faraday thickness assumes:

1. Every electron plates silver (100% current efficiency)
2. The deposit is uniform
3. The area estimate is right
4. You used the average current

In reality some current makes side products, edges plate faster, and area is approximate. So the calculation is an **ideal estimate**, and today we get to check it two ways: against the control coin, and against the pH.

### 3.11 Safety (brief but firm)

- Gloves and goggles **before** pouring AgNO₃
- It stains skin and clothing dark brown-black, effectively permanently — that stain is metallic silver forming in your skin
- Small volumes only, 30–40 mL
- All silver waste to the labeled container — **never** the drain
- **Never** add ammonia to silver nitrate. Online "silver mirror" recipes do exactly this and the resulting solution forms an explosive solid on standing

---

## 4. Quiz questions (before the lab)

Cold call, pair-share, or a 3-minute written check. Answers in *italics*.

### A. Review from Days 1–2

**Q1.** In the fruit battery, which electrode was oxidized — zinc or copper?
*Zinc. Zn → Zn²⁺ + 2e⁻. Copper is where reduction happened.*

**Q2.** When electroplating, the object goes to which battery terminal, and why?
*Negative. That makes it the cathode, so metal ions can gain electrons and become metal.*

**Q3.** True or false: in an electrolytic cell the anode is always negative.
*False. In electrolysis the anode is on battery (+). In a galvanic cell it is negative.*

**Q4.** Why did Day 2 use a copper anode rather than any old metal?
*It dissolves and replenishes Cu²⁺ in the bath.*

### B. Today's concepts

**Q5.** Write the half-reaction for plating silver. How many electrons per atom?
*Ag⁺ + e⁻ → Ag. One.*

**Q6.** Our bath has AgNO₃ and KNO₃ in it. Which one ends up on the coin?
*Only the silver. The KNO₃ carries current and is still there at the end — a supporting electrolyte.*

**Q7.** A student measures 2 mA for 900 s. What is Q?
*I = 0.002 A; Q = 0.002 × 900 = 1.8 C.*

**Q8.** If Q = 9.65 C plates silver at 100% efficiency, roughly how many moles of Ag?
*n = Q/F ≈ 9.65/96,485 ≈ 1.0 × 10⁻⁴ mol.*

**Q9.** Why must the meter be in **series** on the current setting?
*Current mode measures charge flowing through the circuit. Across the battery it is a short, gives nonsense, and can blow the meter fuse.*

**Q10.** We use a graphite anode. Does it replace the Ag⁺ used at the cathode?
*No — graphite is inert. Ag⁺ comes from the bath and slowly depletes.*

**Q11.** Why distilled water and not tap?
*Tap water contains chloride, which precipitates AgCl and ruins the bath.*

### C. Today's new ideas

**Q12.** What happens if you drop a clean copper coin into silver nitrate with no battery at all?
*It gets coated with silver anyway — copper is more reactive and hands electrons straight to Ag⁺. But the deposit is loose grey powder that rubs off.*

**Q13.** So why do we switch the power on before the coin goes in?
*Live entry. Powering it makes it a cathode immediately, so the copper cannot dissolve and the loose displacement layer never forms.*

**Q14.** Why not just run 20 mA and finish in a minute?
*Silver ions cannot diffuse to the surface that fast. Past the limit the deposit goes dendritic — fluffy grey trees instead of a coating.*

**Q15.** What is the 1 kΩ resistor for?
*It sets the current. Since the bath conducts well, the resistor dominates the circuit, so every group gets the same current regardless of how their electrodes sit.*

### D. Stretch

**Q16.** Same charge, same efficiency — larger mass of Ag or of Cu? (M_Ag ≈ 108, M_Cu ≈ 63.5; remember z.)
*n_Ag = Q/F but n_Cu = Q/2F. Mass Ag = (Q/F)(108); mass Cu = (Q/2F)(63.5). Silver wins by a factor of about 3.4.*

**Q17.** The graphite anode releases H⁺. Predict the final pH — and say what it would mean if the real pH came out much higher than your prediction.
*Moles of H⁺ = moles of e⁻. If the measured pH is much higher, something at the cathode consumed protons instead of depositing silver — meaning the bath ran short of Ag⁺.*

---

## 5. Interactive activity + pre-lab calculation (required before plating)

### Activity: "Predict before you plate"

**Format:** pairs or threes. **15 minutes.**
**Goal:** every group completes one full Faraday calculation with realistic numbers before touching AgNO₃, then repeats it with real data after.

### Part 1 — Station card

| Parameter | Value |
|-----------|-------|
| Planned current I | **2.0 mA** |
| Planned time t | **900 s** (15 min) |
| Object | Copper coin, **one face** plates |
| Diameter | **2.0 cm** |

### Part 2 — Live prompts

1. **Area challenge (3 min).** Each group computes A = π(d/2)². Expected **3.14 cm²**. Anyone who says 12.6 used the diameter as the radius — fix it now.

2. **Unit police (2 min).** Hold up a meter reading "2.0" on mA. *"What goes into Q = It?"* Chorus: **0.0020 A**.

3. **Current-density check (2 min).** *"2 mA over 3.14 cm² — what is that per cm²?"* → **0.64 mA/cm²**. *"The bath tops out near 4. Are we safe?"* → yes, about a quarter of the limit. This is the number that decides whether they get a coating or a fluffy mess.

4. **Human flowchart (3 min).** Five volunteers hold signs: `I,t` → `Q` → `n_e` → `m` → `d`. The class shouts the formula linking each pair.

### Part 3 — Calculation worksheet

Complete **before** collecting silver solution. A TA initials one line per group.

**Constants:** F = 96,485 C/mol; M_Ag = 107.87 g/mol; ρ_Ag = 10.49 g/cm³

| Step | Formula | Work | Answer + unit |
|------|---------|------|---------------|
| 1. Area A | π(r)² | | ______ cm² |
| 2. Current density | I / A | | ______ mA/cm² |
| 3. Charge Q | I × t | | ______ C |
| 4. Moles e⁻ | Q / F | | ______ mol |
| 5. Moles Ag | n_Ag = n_e | | ______ mol |
| 6. Mass Ag | n × 107.87 | | ______ g |
| 7. Volume Ag | m / 10.49 | | ______ cm³ |
| 8. Thickness | V / A | | ______ cm and ______ µm |
| 9. Atoms | n × 6.022×10²³ | | ______ atoms |
| 10. Predicted pH | n_e ÷ volume in L, then −log | | ______ |

**Target answers (for you):**

| Step | Result |
|------|--------|
| A | **3.14 cm²** |
| Current density | **0.64 mA/cm²** |
| Q | 0.0020 × 900 = **1.80 C** |
| n_e | 1.80 / 96,485 = **1.87 × 10⁻⁵ mol** |
| m | **2.01 mg** (0.00201 g) |
| V | **1.92 × 10⁻⁴ cm³** |
| d | **6.11 × 10⁻⁵ cm = 0.61 µm** |
| Atoms | **1.1 × 10¹⁹** |
| Predicted pH in 30 mL | [H⁺] = 6.2 × 10⁻⁴ M → **pH 3.2** |

**Sense-checks to say:**

*"Two milligrams. Six tenths of a micrometre — about a hundredth the thickness of a sheet of paper. Eleven billion billion atoms. Those are all the same object, described three ways."*

*"And notice the last line: we have predicted the pH of the bath before we have run it. Tomorrow we do the same trick with a volume of gas."*

### Part 4 — Prediction statement

Each group writes one sentence:

> "Plating at about ______ mA for 15 minutes on ______ cm², we expect roughly ______ µm of silver, about ______ atoms, and the bath should finish near pH ______."

After the run they recalculate with **I_avg** and compare.

### Gate before chemicals

- [ ] Pre-lab table complete
- [ ] TA has checked Q, A, and the current density
- [ ] Gloves and goggles on
- [ ] Group can point to: cathode object (−), graphite anode (+), ammeter in series, **resistor in series**
- [ ] Group can state the **live entry** rule and say why it matters
- [ ] Second coin cleaned and ready as the **no-power control**

---

## 6. During and after the experiment — what to emphasize

1. Watch for the coin going into the bath unpowered. It is the single easiest mistake and it invalidates the comparison.
2. Log current often and use **I_avg**. With the resistor it should be nearly flat, and a flat current is itself worth remarking on.
3. If a calculated thickness comes out absurd — centimetres, or 10⁻¹² cm — check mA→A first, area second.
4. Make every group physically hold the two coins side by side. The control coin does more teaching than any explanation.
5. Debrief questions:
   - Did the coin look more silvery? Did the coating survive a rub?
   - How did the control compare, and what does that tell you?
   - Did the measured pH match your prediction? What would a mismatch mean?
   - Why is our graphite anode different from Day 2's copper anode?

---

## 7. Bridge to Session 4

*"We've counted metal atoms with electric charge, and we even predicted the pH of the bath. Tomorrow we split **water** — and the same law predicts a volume of gas we can actually see and measure. Same arithmetic, easier to check."*

Note the deliberate handoff: the KNO₃ they met today as a supporting electrolyte is exactly the role Na₂SO₄ plays tomorrow.

---

## 8. Vocabulary checklist

- [ ] Electrolytic cell vs galvanic cell
- [ ] Cathode / anode (electrolytic signs)
- [ ] Faraday constant; coulomb; ampere
- [ ] **Supporting electrolyte / spectator ion**
- [ ] **Displacement (immersion) plating**
- [ ] **Current density**
- [ ] Current efficiency
- [ ] Inert anode (graphite) vs sacrificial metal anode

---

## 9. Materials you need in hand while teaching

- Dull copper coin for the hook
- Board markers and flowchart space
- Pre-lab cards or a projected table
- Printed worksheet (§5 Part 3), one per group
- A demo ammeter showing mA, and a 1 kΩ resistor to hold up
- Graphite rod and a coin, to show polarity dry
- **Last year's photo of the dendritic overnight failure** — the best single visual in this session
