# Session 3 — Instructor Notes: Silver Plating + Faraday Deep Dive

**Audience:** instructors and TAs only.
**Classroom teaching script** (review, quiz, pre-lab): [lecture.md](lecture.md).
**Bench procedure:** [experiment.md](experiment.md).

---

## Why this session exists

Students saw copper move in Session 2. Now they **quantify** electrodeposition: charge → moles of electrons → moles of metal → mass → thickness → atoms. Silver is ideal because Ag⁺ + e⁻ → Ag is 1:1. This is the week's heaviest math session — go slowly on units.

---

## What changed this year, and why

The original bath was **0.01 M AgNO₃ with no supporting electrolyte, run at 10–30 mA by setting a voltage**. Three things were wrong with that, and they compound.

**It was far past the diffusion limit.** At 0.01 M unstirred, the maximum current the bath can sustain is about **0.6 mA/cm²**. On a 3 cm² coin that is under 2 mA total. Targeting 20 mA meant asking for roughly **ten times** what the solution can deliver. Beyond the limit the deposit does not just get worse gradually — it changes character, into dendrites.

**The current was never going to reach the target anyway.** 0.01 M AgNO₃ with nothing else in it is a poor conductor. A measured cell resistance of about 1700 Ω means a 3 V pack delivers under 2 mA no matter what the instruction sheet says. Groups would have chased a target they could not physically hit.

**Nothing controlled the current.** Setting a voltage means the current depends on immersion depth, electrode spacing and surface state, so every bench gets a different number and there is no way to compare results.

### The fixes

| Change | What it fixes |
|--------|---------------|
| **0.05 M AgNO₃** (up 5×) | Raises the diffusion limit to ~4 mA/cm² stirred; also makes depletion negligible |
| **0.2 M KNO₃ supporting electrolyte** | Drops solution resistance; even current distribution; introduces a concept reused tomorrow |
| **1 kΩ series resistor** | The resistor sets the current, so all benches match and the current stays flat |
| **Target 0.5–1.0 mA/cm² (~2 mA)** | About a quarter of the limit — the classic smooth-deposit window |
| **Live entry** | Prevents the displacement underlayer that stops coatings adhering |
| **No-power control coin** | Makes the displacement reaction a measured result rather than a hidden confounder |
| **15 min instead of 5** | Gets thickness to ~0.6 µm at the lower current |

### A counter-intuitive point you should understand before teaching it

Adding KNO₃ **lowers** the limiting current at fixed silver concentration, by about a factor of 1.9.

Without a supporting electrolyte, Ag⁺ reaches the cathode by *two* mechanisms: diffusion **and** migration in the electric field. Adding an excess of inert ions means K⁺ carries nearly all the migration current instead, so silver arrives by diffusion alone. The transport number of Ag⁺ in AgNO₃ is about 0.46, and the enhancement factor 1/(1−t₊) is therefore about 1.9.

So supporting electrolyte on its own would have made the dendrites **worse**. It only helps because we raised the silver concentration five-fold at the same time. If someone asks "why not just add KNO₃ to the old bath," this is the answer — and it is a genuinely good question to get.

---

## Atomic / electronic foundations

```
Ag⁺(aq) + e⁻ → Ag(s)
```

Silver (Z = 47) loses one valence electron to form Ag⁺; plating returns it. Hence **n_Ag = n_e** at 100% efficiency.

Compare Session 2:

```
Cu²⁺ + 2e⁻ → Cu    ⇒   n_Cu = n_e / 2
```

Mention the contrast so students see why the electron count in the half-reaction matters.

---

## The displacement reaction — own this thoroughly

```
Cu(s) + 2Ag⁺(aq) → Cu²⁺(aq) + 2Ag(s)        E° = +0.458 V
ΔG° = −88 kJ/mol        K ≈ 3 × 10¹⁵
```

At [Cu²⁺] = 5 mM the equilibrium [Ag⁺] is around 10⁻⁹ M. In other words a copper object left in silver nitrate will strip the bath **essentially dry**, given time. This is not a side effect to be managed; on a long timescale it is the dominant reaction.

**Consequences for teaching:**

- The deposit it produces is loose, dendritic and poorly adherent, because nothing controls where or how fast it forms. Anything electroplated on top delaminates with it.
- It is **pH-neutral** in the acid sense, and it passes no current through your external circuit — so it is invisible to your ammeter and to your Faraday calculation. A student can deposit a great deal of silver that their arithmetic knows nothing about.
- It is also the standard method for **recovering silver from waste**. Put a copper coil in the waste bottle; the same reaction that spoils the plating cell cleans out the waste. Worth doing, and worth pointing out.

