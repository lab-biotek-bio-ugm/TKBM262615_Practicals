---
type: Concept
title: "L04 Plan — Conservation and Numerical Simulation"
description: Backwards-design plan for the fourth lecture — mass conservation in closed systems, using a conservation to shrink a model exactly, Euler's method, and solving ODEs in Python.
tags: [course, lecture-plan, L04]
sources:
  - id: wiki-l04
    resource: /index.md
    title: "Wiki pages tagged teaching.lecture: L04"
generated:
  by: claude-opus-5
  at: 2026-09-09
status: draft
teaching:
  lecture: L04
  role: reference
outcomes:
  - "State what a conservation relation is, find one in a small closed network by two routes, and say why it holds for every value of the rate constants."
  - "Use a conservation to eliminate one differential equation exactly, and find the resulting steady state algebraically."
  - "Derive Euler's method from the definition of the derivative, take three steps by hand, and say where the error comes from and how it scales with the step size."
  - "Integrate a reaction-network model with scipy's solve_ivp, setting tolerances deliberately, and say what a simulation cannot tell you that a formula can."
duration: "2 hours"
draws_on:
  - conservation-relation
  - nullspace
  - steady-state
  - numerical-simulation
  - simulation-versus-analysis
notes: [notes.md, notes.id.md]      # English and Bahasa Indonesia; keep the pair in step
practical: "TKBM262615_Practicals/notebooks/03_conservation_and_numerics.ipynb"
---

# L04 Plan — Conservation and Numerical Simulation

Designed backwards.

**Scope note, and it is a deliberate re-cut.** An earlier version of this lecture carried steady
states, separation of time-scales, rapid equilibrium and the quasi-steady-state approximation as
well as the numerical material. That was the densest lecture in the course by a wide margin, and
it front-loaded three model-reduction techniques before the students had met a single model that
needed one. This version keeps the two things L04 is actually for — the one reduction that is
*exact*, and the numerics that let you run a model you cannot solve — and hands the approximate
reductions to L05, where the enzyme mechanism supplies a reason to want them.

The trade is worth naming because it is also pedagogically load-bearing: **conservation first,
approximation second.** A student who has seen an exact reduction, and been told plainly that it
is exact, has something to compare against when L05's quasi-steady-state approximation arrives
looking identical on the page and behaving differently. Teaching them in the other order, or in
the same lecture, blurs exactly the distinction that matters.

[[numerical-simulation]] stays here rather than in L02, for the reason the L02 plan already
flagged: it needs a model built from a real network to run on, and the question "how does the
solver you have been calling since L01 actually work" only lands once you have written the
equations yourself.

## Stage 1 — Desired results

### Enduring understandings

1. **A conservation is a property of the network's structure, not of its parameters.** It holds
   for every choice of rate constants, because it follows from which arrows exist. This is the
   seed of everything Ch. 5 does with metabolic network structure, and it is the reason a
   conservation can be trusted in a model whose constants are unmeasured.
2. **Reducing a model with a conservation is rewriting, not approximating.** Two differential
   equations become one differential equation plus one line of arithmetic, and the reduced model
   is the same model. Nothing is lost. Say the word *exact* and mean it, because L05 will present
   a reduction that looks the same and is a bet.
3. **A numerical solution is a finite list of approximate points, not a formula and not the
   solution.** Its accuracy is something you chose, whether or not you thought about choosing it.

### Essential questions

1. *"Does this conservation depend on the value of $k$?"* (No. It holds for every $k$ — which is
   what "structural" means, and what makes it worth finding.)
2. *"$A \to B$ conserves $a + b$. Does it conserve mass?"* (Only if A and B have the same
   molecular mass, which they need not. The conserved thing is a count.)
3. *"I halved my step size and the answer changed. Which one is right?"* (Neither, necessarily —
   but the size of the change tells you the size of the error, and if halving again barely moves
   it, you have converged.)

### Students will know

- A closed network has at least one conservation relation, findable either by inspecting the
  arrows or by adding the differential equations and watching the terms cancel
