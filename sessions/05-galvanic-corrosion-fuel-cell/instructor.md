# Session 5 — Instructor Notes: Corrosion, Galvanic Cells & Rust Removal Deep Dive

**Audience:** instructors and TAs only. Pair with [lecture.md](lecture.md) and [experiment.md](experiment.md).

---

## Why this session exists

This is the synthesis day. Students reconnect Session 1 (spontaneous galvanic cells) to real-world corrosion, see sacrificial protection, and open overnight electrolytic rust-removal cells started in Session 4. Your job: make **activity series**, **galvanic couples**, and **driven vs spontaneous** feel like one coherent story — not three demos.

---

## Atomic foundations of corrosion

### What rust is

Iron metal oxidizes in the presence of water and oxygen. A simplified teaching sequence:

```
Fe(s) → Fe²⁺(aq) + 2e⁻          (anodic dissolution)
O₂ + 2H₂O + 4e⁻ → 4OH⁻         (cathodic oxygen reduction, common in neutral water)
```

Fe²⁺ further oxidizes and precipitates as hydrated oxides / oxyhydroxides — the red-brown **rust** students recognize (Fe₂O₃·nH₂O / FeOOH family). Exact mineralogy is complex; students need: *rust is oxidized iron, not dirt sitting on iron.*

### Valence electrons and why iron corrodes

Iron (Z = 26) readily loses valence electrons to form Fe²⁺/Fe³⁺. In the activity series, Fe sits **above** Cu and **below** Zn:

```
Mg > Al > Zn > Fe > Sn > Pb > (H) > Cu > Ag > Au
```

**Consequences you must own:**

- Fe + Cu in saltwater → Fe becomes anode → **faster rust**
- Fe + Zn in saltwater → Zn becomes anode → **Fe protected** (galvanizing logic)
- Pure Fe still rusts alone (local anodes/cathodes on the same piece from impurities, stress, O₂ gradients)

---

## Electrochemical series — instructor reference table

Approximate standard reduction potentials (acidic, vs SHE):

| Half-reaction | E° (V) | Implication |
|---------------|--------|-------------|
| Mg²⁺ + 2e⁻ → Mg | −2.37 | Very active; strong sacrificial candidate |
| Al³⁺ + 3e⁻ → Al | −1.66 | Active but often passive (oxide film) |
| Zn²⁺ + 2e⁻ → Zn | −0.76 | Classic sacrificial anode / galvanizing |
| Fe²⁺ + 2e⁻ → Fe | −0.44 | Rusts readily when coupled to Cu |
| 2H⁺ + 2e⁻ → H₂ | 0.00 | Reference |
| Cu²⁺ + 2e⁻ → Cu | +0.34 | Noble relative to Fe; accelerates Fe corrosion when coupled |
| Ag⁺ + e⁻ → Ag | +0.80 | Even more noble |
| O₂ + 4H⁺ + 4e⁻ → 2H₂O | +1.23 | Key cathodic reaction in wet corrosion |

**Teaching rule of thumb:** the metal with the **more negative** reduction potential tends to oxidize when two metals are coupled in an electrolyte.

---

## Galvanic cells revisited (metal-pair lab)

### What students measure

Two dissimilar metals in saltwater + multimeter ≈ a crude galvanic cell:

- More active metal → anode (corrodes)
- Less active → cathode (protected)
- Voltage polarity tells you which way electrons want to flow

### Expected qualitative voltages (order of magnitude)

| Pair | Typical open-circuit trend |
|------|----------------------------|
| Zn–Cu | Highest of common set (~1 V class) |
| Al–Cu | Can be high, but Al oxide may suppress |
| Fe–Cu | Medium |
| Zn–Fe | Smaller than Zn–Cu |

Do not grade students on matching textbook E° exactly — saltwater concentrations, surface films, and area ratios dominate.

### Saltwater role

NaCl solution:

- Provides ions for conduction
- Chloride promotes breakdown of passive films (especially relevant to real-world pitting)
- **Reminder:** saltwater is OK for corrosion demos; still **forbidden** for Session 4-style water electrolysis / derusting electrolytes

---

## Corrosion jars A / B / C — narrative

