---
type: Concept
title: "L01 Plan — Why Model a Cell?"
description: Backwards-design plan for the first lecture — outcomes, assessment evidence, then the two-hour sequence.
tags: [course, lecture-plan, L01]
sources:
  - id: wiki-l01
    resource: /index.md
    title: "Wiki pages tagged teaching.lecture: L01"
generated:
  by: claude-opus-5
  at: 2026-09-09
status: draft
teaching:
  lecture: L01
  role: reference
outcomes:
  - "State what makes a model *dynamic*, and what a dynamic model commits you to."
  - "Give one example where verbal reasoning about a network gives the wrong answer."
  - "Distinguish a model used for prediction from one used for explanation."
duration: "2 hours"
draws_on:
  - systems-biology
  - synthetic-biology
  - complex-system
  - feedback
  - dynamic-mathematical-model
  - interaction-diagram
  - simulation-versus-analysis
  - deterministic-and-stochastic-models
  - saturation
  - case-trypanosoma-glycolysis
  - case-nf-kb-oscillation
  - case-collins-toggle-switch
  - case-hodgkin-huxley
---

# L01 Plan — Why Model a Cell?

Designed backwards (Wiggins & McTighe): outcomes first, then the evidence that would show the
outcomes were met, then the activities. Written before `notes.md` and `slides.md`.

**The job of this lecture.** Not to teach modelling. To make the rest of the course feel
*necessary* rather than imposed — because a student who thinks equations are optional decoration
will treat L03 onward as arbitrary algebra.

---

## Stage 1 — Desired results

### Enduring understandings

1. **The behaviour of a network does not follow from the behaviour of its parts.** Knowing what
   every component does is not sufficient to predict what the assembly does. This is a structural
   claim, not a complaint about difficulty.
2. **A cartoon diagram is ambiguous about behaviour, especially where there is feedback** — and the
   ambiguity is removed only by supplying a number for every interaction.
3. **A model is a hypothesis whose consequences can be computed**, so a model that fails falsifies
   the biology it was built on. That is what makes modelling worth the effort.

### Essential questions

These recur through the whole course, and students' answers should get better each time:

1. *"You know exactly what every part does. Can you predict what the system does?"*
   (L01 answer: no, when there is feedback. L04 answer: yes, if you write and solve the equations.)
2. *"What would have to happen for you to abandon this model?"*
   (L01: they usually cannot answer. By L05 they can name the assumption that would break.)
3. *"Is this model wrong, or just not useful here?"*
   (The distinction most students have never been offered.)

### Students will know

- What "systems biology" claims, as distinct from "biology done with computers"
- The vocabulary of an interaction diagram: solid vs dashed, plain vs blunt-ended arrow
- **System** = interacting components + a boundary; **complex** = qualitative behaviour depending
  on quantitative structure
- Negative feedback stabilises **unless lagged**; positive feedback diverges **unless saturated**
- Mechanistic vs descriptive models; simulation (*how*) vs analysis (*why*)
- Why this course is deterministic, and the molecule-count condition under which that is fair

### Students will be able to

- Read an interaction diagram and say what it does *not* tell them
- Trace a feedback loop and determine its sign
- Given a published modelling study, say what the model was *for*: prediction, explanation, or
  design

---

## Stage 2 — Assessment evidence

### Performance task — "Two negatives"

> Here is a two-gene circuit. Gene 1's protein represses Gene 2. Gene 2's protein represses Gene 1.
> Nothing else is specified.
>
> **(a)** Trace the loop and state its overall sign. Justify in one sentence.
> **(b)** A colleague says: "Obviously this is a switch — it will sit in one of two states." Under
> what circumstances are they right, and under what circumstances is the circuit useless? You may
> not use any equations.
> **(c)** What is the smallest piece of *quantitative* information you would ask for to settle it?

*Assesses:* Understanding 1 (parts vs whole), Understanding 2 (the diagram is not enough),
Essential Question 1. It requires **transfer** — the toggle switch is covered in the lecture, but
part (b) demands reasoning about the asymmetric case, and part (c) asks them to identify the missing
information rather than recall an answer.

*Success criteria:*
- Identifies the loop as **positive** (two negatives compose to a positive), with the composition
  argument, not by assertion
- States that a switch requires the mutual repression to be *balanced enough* and *nonlinear
  enough*
- Names a genuinely quantitative gap — relative repression strengths, expression rates, or the
  steepness of the repression response
- Does **not** claim the diagram alone settles it

### Other evidence

| When | Instrument | Outcome assessed |
|---|---|---|
| Minute 20 | Cold call on Figure 1.1: *"What happens to D if I double B?"* Collect three answers, do not resolve. | Understanding 2 — and the disagreement *is* the evidence |
| Minute 55 | **Hinge question** (below) on mini-whiteboards | Understanding 1, feedback signs |
| Minute 95 | Exit ticket: *"Name one thing modelling bought in one of today's four case studies, in one sentence."* | Skill: identifying a model's purpose |
| Before L02 | Three retrieval questions, posted after class | Retention into L02 |

### The hinge question

Placed after [[feedback]], before the case studies. Every wrong answer diagnoses a different thing.

> A signalling pathway has a single negative feedback loop and no other regulation. Its output
> **oscillates** for hours. What is the most likely explanation?
>
> **A.** The feedback is actually positive — someone drew the diagram wrong.
> **B.** There is a **delay** in the feedback.
> **C.** Negative feedback always oscillates; this is normal.
> **D.** There must be a second, hidden loop.

**B is correct.** And the wrong answers are the useful part:

- **A** — believes negative feedback *cannot* oscillate, so an oscillation must mean a drawing
  error. The rule has been learned as an absolute.
- **C** — has over-corrected from the lecture and lost the default case. Negative feedback usually
  *does* stabilise.