- Conservation of concentration is conservation of a molecule count, which may or may not be
  conservation of mass; the biological case is usually **moiety** conservation
- A conservation is not always a sum — Exercise 2.1.8 has one that is a difference
- Substituting $b = T - a$ removes one equation exactly, and the steady state of what remains
  follows by setting the derivative to zero
- In a network too big to eyeball, conservations are the **left nullspace** of the stoichiometry
  matrix: $\mathbf{w}^T\mathbf{N} = 0$
- Euler's method, $a(t+h) = a(t) + hf(a(t))$, comes directly from the derivative's definition, and
  its error halves when $h$ halves — first order, and a bad deal
- `solve_ivp` is Euler's idea done far better, with adaptive higher-order steps, and it still has
  settings worth understanding rather than accepting

### Students will be able to

- Find the conservation in a small closed network by both routes and check that the two agree
- Use it to reduce a two-species model to one equation and solve for the steady state
- Compute `null_space(N.T)` for a small stoichiometry matrix and read the answer as a combination
- Take three Euler steps by hand on a one-variable model and compare against the exact solution
- Call `solve_ivp` with explicit `args`, `dense_output` and tolerances, and say what each does
- Print a conservation check alongside a simulation, as a habit

---

## Stage 2 — Assessment evidence

### Performance task — a fading sequence, due before L05

Three problems on the same technique with decreasing scaffolding, following Renkl and Atkinson.
Problems 1 and 2 are also the spine of the week's Colab notebook, so the lecture, the practical
and the problem set are one artefact rather than three.

**Level 1 — worked in `notes.md`, reproduce from memory.** The closed pair
$A \rightleftharpoons B$: find the conservation by both routes, use it to reduce the system to
equation (2.12), and derive the steady state (2.13). Check that $a^{ss} + b^{ss} = T$.

**Level 2 — partially faded.** The three-step chain $A \to B \to C$. The conservation is stated;
derive it by the second route, use it to eliminate $C$, and simulate the reduced and full systems
in Python. Print the conservation check at every time point rather than only at the ends, and say
what tolerance you had to set for the two integrations to agree to four decimal places, and why
they do not agree at the default.

**Level 3 — fully independent.** A closed network whose conservation is a **difference**, not a
sum (Ingalls Exercise 2.1.8). No hint that the pattern has changed. Find the conservation, state
whether it is a moiety conservation and why, reduce the model, and confirm numerically. Then take
the same system and integrate it with a hand-written Euler loop at three step sizes, reporting
whether the conservation survives Euler as exactly as it survives `solve_ivp` — and explaining the
answer.

*Assesses:* Understanding 1 at every level, Understanding 2 at Levels 1–2, Understanding 3 at
Level 3.

*Success criteria:*
- Level 1: both routes shown, arriving at the same $T$; the sum check stated as a *requirement*,
  not an observation.
- Level 2: correct elimination; the tolerance question answered in terms of `rtol`, not blamed on
  a bug in either integration.
- Level 3: recognises that the combination is a difference before being told; the Euler question
  answered correctly — the conservation survives Euler exactly too, because Euler adds the same
  quantity to one species that it subtracts from the other at every step, and that is a property
  of the update formula rather than of the accuracy. Students who answer "no, because Euler is
  less accurate" have confused two different things, which is the point of the question.

### Other evidence

| When | Instrument | Outcome assessed |
|---|---|---|
| 0–10 | Retrieval: 3 questions on L03, posted after L03 | Retention into L04 |
| Minute 25 | Cold call (essential question 2): does $A \to B$ conserve mass? | Understanding 1, the misconception |
| Minute 30 | Cold call (essential question 1): does it depend on $k$? | Understanding 1 |
| Minute 50 | **Hinge question** (below) on mini-whiteboards | Understandings 1 and 2 together |
| Minute 95 | Cold call (essential question 3): I halved $h$ and the answer changed | Understanding 3 |
| Minute 120 | Exit ticket: *"Name one thing a simulation cannot tell you that a formula can."* | Understanding 3, transfer |

### The hinge question