| Jar | Setup | What students should see | Story |
|-----|-------|-------------------------|-------|
| A | Fe alone | Gradual rust | Local cells on one metal |
| B | Fe + Cu touching | **Faster** Fe rust | Galvanic couple; Fe anode, Cu cathode |
| C | Fe + Zn touching | Fe cleaner; Zn suffers | Sacrificial anode |

**Ship / water-heater analogy:** zinc or magnesium blocks bolted to steel hulls / heaters are Jar C at engineering scale.

### Why “touching” matters

Galvanic corrosion requires:

1. Electrical contact between metals (electron path)
2. Shared electrolyte (ion path)

If metals are insulated from each other, the couple does not form.

---

## Electrolytic rust removal — deep dive

### Polarity (repeat until automatic)

| Piece | Battery terminal | Role |
|-------|------------------|------|
| Rusty object | **−** cathode | Reduction / cleaning |
| Sacrificial steel or graphite | **+** anode | Oxidizes / may sludge |
| Electrolyte | Washing soda (Na₂CO₃) or baking soda | Alkaline, **no chloride** |

### Why not NaCl

Chloride + anode can produce chlorine and aggressive pitting chemistry. Same rule as Session 4.

### What “cleaning” means chemically

At the cathode, electrochemical reduction and vigorous local chemistry disrupt oxide layers; hydrogen evolution often helps lift rust. The object does not become “new steel” by magic — loosely bound oxides fall away; residual films may need brushing/rinsing. Results vary with rust thickness and overnight time.

### Link to jars

| Process | Iron’s role | Energy |
|---------|-------------|--------|
| Jar B galvanic corrosion | Anode (oxidizes) | Spontaneous |
| Electrolytic derusting | Cathode (reduced) | Driven by battery |

This contrast is the intellectual climax of the week.

### Reveal protocol (Session 5 opening)

1. Disconnect power.
2. Remove nails; rinse.
3. Compare to control and before photo.
4. Ask: which electrode was cathode? How is this like Session 4? How is it opposite of Jar B?

---

## Sacrificial protection — mechanisms students can own

1. **Galvanizing:** zinc coating on steel. Zinc corrodes preferentially; even if scratched, Zn can still protect nearby steel electrochemically (within electrolyte contact).
2. **Impressed current / electrolytic protection:** external power forces structure to be cathodic (related idea to derusting polarity).
3. **Paint / barriers:** not electrochemical, but prevent electrolyte/O₂ access — mention as complementary.

---

## Fuel cells — optional concept only

If asked:

```
Electrolysis:  electricity + H₂O → H₂ + O₂
Fuel cell:     H₂ + O₂ → electricity + H₂O
```

Same chemistry, opposite energy direction. No PEM kit required this week. Emphasize efficiency losses and “energy carrier” language from Session 4.

---

## Week synthesis — how to run the final challenge

Have the answer key ready ([lecture.md](lecture.md)). Push students to use vocabulary:

- Galvanic vs electrolytic
- Anode / cathode
- Oxidation / reduction
- Electron path vs ion path

Strong closing: every session was about **where electrons go and why**.

---

## Misconceptions

| Misconception | Correction |
|---------------|------------|
| “Rust is a coating that sits on iron.” | Rust is **iron that has already oxidized**. |
| “Copper makes iron rust by touching it chemically like paint.” | Copper makes iron the **anode** in a galvanic couple. |
| “Zinc coating just seals the steel.” | Sealing helps, but Zn also **sacrifices** electrochemically. |
| “Derusting means the battery dissolves rust into nothing.” | Electrochemistry + rinsing removes / reduces oxide; sludge remains in bath. |
| “Salt is always the best electrolyte.” | Great for corrosion demos; dangerous for Cl₂-producing electrolysis. |

---

## Board plan

1. Reveal derusted vs control nails (visual hook).
2. Activity series arrow; place Zn, Fe, Cu.
3. Draw jars A/B/C with anode labels.
4. Contrast galvanic rusting vs electrolytic cleaning table.
5. Final challenge worksheet → closing message.

---

## Optional enrichment

- Crevice corrosion and differential aeration (why nails rust under washers).
- Stainless steel passivation (Cr₂O₃ film) — why “stainless” is not magic.
- Cathodic protection standards in marine engineering (names only).
- Pourbaix diagram for Fe (advanced TA interest).