### Live entry

Making the object cathodic before it wets holds it below its own corrosion potential, so the copper cannot dissolve and the displacement reaction cannot proceed. With the 1 kΩ resistor in place, the first moment of contact wets a tiny area at ~2 mA, so the local current density is very high and protection is emphatic.

Watch for the failure mode where a student dunks the coin to "check it fits" before switching on. That one action produces the loose layer and everything afterwards is compromised. Have TAs stand at each bench for the first entry.

### Commercial context, if a student asks how real plating avoids this

Two answers, both worth a sentence. Industry plates from **complexed** silver, not free Ag⁺ — historically cyanide, now succinimide or thiosulfate systems. Complexing collapses the free-silver activity by ten orders of magnitude, which both kills the displacement driving force and forces fine-grained nucleation. A thiosulfate bath at 0.1 M free S₂O₃²⁻ puts [Ag⁺] near 10⁻¹³ M, which makes E(Ag⁺/Ag) about +0.04 V — now *below* copper, so displacement runs backwards and stops. Industry also uses a **silver strike**: a brief, very dilute, high-current first layer that establishes a bonded film before the main plate.

We are not doing either, because a new bath chemistry introduced mid-week is a bigger risk than a matte finish. Live entry plus the control coin gets us most of the teaching value.

**A warning to pre-empt:** students who search this at home will find "silver mirror" recipes using ammoniacal silver nitrate (Tollens'). Ammonia does **not** help — it complexes copper about as strongly as silver, so the displacement driving force is essentially unchanged — and ammoniacal silver solutions deposit explosive silver nitride on standing. Say this out loud before someone tries it.

---

## Faraday's law — instructor mastery

```
Q = I × t          n_e = Q / F          F = 96,485 C/mol e⁻
n_metal = Q / (z F)          m = n M          V = m / ρ          d = V / A
```

| Metal ion | z |
|-----------|---|
| Ag⁺ | 1 |
| Cu²⁺ | 2 |
| Al³⁺ | 3 |

| Quantity | Silver |
|----------|--------|
| M | 107.87 g/mol |
| ρ | 10.49 g/cm³ |
| A | geometric plated area — **the biggest student error source** |

### Worked example — the board version (memorize this one)

I = 0.0020 A, t = 900 s, A = 3.14 cm² (a 2.0 cm coin, one face):

| Step | Math | Result |
|------|------|--------|
| Q | 0.0020 × 900 | **1.80 C** |
| n_e | 1.80 / 96,485 | **1.87 × 10⁻⁵ mol** |
| n_Ag | = n_e | 1.87 × 10⁻⁵ mol |
| m | × 107.87 | **2.01 mg** |
| V | m / 10.49 | 1.92 × 10⁻⁴ cm³ |
| d | V / 3.14 | 6.11 × 10⁻⁵ cm = **0.61 µm** |
| N | n × 6.022×10²³ | **1.1 × 10¹⁹ atoms** |

**Use these numbers everywhere.** Last year `lecture.md` and `experiment.md` carried two different worked examples with different areas and different answers, which reads as an inconsistency to any student comparing the two files.

**Sense-check:** 0.1–2 µm is the sane window. Outside it, suspect mA→A or the area.

### Average current

With the resistor the current should be nearly flat, so I_avg is easy. If it does drift, use the mean of the logged values or a trapezoidal estimate — never the first reading alone.

---

## The pH check — new this year, and a genuine test

Graphite anode: `2H₂O → O₂ + 4H⁺ + 4e⁻`, so **moles H⁺ = moles e⁻**.

For the worked example in 30 mL: 1.87 × 10⁻⁵ mol in 0.030 L = 6.2 × 10⁻⁴ M → **pH 3.2**, from about 7.

This is a real, checkable prediction, and it also functions as a diagnostic. If the measured pH comes out **much higher** than predicted, protons are being consumed at the cathode — which means the cathode has run short of Ag⁺ and switched to reducing dissolved O₂ or nitrate instead. That is precisely what happens in an over-driven or exhausted bath.

At 0.05 M, a 15-minute run consumes only about **1%** of the silver in 30 mL, so this failure mode should not appear. If it does, look for a bath that has been sitting with copper objects in it.

**Practical caution on measurement:** silver ions are hostile to glass pH electrodes with KCl references — chloride leaking from the junction precipitates AgCl right where the junction is, and readings drift. Calibrate immediately before use, rinse the probe well afterwards, and treat a suspicious reading as an instrument problem before treating it as chemistry. Paper is acceptable here; you only need to resolve about one pH unit.

---

## Current efficiency

```
η = (charge that plated Ag) / (total charge)  ≤ 1
```

Loss channels: side reductions, non-uniform current (edges plate more), and deposit that rinses away. Note that displacement silver pushes the *apparent* efficiency **above** 100% if you weigh the object, because that silver arrived without passing through your ammeter — another reason the control coin matters.

Honest note for the debrief: with a ±0.001 g balance and a 2 mg deposit, a mass-based efficiency measurement is not really possible — the deposit is only twice the balance resolution. Tell students that, and flag forward: **tomorrow's gas volume is easy to measure, so Session 4 is where we finally audit the efficiency we have been assuming all week.**

---

## Electrochemical series

| Couple | E° (V) |
|--------|--------|
| Ag⁺/Ag | +0.80 |
| Cu²⁺/Cu | +0.34 |
| H⁺/H₂ | 0.00 |

The 0.46 V gap between silver and copper is exactly what drives both the useful plating and the unwanted displacement. Same number, two consequences.

**Anode choice.** Graphite is inert: Ag⁺ comes only from the bath and is not replenished, and O₂ plus H⁺ are produced instead. At 0.05 M this is fine for classroom runs. If you ever acquire a silver anode (sterling wire, or a 1 oz bullion round — a reusable purchase), it would replenish Ag⁺, eliminate the pH drift entirely, and make the bath effectively immortal. It would also remove the pH prediction exercise, which is now one of the better parts of the session, so it is not an unambiguous upgrade.

---

## Experiment coaching

**Area estimation.** Coach aggressively. Coin face = πr² per face; washer = π(R² − r²); irregular = length × width of the immersed region, stated as an approximation. Students who invent a huge area get an absurdly small thickness and conclude Faraday "failed."

**Ammeter in series.** Walk every station once. This is also rehearsal for Session 4.

**Timing discipline.** Clock starts as the powered object enters the liquid; stops as it leaves, still powered.

**What success looks like.** An even whitish-silver sheen, **matte rather than mirror** — classroom baths have no brighteners. Burnishing with a soft cloth brings it up noticeably and is normal practice. It should survive a firm rub; the control coin should not.

---

## Misconceptions

| Misconception | Correction |
|---------------|------------|
| "Q = I + t" | Q = I × t |
| "Use mA directly in Q = It" | Convert to amperes |
| "Cu and Ag use the same z" | Ag⁺ needs 1 e⁻; Cu²⁺ needs 2 |
| "Thickness should be measurable with a ruler" | Sub-micrometre. Appearance is qualitative |
| "Faraday is wrong, the deposit looks thin" | Efficiency and area errors dominate |
| "More current means a better coating" | Past the diffusion limit, more current means dendrites |
| "The KNO₃ ends up in the coating" | It is a spectator; only silver deposits |
| "Nothing happens until you switch on" | Copper displaces silver spontaneously. The control coin proves it |
| "A thicker coating is always better" | Adhesion beats thickness. A loose 5 µm layer is worse than a bonded 0.5 µm one |

---

## Board plan

1. `Ag⁺ + e⁻ → Ag`; circle "1 electron per atom."
2. Two-column table: AgNO₃ = reactant, KNO₃ = spectator.
3. Flowchart: I,t → Q → n_e → n_Ag → m → V → d → N.
4. Full numerical example with units at every step.
5. `Cu + 2Ag⁺ → Cu²⁺ + 2Ag`, E° = +0.46 V. Write **LIVE ENTRY** beside it and box it.
6. Current density: 2 mA / 3.14 cm² = 0.64, limit ≈ 4. Write "stay at a quarter."
7. Predicted pH, in a box, to be checked at the end.
8. Bridge: tomorrow the same law predicts a **gas volume** we can actually measure.

---

## Optional enrichment

- Recover the silver from the waste bottle with copper wire and weigh it. Full circle, and it is real chemistry.
- Retroactively derive z for Session 2's copper from their own logged data.
- Hall–Héroult aluminium smelting as an industrial Faraday consumer — a single potline runs several hundred thousand amperes.
- Why complexing agents give bright deposits: fewer free ions, higher nucleation overpotential, finer grain.
- For a strong student: derive the limiting current from Fick's first law and explain why stirring raises it.