Placed at the end of Part 2, after the reduction and the steady state, before the numerics.

> The closed network $A \rightleftharpoons B$ starts at $a(0) = 3$, $b(0) = 1$ mM. Someone doubles
> **both** $k_+$ and $k_-$. Which statement is true of the new steady state?
>
> **A.** $T$ changes, $a^{ss}$ does not.
> **B.** Neither $T$ nor $a^{ss}$ changes.
> **C.** $T$ holds, but $a^{ss}$ changes.
> **D.** Both change.

**B is correct**, and it tests both of the lecture's first two understandings in one question.

- **A** — thinks rate constants can move the conserved total. They cannot: $T = A_0 + B_0$ is set
  by the initial condition, and the constants cancelled out of the derivation entirely.
- **C** — the most instructive wrong answer, and the most popular. It gets the structural half
  right and then assumes that changing a parameter must change the answer. Work the algebra on the
  board: $a^{ss} = k_-T/(k_+ + k_-)$, double top and bottom, and watch the factor of two cancel.
  Only the *ratio* matters — the same fact the practical notebook's Example IV demonstrates
  numerically.
- **D** — both errors at once.

If more than a third pick C, do the doubling algebra live and re-ask before moving on. Break
immediately after.

---

## Stage 3 — Learning plan (120 minutes)

### 0–10 · Retrieval + hook

Three retrieval questions on L03 (posted after that lecture): why the rate for $A + B$ is a
product; how many equations a five-species, three-reaction network has; the units of a
second-order rate constant. Then the hook, and it should be physical rather than symbolic: hold
two markers, one labelled A and one labelled B, convert one in front of the room, ask for the
total. Nothing has changed. That is the whole concept; the rest is notation.

### 10–25 · Conservation in a closed system

[[conservation-relation]]. What *closed* buys you. Route 1, reading it off the arrows. Route 2,
adding the differential equations and watching $-ka + ka$ cancel — done on the board, not shown
finished. Land the point that matters about seeing the same answer arrive twice: it is what makes
the algebraic route believable later, when the chemistry is too complicated to eyeball.

**Cold call (essential question 2):** does $A \to B$ conserve mass? Do not skip this. The
syllabus's own phrase "mass conservation" invites the misreading, so correct it explicitly.

### 25–35 · Structural, not parametric; and what it is called

**Cold call (essential question 1):** does the conservation depend on $k$? Then the vocabulary,
kept short and biological: moiety conservation, phosphate groups, adenine nucleotides, NAD⁺/NADH.
Finish with Exercise 2.1.8's warning that a conservation need not be a sum — one slide, set as
homework rather than developed, because it breaks the pattern students will otherwise generalise.

### 35–50 · Using the conservation

Substitute $b = T - a$ into the reversible pair; two coupled equations become equation (2.12), in
one unknown, of a shape they already solved in L03 and in practical notebook 02. Set the
derivative to zero for (2.13), and say the sum check aloud as a requirement.

One slide of [[steady-state]] as a bridge, no more: $f(\mathbf{x}^{ss}, \mathbf{p}) = 0$ means
every rate of change is zero at once, not that the reactions stopped. This is here because the
hinge question needs it and because L05 needs it; the full treatment belongs to Ch. 4, outside
this course.

### 50–60 · Hinge question, then break

Mini-whiteboards, simultaneous reveal. Do not proceed until it lands. Break after.

### 60–70 · Conservations in networks too big to see

[[nullspace]], finally earning its place. $\mathbf{w}^T\mathbf{N} = 0$ read as a sentence: find
the weightings that no reaction disturbs. Then `null_space(N.T)` in three lines, run live if
possible, with the normalisation answered before it is asked — $[0.707, 0.707]$ means "$a + b$",
because direction is what matters and scale is not.

Close the half with the sentence to bank: **this reduction is exact.** Nothing is approximated;
the reduced model is the same model, written shorter. Say that L05 will show one that looks
identical and is not.

### 70–95 · Euler's method