- **D** — reasonable and shows systems thinking, but reaches for extra machinery before exhausting
  what the given loop can do. Worth praising, then redirecting.

If more than a third pick A, do not move on. Go back to the hallway thermostat.

---

## Stage 3 — Learning plan (120 minutes)

Following WHERETO. Timings are targets, not a script.

### 0–10 · **W** + **H** — Where we are going, and the hook

Open with the Lewis Thomas epigraph on a slide, read aloud, no commentary. Then the course map in
one slide: six lectures, one question each.

**Hook:** *"You know exactly what every component of a thermostat does. Can you predict the
temperature of the room?"* Everyone says yes. Then: *"The thermostat is in the hallway. The heater
is upstairs."* Sit with the silence.

### 10–25 · **E** — What systems biology actually claims

[[systems-biology]]. The historical arc — reductionism forced by instruments, high-throughput
methods around 2000, the genome draft. Two boxes on the board: "what each part does" and "what the
network does". Ask what bridges them. Accept "adding up" and hold it.

Engineering analogy **with its limit stated** — selection is not design.

### 25–40 · **E** — The cartoon and its ambiguity

[[interaction-diagram]]. Figure 1.1 on the board with full notation: solid vs dashed, plain vs
blunt.

**Cold call:** *"What happens to D if I double B?"* Take three answers. **Do not resolve them.**
> "None of you can be shown wrong from this picture. That is the problem we are going to fix."

This is the emotional centre of the lecture. Do not rush it.

### 40–55 · **E** — Complexity and feedback

[[complex-system]]: system = components + boundary; Kelly's avalanche; complex ≠ complicated.
Then [[feedback]], and specifically **the exceptions**, which are the material:

| The rule | When it fails |
|---|---|
| Negative feedback stabilises | With a **lag** → oscillation |
| Positive feedback explodes | With **[[saturation]]** → latching, i.e. memory |

Draw the hallway-thermostat temperature trace *with* the room. They will draw an oscillation
unprompted.

### 55–65 · **E** (evaluate) — Hinge question + break

Mini-whiteboards. Do not proceed until it lands. Then a ten-minute break.

### 65–75 · **E** — What a model is, and what it buys

[[dynamic-mathematical-model]]: abstraction, the price (a number for every interaction),
mechanistic vs descriptive, and the four returns — audit, communication, working hypothesis,
falsification.

[[simulation-versus-analysis]] in ninety seconds: *how* versus *why*. Promise L04.

### 75–105 · **E** — Four case studies, four different uses

Thirty minutes, seven or eight each. The point is not the biology; it is that **each shows a
different use of a model**. Say that before starting and put the four-row table up.

1. [[case-trypanosoma-glycolysis]] — **finds** something: five good drug targets, and three
   believed-good ones ruled out. Ask what the negative result was worth.
2. [[case-nf-kb-oscillation]] — **explains** something: why three inhibitor isoforms, not one.
   Callback to the lagged negative loop.
3. [[case-collins-toggle-switch]] — **designs** something, before construction. Trace the loop
   aloud and let the room hear that two negatives make a positive. This is the performance task's
   setup.
4. [[case-hodgkin-huxley]] — **proves sufficiency**: a 3% stronger stimulus, a categorically
   different response. Show the two stimuli and ask them to predict before revealing.

### 105–115 · **R** + **E** — Rethink, and the honest boundary

[[deterministic-and-stochastic-models]] briefly: this course is deterministic, here is the
molecule-count condition, here is where it fails and where the book handles it (§7.6). Students
should know what is being left out, not discover it later.

Return to Essential Question 1. Compare with their answer at minute 5.

### 115–120 · **O** — Set up L02 and issue the task

Preview: *"Next week we take the derivative apart, because everything after that is a statement
about a rate."* Issue the performance task; due before L03.

---

## Tailoring

- **Weak calculus background.** Nothing in L01 requires it. Say so out loud — some students arrive
  braced for an ordeal and stop listening.
- **Strong mathematical students.** Extension: *"§1.6.3 says bistability fails if expression rates
  are too low, even in the symmetric case. Why might that be?"* No answer expected; it is a hook
  into Ch. 4.
- **Language.** Slides and notes are English. The technical terms that carry the lecture —
  *feedback*, *steady state*, *saturation*, *bistable* — should be written on the board and left
  there.

---

## Alignment check

| Stage 1 outcome | Assessed in Stage 2 | Taught in Stage 3 | ✓ |
|---|---|---|---|
| U1 — parts do not determine the whole | Performance task (a),(b); hinge question | 10–25, 40–55, case studies | ✓ |
| U2 — cartoons are ambiguous | Performance task (b),(c); minute-20 cold call | 25–40 | ✓ |
| U3 — a model is a falsifiable hypothesis | Exit ticket; Essential Question 2 | 65–75, case studies | ✓ |
| K — systems / complex / feedback vocabulary | Hinge question; performance task (a) | 10–55 | ✓ |
| K — deterministic assumption and its limit | *(not assessed)* | 105–115 | ⚠ |
| S — read a diagram for what it omits | Performance task (c) | 25–40 | ✓ |
| S — trace a loop's sign | Performance task (a) | 40–55, toggle switch | ✓ |
| S — identify a model's purpose | Exit ticket | 75–105 | ✓ |

**One deliberate gap.** The deterministic/stochastic distinction is taught but not assessed. It is
orientation — students need to know what the course excludes — and testing it would reward
memorising a boundary rather than understanding the material inside it. Flagged rather than hidden.

## Sources

Built from the wiki pages listed in `draws_on`, all of which trace to
[[ingalls-ch01-introduction]]. Design framework: Wiggins & McTighe, *Understanding by Design*;
constructive alignment per Biggs & Tang.
