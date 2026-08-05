# Session 4 — Instructor Notes: Water Electrolysis Deep Dive

**Audience:** instructors and TAs only. Pair with [lecture.md](lecture.md) and [experiment.md](experiment.md).

---

## Why this session exists

For three days the students changed a **metal**. Today they change the **solvent**, and for the first time the product is something they can actually measure. That is what makes this the quantitative high point of the week: Session 3 asked them to trust Faraday's law, and Session 4 lets them audit it.

The session is built around one arc: **predict a volume from a current, then go and measure that volume.** Everything else — the conductivity ladder, the splint tests, the balloon — is scaffolding around that arc. If you are short on time, protect Parts B and C and cut elsewhere.

---

## Teaching sequence (keep this order)

1. **Distilled water beaker** — expect disappointment. That disappointment is the lesson.
2. **Ladder up through tap to electrolyte** — one voltage, three liquids, three currents.
3. **Measure I and predict** a gas volume in millilitres, on paper, before collecting.
4. **U-tube** — the ratio confirms the electron counting; the absolute volume audits the efficiency.
5. **Splint tests** — cheap, reliable identification of both gases.
6. **Balloon** — the memorable one, already running since before class.
7. **Derusting cells** — handoff to Session 5.

---

## The three things that most often go wrong

Ranked by how much damage they do, and all three are avoidable:

### 1. The balloon generator started too late

This is the most common failure and it is pure arithmetic. Faraday sets the pace:

| Current | H₂ rate | Time to a 500 mL balloon |
|---------|---------|--------------------------|
| 0.5 A | 3.8 mL/min | 132 min |
| 1.0 A | 7.6 mL/min | 66 min |
| 2.0 A | 15.2 mL/min | 33 min |
| 3.0 A | 22.8 mL/min | 22 min |

A "modestly inflated" party balloon is around 500 mL. There is no clever technique that beats this table — the electrons have to arrive one at a time. **Switch the generator on before the students walk in**, run the highest current your supply and electrodes tolerate, and pre-stretch the balloon so it does not fight the very low pressure the cell can deliver.

Pilot this and write the actual time in [materials.md](materials.md). It is the single most useful number to hand next year's version of yourself.

### 2. The U-tube filled below the side arms

Gas collects in the sealed dome under each stopper and pushes the liquid **down**; the displaced liquid rises into the open side arm, which is the vent. So:

- Fill until liquid **stands part-way up both side arms**, equal on both sides.
- If you fill to below the side-arm junction, the gas has a free path out of the side arm. The cell bubbles beautifully and collects nothing, which is a genuinely confusing failure to debug live.
- Stop the run before the falling level in the **H₂** limb reaches its side-arm junction. The H₂ limb fills twice as fast, so it always gets there first, and once it vents the ratio slides toward 1.

### 3. Timing started before the solution is saturated

The first gas produced dissolves rather than collecting, and it does so unequally, because O₂ is roughly twice as soluble as H₂. Run **2–3 minutes before marking t = 0** and most of that error disappears. Groups that skip it get the worst ratios and conclude the chemistry is unreliable.

---

## Atomic and molecular foundations

### Why pure water fails

Autoionization gives [H⁺] = [OH⁻] = 10⁻⁷ M at 25 °C, against a water concentration of 55.5 M — about **one molecule in 550 million** is ionized. Conductivity of ultrapure water is around 0.055 µS/cm; typical tap water is 50–800 µS/cm; 0.1 M Na₂SO₄ is on the order of 10,000 µS/cm.

That spread is why the ladder is worth doing as three rungs rather than two. Tap water is the interesting middle case: it is emphatically not pure, and students who have been told "water doesn't conduct" need to meet the version of the statement that is actually true — *pure* water conducts poorly, and purity is a variable, not a property of the word "water."

### Why Na₂SO₄ and not something else

Sodium is far too difficult to reduce in water (its reduction potential is well below that of water itself, so hydrogen evolves instead), and sulfate is already at maximum oxidation state, so neither ion has a competing half-reaction available. Both are pure charge carriers. This is the definition of a supporting electrolyte, and it is a concept students have not met in Sessions 2 and 3, where the dissolved salt was the *reactant*. Make the contrast explicit — the table in [lecture.md](lecture.md) §3.3 exists for this.

| Electrolyte | Verdict | Reason |
|-------------|---------|--------|
| Sodium sulfate | **Planned** | Inert; no competing half-reaction |
| Baking soda | Backup | No chlorine risk, but CO₂ evolution muddies the anode gas measurement |
| Table salt | **Never** | Chloride oxidizes in preference to water → Cl₂ |
| Sulfuric acid | Not for this age group | Works well, but the hazard is not worth it |

