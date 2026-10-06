---
type: Concept
title: "L06 Plan — Enzyme Kinetics II"
description: Backwards-design plan for the sixth lecture (Kinematika Enzim II) — competitive and non-competitive inhibition, allosteric regulation and cooperativity, Hill functions as regulation models, and sigmoidal kinetics as soft switches.
tags: [course, lecture-plan, L06]
sources:
  - id: wiki-l06
    resource: /index.md
    title: "Wiki pages tagged teaching.lecture: L06"
generated:
  by: claude-opus-5
  at: 2026-09-16
status: draft
teaching:
  lecture: L06
  role: reference
outcomes:
  - "Derive the competitive-inhibition rate law, state what competitive and non-competitive inhibitors do to Vmax and KM, and identify the mechanism from a pair of measurements."
  - "Explain why independent sites give a hyperbola, derive the Hill function from simultaneous binding, and state what the Hill coefficient does and does not measure."
  - "Write Hill-type rate laws for cooperatively binding competitive and non-competitive inhibitors and say how substrate moves the half-inhibiting dose in each."
  - "Explain why a sigmoidal response is a soft switch, quantify its sharpness (10–90% span, kinetic order n(1−Y)), and state what it cannot do without feedback."
duration: "2 hours"
draws_on:
  - competitive-inhibition
  - allosteric-regulation
  - cooperativity
  - hill-function
  - hill-type-regulation
  - switch-like-response
  - kinetic-order
  - case-collins-toggle-switch
notes: [notes.md, notes.id.md]      # English and Bahasa Indonesia; keep the pair in step
practical: "TKBM262615_Practicals/notebooks/05_regulation_and_switches.ipynb"   # planned
replaces: "L06-regulation-cooperativity-and-transport (2026-09-09), re-scoped on 2026-09-16"
---

# L06 Plan — Enzyme Kinetics II (Kinematika Enzim II)

**Topics, as set in the course plan (RPS):** competitive and non-competitive inhibition; allosteric
and cooperative regulation; the Hill function as a model of regulation (competitive and
non-competitive); sigmoidal kinetics as "soft switches".

**Scope note.** The earlier L06 also covered compartments, diffusion and transport (Ingalls §3.4).
Those are not in the RPS for this meeting and have been dropped; the wiki pages remain, untagged
from this lecture, and the question of where they go is in `QUESTIONS.md`. The time freed goes to
two things the earlier version lacked: a full derivation of competitive inhibition in class, and
the last two RPS topics, which need their own teaching blocks.

**Two honest additions.** (1) The Hill-type inhibition laws are derived here by combining §3.2 with
Exercise 3.3.3; Ingalls does not print them, and the notes say so. (2) Solving the QSSA for the
non-competitive square exactly does not give Ingalls' (3.15) unless $k_2 \ll k_{-1}$; the notes
derive (3.15) under an explicit binding-equilibrium assumption and show the numerical check. The
lecture should mention this in one sentence and not dwell on it.

## Stage 1 — Desired results

### Enduring understandings

1. **An inhibitor's mechanism is visible in which constant it moves.** The same factor
   $(1 + i/K_i)$ multiplies $K_M$ in one law and divides $V_{max}$ in the other. Competition can be
   won with substrate; allosteric inhibition cannot.
2. **A sigmoid comes from interaction, not from multiplicity.** Independent sites give a hyperbola.
   The Hill coefficient measures steepness, not a count of sites.
3. **A Hill factor is a regulation module and a soft switch.** It multiplies an ordinary rate law,
   amplifies relative changes by up to $n$, and responds to the present input only. Memory needs
   feedback.

### Essential questions

1. *"How would you turn a reaction down, fast?"* (Block the enzyme, two ways.)
2. *"Why isn't a four-site protein automatically sigmoidal?"* (Independent sites fill like one.)
3. *"If a sigmoid is a switch, does it remember which way it was flipped?"* (No.)

### Students will know

- The competitive scheme and its three-term conservation; $K_i = k_{-3}/k_3$
- $v = \frac{V_{max}s}{K_M(1 + i/K_i) + s}$ and $v = \frac{V_{max}}{1 + i/K_i}\frac{s}{K_M + s}$,
  and the fingerprint table
- What allostery is and why it removes the resemblance constraint (Jacob and Monod, 1961)
- Haemoglobin against myoglobin; fractional saturation; the two-site Adair form
- The Hill function, its derivation from simultaneous binding, and Hill's own $n$ = 1 to 3.2
- Hill-type inhibition laws; $i_{50} = K_i(1 + s/K_M)^{1/n}$ (competitive) and $i_{50} = K_i$
  (non-competitive)
- Kinetic order $n(1 - Y)$; the 10–90% span $9^{2/n}$; slope $n/4K$
- The three properties of a soft switch: graded, reversible along the same path, memoryless

### Students will be able to

- Derive the competitive law in five steps
- Diagnose an inhibitor from $(V_{max}, K_M)$ with and without it, and compute $i/K_i$
- Derive (3.19) from $P + nX \rightleftharpoons PX_n$
- Compute a 10–90% span, a kinetic order, and an $i_{50}$
- Explain, with a simulation, the difference between lag and memory

## Stage 2 — Assessment evidence

### Performance task — the six-rung problem set (in the notes, with answers)

1. Reproduce the competitive derivation.
2. Diagnose three drugs from $(V_{max}, K_M)$; the third one is uncompetitive and fits neither
   mechanism from class.
