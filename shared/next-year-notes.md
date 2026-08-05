# Next Year — Changes to Make Before Day 1

Sessions 4 and 5 were rewritten in place. This page collects everything that should change in **Sessions 1–3**, which were already taught, plus the week-level changes worth making before the course runs again.

Work down from the top. The items are in order of how much difference they make.

---

## 1. Start the corrosion jars on Day 1 — not later

**The single most important change on this page.**

Session 5's jar comparison needs four to five days to develop. Previously that requirement was documented only inside Session 5's own preparation notes, which is the one place nobody reads in time to act on it. It now lives in [multi-day-setup.md](multi-day-setup.md), and Session 1 should end with ten minutes of jar building.

It also lands well pedagogically. Students have just spent ninety minutes building a battery from two dissimilar metals in an electrolyte. Jars A, B and C are the same cell, left running, doing damage. The teaser writes itself:

> *"You just made electricity from two different metals in a liquid. Bad news: this happens whether you want it or not. These three jars sit here all week."*

Add to Session 1's session plan: **80–90 min — build corrosion jars A/B/C for Session 5.**

---

## 2. Make the ammeter standard in Session 2

Session 2 currently lists the multimeter as optional and the current-limiting resistor as optional. Both should be standard, for different reasons.

**The ammeter**, because Session 3 depends on students being fluent with a series ammeter, and Session 3's notes already record groups wiring it wrong and stalling. Day 2 is the low-stakes place to learn that skill — nothing depends on the reading, so a mistake costs nothing. By Day 3 it costs the whole calculation.

**The resistor**, because a 9 V battery straight into a plating cell drives more current than a smooth deposit tolerates, and the black powdery result is already listed in the troubleshooting table as a known failure. Either use a 3 V pack as standard, or make the 220–470 Ω resistor a required part rather than a variable to explore.

Then Session 2 can log current and time alongside the visual result — which sets up Day 3 as *"you already recorded everything you needed to count the atoms, you just didn't know it yet."* That is a much stronger opening for Day 3 than starting from scratch.

---

## 3. Session 3 — rebuilt (done, but read this)

Session 3 was rewritten after a pilot run went wrong in an instructive way: a copper ring left overnight in 0.01 M AgNO₃ at 0.6 mA produced a fluffy grey dendritic mass instead of a coating, and the pH barely moved. Three separate faults, all now fixed.

**The bath could not sustain the target current.** At 0.01 M with no supporting electrolyte, the diffusion-limited current density is about 0.6 mA/cm². The old sheet targeted 10–30 mA on a ~3 cm² coin, which is roughly ten times what the solution can deliver. Past that limit the deposit does not degrade gradually — it goes dendritic, because any protrusion reaching into fresher solution grows faster, which is a runaway. The bath is now **0.05 M AgNO₃ in 0.2 M KNO₃**, which raises the ceiling to about 4 mA/cm² stirred, and the target is **0.5–1.0 mA/cm²**, roughly a quarter of it.

**Note the counter-intuitive part**, because it will come up: adding KNO₃ *lowers* the limiting current at fixed silver concentration, by about 1.9×. Without supporting electrolyte, Ag⁺ arrives by diffusion **and** migration; flooding the solution with inert ions means K⁺ carries the migration current instead. Supporting electrolyte alone would have made the dendrites worse. It only helps because the silver went up five-fold at the same time.

**Nothing controlled the current.** Setting a voltage means current depends on immersion depth, spacing and surface state, so no two benches agree. There is now a **1 kΩ series resistor** at every station: with a conductive bath, the resistor dominates the circuit and sets the current at about 2 mA regardless of what the electrodes are doing. This is also why the current now stays flat, which makes I_avg trivial.

**Copper plates itself with silver whether you like it or not.** Cu + 2Ag⁺ → Cu²⁺ + 2Ag has E° = +0.46 V and K ≈ 3×10¹⁵, so a copper object in silver nitrate strips the bath essentially dry given time, depositing loose powder that nothing sticks to. The session now teaches **live entry** — power on before the object touches the liquid, power off only after it leaves — and runs a deliberate **no-power control coin** alongside every plating run, so students can see the difference for themselves rather than having it described.

Also fixed while in there: the two worked examples that used different areas and reached different thicknesses are now a single consistent one (2.0 mA, 900 s, 3.14 cm² → 0.61 µm, 1.1×10¹⁹ atoms); the volume went from 20 to 30–40 mL; and the mass-balance efficiency check is now labelled honestly as beyond a ±0.001 g balance, with the efficiency question handed forward to Session 4 where a gas volume can actually be measured.

**New in the session, and worth keeping:** students now predict the **final pH** from the charge before running, and check it. It works when the bath is healthy, and it fails in a specific, diagnosable direction when the bath is exhausted — which is exactly what happened in the pilot.

### Still worth doing for Session 3 next year