### Half-reactions and where the 2:1 comes from

**Cathode (−):** `2H₂O + 2e⁻ → H₂ + 2OH⁻`
**Anode (+):** `2H₂O → O₂ + 4H⁺ + 4e⁻` (or `4OH⁻ → O₂ + 2H₂O + 4e⁻` in base)
**Overall:** `2H₂O → 2H₂ + O₂`

Four electrons make **two H₂ and one O₂**. Series circuit ⇒ identical charge through both electrodes ⇒ the ratio is forced. Then Avogadro does the rest: equal numbers of gas molecules occupy equal volumes at the same temperature and pressure, so the mole ratio *is* the volume ratio.

Worth saying explicitly, because students often think the 2:1 comes from the formula H₂O. It does, but only via the electron count — and framing it that way is what makes Faraday's law feel like a tool rather than a formula.

---

## Faraday coaching (Part B)

```
ṅ(H₂) = I / (2F)     ṅ(O₂) = I / (4F)     F ≈ 9.65 × 10⁴ C/mol
V̇(H₂) in mL/min ≈ 7.6 × I  (I in A, room conditions)
```

- **mA → A first, every time.** A thousandfold error is invisible on a calculator.
- The 2:1 is already present in the mole rates. The U-tube confirms chemistry students have *already derived*; it is not a new fact.
- Molar volume: 24.45 L/mol at 25 °C, or 22.4 L/mol at 0 °C. Pick one and stay with it all session. Mixing them introduces a 9% discrepancy that will surface exactly when you are computing efficiency and trying to explain a 15% shortfall.

### The efficiency conversation

The measured-over-predicted ratio is the payoff of the whole week's arithmetic. Expect **70–95%**. Losses:

| Loss | Typical size |
|------|--------------|
| Gas dissolved in solution | Largest single term, especially early |
| Leaks past stoppers | Variable; the fixable one |
| Side reactions on graphite (anode attack) | Small but real; grows with current |
| Gas escaping the side arm | Should be zero if the fill level is right |

Above 100% is always a measurement artifact: an air bubble trapped under the stopper at t = 0, a mis-measured tube diameter (it enters squared, so a 10% diameter error is a 21% volume error), or a t = 0 mark made after the run had already started.

### Voltage talking points

- 1.23 V thermodynamic floor.
- Onset of visible bubbling on graphite is typically **1.6–2.0 V** — the gap is overpotential, mostly on the oxygen side, which is kinetically the harder reaction.
- Several volts to run briskly; the surplus is dissipated as heat and buys rate, not yield per coulomb.
- If your supply is adjustable, hunting the bubbling threshold is a genuinely nice measurement and takes 90 seconds.

---

## U-tube coaching (Part C)

Equal bore in both limbs means **column height ratio = volume ratio**, so the diameter is irrelevant to the ratio and only needed for the absolute Faraday check. Measure it once, put it on the board, done.

**Accept 2.0–2.6.** Tell students the expected direction *before* they measure — see [lecture.md](lecture.md) §3.8. Causes of a high ratio:

| Cause | Note |
|-------|------|
| O₂ roughly 2× more soluble than H₂ | Dominant early; mostly cured by pre-saturating |
| Graphite anode attacked; some O as CO₂ | CO₂ is highly soluble, so it vanishes from the gas phase |
| O₂ evolution has the larger overpotential | Slower to start |

A ratio **below 2** is a fault, not a subtlety. Check the H₂ stopper seal first, then whether the H₂ level reached the side arm.

---

## Gas identification (Part D)

### Splint tests — do these even if the balloon works

| Gas | Test | Why it works |
|-----|------|--------------|
| H₂ | Lit splint at the mouth → **squeaky pop** | H₂ burns in the air around it; the pop is the flame front crossing the gas/air boundary |
| O₂ | Glowing splint → **relights** | Pure O₂ raises the combustion rate enough to restart a smouldering ember |

These take two minutes, cost nothing, work every time, and are a *better* piece of chemistry than the balloon because they identify **both** gases rather than one. At 0.3 A a 10 mL test tube of hydrogen fills in about 4 minutes — start them at the beginning of Part C.

Keep collection tubes **mouth-down** until the moment of testing. Hydrogen is 14 times lighter than air and leaves an upright tube almost immediately.

### The balloon — safety and physics

Beyond the timing table above:

- **Cathode gas only.** A balloon of pure H₂ deflagrates: it burns at the surface where it meets air, giving a bark. A stoichiometric H₂/O₂ mixture **detonates** — much louder, genuinely dangerous, and never a classroom demo.
- **Never a rigid container.** A balloon fails by tearing; glass fails by becoming shrapnel.
- Untie and ignite **well away from the generator**, which is still making hydrogen the whole time.
- Warn the room. The bang startles, and some students find it genuinely distressing.
- Have the extinguisher present and know where it is, not merely "in the building."

The teaching moment is immediately afterwards, while the room is still noisy: that bang was the electrical energy of the last hour coming back out in a fraction of a second. Hydrogen stored it. That is what "energy carrier" means, and it is the honest version of the hydrogen-economy story — round-trip efficiency is well under 100%, and the electricity has to come from somewhere first.

---

## Part E — Rust removal handoff

| Role | Connection |
|------|------------|
| Rusty iron | Battery **−** (cathode) |
| Sacrificial steel or graphite | Battery **+** (anode) |
| Electrolyte | Washing soda (preferred) or baking soda — **never NaCl** |

**Power supply matters more than anything else here.** A 9 V alkaline holds about 500 mAh and a derusting cell pulls a few hundred mA. It is flat in roughly two hours, and Session 5 then opens on a nail indistinguishable from the control — which is a bad start to the synthesis day. Use a mains supply or a 5 V USB brick. If neither exists, run the cells for 60–90 minutes during class and accept a smaller effect, rather than trusting a battery to last the night.

Also: these cells evolve hydrogen continuously. Jars stay **open**, the room stays **ventilated**, and nothing sealed is ever used. Confirm the venue's overnight-power policy in advance rather than at 4 pm on the day.

Photograph the "before". Set up an unpowered control in the same solution. Without both, tomorrow's reveal is an anecdote.

---

## Misconceptions

| Misconception | Correction |
|---------------|------------|
| "The bubbles are steam." | H₂ and O₂. The water is being chemically split, not boiled — the beaker is barely warm. |
| "Water doesn't conduct electricity." | *Pure* water conducts poorly. Tap water conducts measurably. That is the whole point of the ladder. |
| "The salt gets used up making the gas." | Na⁺ and SO₄²⁻ are spectators. Water is the only reactant. |
| "Salt would work better." | Salt makes chlorine. A competing half-reaction, not a rule for its own sake. |
| "We need a big voltage because water is strong." | Minimum is 1.23 V. The excess is kinetics and resistance, and it becomes heat. |
| "Current and stoichiometry are separate topics." | Faraday's law **is** stoichiometry, written in electrons. |
| "The 2:1 comes from the formula H₂O." | It comes from the electron counts, 2 and 4 — which of course trace back to the formula, but the electrons are the mechanism. |
| "Hydrogen is a fuel like petrol." | It is a carrier. The energy came from the socket, and you never get all of it back. |
| "Our ratio was 2.3, so the experiment failed." | 2.0–2.6 is the correct answer for this apparatus, and its direction is predictable. |

---

## Board plan

1. Beaker, two rods, distilled water. Write "1 in 550 million."
2. Add ions: draw Na⁺ and SO₄²⁻ shuttling. Write "spectators."
3. Half-reactions, with **2 e⁻** and **4 e⁻** circled.
4. `ṅ = I/(nF)` → `7.6 × I mL/min` → predicted volume in a box.
5. `2H₂O → 2H₂ + O₂`, circle the 2:1.
6. Reserve a corner for measured ÷ predicted = efficiency. Fill it in live from the first group that finishes.
7. Safety: no NaCl; side arms open; flame is mine.
8. Before dismissal: **rusty iron on negative.**

---

## Optional enrichment

- Conductivity measured properly, in µS/cm, if you have a meter — turns the ladder from qualitative to quantitative.
- Collected gas is saturated with water vapour; correcting for vapour pressure (~3.2 kPa at 25 °C, about 3% of atmospheric) is a nice touch for the strongest students and explains part of a systematic overestimate.
- Overpotential on graphite vs platinum, and why fuel cells pay for platinum.
- Alkaline vs PEM electrolyzers at industrial scale; the thousands-of-amps comparison lands well right after they compute 23 mL in ten minutes.
- **Universal indicator** in the electrolysis cell, if you can get it for next year: the cathode region turns blue-purple from OH⁻ and the anode region red-yellow from H⁺, making the half-reactions directly visible. Cheap, fast, and the most vivid single upgrade available to this session.