[[numerical-simulation]]. Say explicitly: "you have called `solve_ivp` three times without knowing
what is inside; today it opens." Derive (2.16) from the definition of the derivative in three
lines on the board, naming out loud the moment the approximation is treated as an equality —
that moment is where all the error comes from and it should be visible. Read the formula as a
sentence before reading it as symbols.

Then hand-compute three Euler steps on $\frac{da}{dt} = -a$, $h = 2/3$: 1, then 1/3, then 1/9,
then 1/27 = 0.037, against the exact $e^{-2} = 0.135$. Give it two minutes; do not rush it. Seeing
their own bad approximation is worth more than any warning.

The figure, then the error table: halving $h$ halves the error, ten times the work for ten times
the accuracy, and `solve_ivp` twelve orders of magnitude better. One minute on Euler's instability
at large $h$ as a property of the method rather than of the biology. Then the `np.arange` mesh bug
as a real bug they will hit, with its subtle symptom.

**Cold call (essential question 3):** I halved my step size and the answer changed.

### 95–115 · Solving ODEs in Python

The whole `solve_ivp` call with nothing hidden, written for $A \rightleftharpoons B$ on the board
together. `rhs(t, y, *args)` — time first, even when the model does not use it. Four settings:
`args` (no globals), `dense_output`, tolerances (the default `rtol=1e-3` is loose enough that two
independent integrations disagree in the fourth decimal), `method` (stiffness as a symptom to
recognise, one sentence, not a topic).

Then [[simulation-versus-analysis]], which deserves the same weight Ingalls gives it: one run is
one initial condition, and a formula shows the parameter dependence a simulation can only be
sampled for. Students who have just learned to call a solver conclude that simulation supersedes
algebra; say the opposite plainly.

### 115–120 · Wrap-up

Three sentences to carry: a conservation is exact, structural and free; reducing with it is
rewriting; a numerical answer's accuracy is something you chose. Issue the fading problem set and
point at practical notebook 03. Preview: *"Next week mass action stops being the right rate law,
and what saves it is an enzyme conservation plus one reduction that, unlike today's, really is a
bet."*

---

## Tailoring

- **If time runs short,** cut the nullspace section (60–70) rather than the hand-computed Euler
  steps. The linear-algebra route is the general method and matters later, but it is recoverable
  from the notes; the hand computation is what makes the error concrete and does not survive being
  read about.
- **If the room is strong on L02's calculus,** Euler's derivation will go quickly. Spend the saved
  time on the mesh bug, which is genuinely subtle and worth watching fail once.
- **Language.** *Conservation relation*, *structural*, *moiety*, *step size*, *tolerance* go on the
  board and stay, same policy as L01–L03.

---

## Alignment check

| Stage 1 outcome | Assessed in Stage 2 | Taught in Stage 3 | ✓ |
|---|---|---|---|
| Find a conservation, two routes; say why it is structural | Minute-25 and minute-30 cold calls; task L1, L3 | 10–35 | ✓ |
| Reduce with it and find the steady state | Hinge question; task L1, L2 | 35–50, 60–70 | ✓ |
| Derive Euler, take steps by hand, scale the error | Minute-95 cold call; task L3 | 70–95 | ✓ |
| Use solve_ivp deliberately; say what simulation cannot give | Exit ticket; task L2 | 95–115 | ✓ |

All four outcomes get both an instrument and a teaching block. The cost of that completeness is
that steady-state *analysis* — stability, multiple steady states, nullclines — is not taught here
at all; it appears as one bridge slide and is otherwise Ch. 4's business, outside this course.
That gap is deliberate and is stated to students rather than hidden.

## Sources

Built from the wiki pages listed in `draws_on`, which trace to [[ingalls-ch02-reaction-networks]]
§2.1.3 (Examples III and IV, equations 2.11–2.13, the remark on conservations p. 29, Exercises
2.1.7 and 2.1.8) and §2.1.4 (Figure 2.7, equation 2.16). Design framework: Wiggins & McTighe,
*Understanding by Design*; constructive alignment per Biggs & Tang; fading sequence per Renkl &
Atkinson.