3. Derive uncompetitive inhibition (Ingalls Exercise 3.2.2) independently; it explains drug C.
4. Minimum Hill coefficient for a three-fold 10–90% span ($n = 4$); why independent sites fail.
5. $i_{50}$ for a cooperative against a non-cooperative competitive inhibitor.
6. Open computational: lag or memory? Design the test.

This closes the fading sequence begun in L05: Michaelis-Menten worked, competitive guided,
uncompetitive independent.

*Success criteria:* rung 2 answered from the rate laws, not from memory; rung 3 notices that the
last two terms of the $C$ equation cancel; rung 6 proposes holding the input fixed from both
directions.

### Other evidence

| When | Instrument | Outcome assessed |
|---|---|---|
| 0–8 | Retrieval: 3 questions on L05 | L05 retention; $V_{max}$ against $K_M$ |
| Minute 12 | Brainstorm (essential question 1) | Hook |
| Minute 45 | **Hinge question**: $V_{max}$ unchanged, $K_M$ tripled | Outcome 1 |
| Minute 58 | Cold call (essential question 2) | Outcome 2 |
| Minute 85 | Mini-whiteboard: $i_{50}$ at $s = 10K_M$ for $n = 1$ and $n = 4$ | Outcome 3 |
| Minute 108 | Cold call (essential question 3), with the ramp figure | Outcome 4 |
| Minute 118 | Exit ticket: *"Name one thing a sigmoid can do that a hyperbola cannot, and one thing it still cannot do."* | Outcomes 2, 4 |

### The hinge question

> $V_{max}$ unchanged, $K_M$ tripled. A: non-competitive. B: competitive. C: cooperative (Hill).
> D: cannot tell without structure.

**B.** A swaps the fingerprints. C confuses curve shape with a shift. D ignores that the two laws
answer it from the numbers. Follow-up for quick rooms: what is $i/K_i$? (2.)

## Stage 3 — Learning plan (120 minutes)

### 0–10 · Retrieval and hook
Three L05 questions. Then the brainstorm: ways to slow a reaction. Sort the answers into slow
(genetic) and fast (a molecule binds the enzyme).

### 10–35 · Part 1, competitive inhibition
Ibuprofen and cyclooxygenase. Scheme. Derive live in five steps, with the room supplying each
QSSA. Units check and the $i = 0$ check. Table at $s = 0.5$ and $s = 50$. "Enough substrate always
wins."

### 35–50 · Part 2, allostery and non-competitive inhibition
The resemblance constraint and how allostery removes it. The square scheme; point at the repeated
rate constants as the meaning of independent binding. Present (3.15) with the equilibrium
assumption stated; one sentence on the exactness caveat. The mirror image, circling the factor.
The inhibition figure. **Hinge question**, then break.

### 50–75 · Part 3, cooperativity and the Hill function
Haemoglobin against myoglobin as an argument. Fractional saturation. The surprise: independent
sites stay hyperbolic (cold call). Adair for two sites, shown not derived. Hill from simultaneous
binding in three lines. $K$ and $n$; Hill's own fits of 1 to 3.2; the warning.

### 75–92 · Part 4, Hill functions as regulation
Replace $i/K_i$ by $(i/K_i)^n$ in both laws; the factor as a decreasing Hill function and a module.
Derive $i_{50}$ for the competitive case on the board. Mini-whiteboards: predict $i_{50}$ at
$s = 10K_M$ for $n = 1$ and $n = 4$ before showing the table and figure. One slide on the activator
(Problem 3.7.8).

### 92–112 · Part 5, soft switches
Kinetic order from L05's reading, extended to $n(1 - Y)$ with the quotient rule. The 10–90% table.
Haemoglobin's five-fold window and the figure. Then "soft": graded, reversible, memoryless, shown
with the ramp model. Cold call (essential question 3). The L01 toggle switch as the contrast:
feedback supplies memory.

### 112–120 · Close
One technique, five rate laws. Problem set and practical. Exit ticket.

## Tailoring

- **If time runs short,** show the activator slide as reading only, and present the Adair form in
  one sentence. Do not cut the soft-switch block; it is an RPS topic in its own right.
- **If the room is quick,** run `soft_switch.py` live with a 10-unit ramp and let them argue whether
  the gap is memory before rung 6.
- **Language.** *Competitive*, *allosteric*, *cooperativity*, *Hill coefficient*, *switch-like*
  stay in English on the board, with the Indonesian gloss beside them.

## Alignment check

| Outcome | Assessed | Taught | ✓ |
|---|---|---|---|
| 1 Inhibition | hinge; rungs 1–3 | 10–50 | ✓ |
| 2 Cooperativity and Hill | minute-58 cold call; rung 4; exit ticket | 50–75 | ✓ |
| 3 Hill regulation | minute-85 whiteboards; rung 5 | 75–92 | ✓ |
| 4 Soft switches | minute-108 cold call; rung 6; exit ticket | 92–112 | ✓ |

## Sources

Built from the wiki pages in `draws_on`, which trace to [[ingalls-ch03-biochemical-kinetics]]
§3.2–§3.3 (Figures 3.5–3.10; equations 3.13–3.19; Exercises 3.2.1–3.3.4; Problems 3.7.8, 3.7.9) and
to Ingalls §1.6.3 for the toggle switch. Design framework: Wiggins and McTighe, *Understanding by
Design*; fading per Renkl and Atkinson.
