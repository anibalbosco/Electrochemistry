# Session 3 — Silver Plating and Faraday's Law

**Hook:** Work out how many silver atoms you deposited, and how thick the film is, without weighing anything.

## Learning outcomes

- Review galvanic vs electrolytic ideas from Sessions 1–2
- Distinguish a **reactant salt** (AgNO₃) from a **supporting electrolyte** (KNO₃) in the same beaker
- Plate silver onto copper at a **controlled current density**, and say why the value matters
- Use Q = It, n = Q/F, and the mass/thickness/atom-count relations
- Explain and apply **live entry**, and why copper spontaneously plates itself with silver without it
- Complete a Faraday prediction **before** plating, then test it against measured current, a control coin, and the pH

## Session plan (90 min)

| Time | Activity | Reference |
|------|----------|-----------|
| 0–8 min | Review Days 1–2 + hook | [lecture.md](lecture.md) §1, §3.1 |
| 8–18 min | Ag⁺ reduction, two salts, Faraday pipeline, current density, live entry | [lecture.md](lecture.md) §3 |
| 18–26 min | Quiz check | [lecture.md](lecture.md) §4 |
| 26–42 min | Interactive pre-lab calculation (**required gate**) | [lecture.md](lecture.md) §5 |
| 42–52 min | Estimate area; clean; wire with **resistor**; rehearse live entry | [experiment.md](experiment.md) — Parts A, B |
| 52–70 min | Timed plating run + **no-power control coin** | [experiment.md](experiment.md) — Part C |
| 70–80 min | Recalculate with real I_avg; compare with prediction | [experiment.md](experiment.md) — Part D |
| 80–86 min | Plated vs control; check pH against the charge | [experiment.md](experiment.md) — Part E |
| 86–90 min | Debrief efficiency; bridge to Session 4 | [lecture.md](lecture.md) §7 |

## Key equations

```
Ag⁺(aq) + e⁻ → Ag(s)

Q = I × t
n_e = Q / F              F = 96,485 C/mol
n_Ag = n_e               (z = 1)
m_Ag = n_Ag × 107.87 g/mol
d = m_Ag / (10.49 × A)
N = n_Ag × 6.022×10²³

And the reaction that happens with no battery at all:
Cu(s) + 2Ag⁺ → Cu²⁺ + 2Ag        E° = +0.46 V,  K ≈ 3×10¹⁵
```

## The bath

| Component | Concentration | Job |
|-----------|---------------|-----|
| AgNO₃ | **0.05 M** | The reactant — becomes the coating |
| KNO₃ | **0.2 M** | Supporting electrolyte — carries current, is not consumed |

Distilled water only. Target current density **0.5–1.0 mA/cm²**, about **2 mA** on a typical coin, set by a **1 kΩ series resistor**.

## Status

- [ ] KNO₃ chloride-tested against AgNO₃
- [ ] 0.05 M AgNO₃ / 0.2 M KNO₃ prepared with distilled water and labeled
- [ ] 1 kΩ resistors staged, one per station
- [ ] Two matched coins per group, one for the control
- [ ] Pilot run completed; live entry rehearsed
- [ ] Pre-lab worksheets printed ([lecture.md](lecture.md) §5)
- [ ] pH paper or meter checked against a buffer
- [ ] Silver waste container labeled, with a copper coil in it for recovery