- **A silver anode** (sterling wire, or a bullion round as a permanent purchase) would replenish Ag⁺, remove the pH drift and make the bath effectively immortal. The trade-off is that it removes the pH-prediction exercise, which is now one of the better parts of the session.
- **A magnetic stirrer** roughly doubles the sustainable current density.
- **A complexed-silver bath** (thiosulfate) is what would actually give a bright, mirror finish, and it suppresses the displacement reaction outright — at 0.1 M free thiosulfate the free Ag⁺ drops to ~10⁻¹³ M, which puts silver *below* copper and reverses the driving force. Worth piloting over the summer rather than introducing mid-week. Never acidify thiosulfate.

## 4. Plant Day 5's aluminium surprise on Day 1

Session 1's "Extension B — compare metals" already invites students to try aluminium foil against copper, and already notes the oxide film. Make that extension a required rather than optional part of Day 1, and have groups record the number.

Then on Day 5, when aluminium is predicted at −1.66 V and reads below iron, you can point back: *you saw this on Monday and we did not explain it. Here is why.* A surprise that has been sitting in their own notebook for four days lands considerably harder than one introduced cold.

---

## 5. Bring Sessions 1 and 2 up to the Session 3 format

Session 3's `lecture.md` is a full teaching script — prior-day review, class plan, detailed explanations, quiz questions with answers, an interactive pre-lab with a worked answer key, and a bridge forward. Sessions 4 and 5 have now been rebuilt to match. Sessions 1 and 2 are still in the original thin format.

The pieces worth adding to each:

| Piece | Why it earns its place |
|-------|------------------------|
| Prior-day review table | Five to eight minutes that make every session feel like part of one argument |
| Quiz questions with answers | Catches misconceptions before students are holding chemicals |
| A pre-lab gate | A worksheet checked before the practical starts. In Session 3 this demonstrably stopped groups stalling mid-run |
| Bridge sentence to the next day | The week reads as a story rather than five experiments |

Session 1 also has room for one genuinely quantitative addition: measure the fruit cell's voltage on open circuit and again under load, and use the difference to calculate the internal resistance. It costs five minutes, it explains why the LED disappoints, and it introduces a real measurement on the very first day.

---

## 6. Week-level changes already made

These are done, and are noted here so the reasoning is not lost:

**Session 5's fuel cell was removed** and the folder renamed to `05-corrosion-and-rust-removal`. The fuel cell was in the folder name but had already been dropped from the teaching, which left the session's title promising something it did not deliver. If it comes back one day, the cheapest version needs no kit at all: after the U-tube run, disconnect the supply and read the voltage across the same graphite electrodes — the gas still clinging to them makes a genuine, if feeble, H₂/O₂ cell.

**Session 4's timing was rebuilt around the balloon.** Filling a party balloon with electrolytic hydrogen takes 30–60 minutes at any current a classroom supply will deliver. The old plan allocated ten minutes. The generator now starts before the students arrive, and the splint tests carry the actual gas identification.

**Overnight derusting moved off 9 V batteries.** A 9 V alkaline holds around 500 mAh against a cell drawing a few hundred mA — flat in roughly two hours, so Session 5 opened on a nail indistinguishable from the control. Mains supply or a 5 V USB brick.

**The U-tube fill instruction was corrected.** The old text said to fill *below* the side-arm ports, which lets the collected gas escape straight out of the side arm. The apparatus works the other way round: fill until liquid stands part-way **up** both side arms, so the arms act as vents for displaced liquid while the gas stays trapped under the stoppers.

**The expected H₂:O₂ ratio was corrected** from 1.6–2.2 to 2.0–2.6. Oxygen runs short in this apparatus — it is twice as soluble as hydrogen, and graphite anodes lose some of it as CO₂. A ratio below 2 signals a leak, not a subtlety, and telling students the direction of the expected error in advance turns it from a failure into a prediction.

---

## 7. Materials worth buying before next year

| Item | Session | What it buys |
|------|---------|--------------|
| **Universal indicator** | 4 | The cathode region turns blue-purple from OH⁻ and the anode red-yellow from H⁺, within seconds. The half-reactions stop being abstract. Cheapest big upgrade in the week |
| **Ferroxyl indicator** (K₃[Fe(CN)₆] + phenolphthalein) | 5 | Anodic sites go blue and cathodic sites pink in **minutes**. Session 5 would no longer depend on jars started on Day 1. Standard school reagent; never acidify it, never heat it |
| Conductivity meter | 4 | Turns the conductivity ladder from qualitative to a measurement in µS/cm |
| ±0.1 mg balance | 2, 3 | Makes the plating efficiency check actually possible |
| More graphite rods | 3, 4, 5 | They erode, and Session 4's balloon generator eats them |
| Rusty hardware, collected early | 4, 5 | Genuinely hard to source on demand. Leave nails in saltwater for a fortnight, or start a jar now |

---

## 8. Fill in the teaching log

[teaching-log.md](teaching-log.md) has a page per session with the numbers worth capturing — currents, voltages, minutes-to-fill, what overran. Fill it in during the ten minutes after each session ends, not the following week.

Next year, the pilot-notes tables in each session's `materials.md` are the first thing to populate from that log. A prep sheet that says *"I: tap 4 mA, Na₂SO₄ 310 mA, balloon ready in 38 min"* is worth more than any amount of rewritten prose.
