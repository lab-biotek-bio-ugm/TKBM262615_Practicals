---
type: Concept
title: "L02 Plan — The Mathematical Toolkit"
description: Backwards-design plan for the second lecture — the derivative as a rate, state versus parameter, linearity and its local escape hatch, and just enough linear algebra to preview L03.
tags: [course, lecture-plan, L02]
sources:
  - id: wiki-l02
    resource: /index.md
    title: "Wiki pages tagged teaching.lecture: L02"
generated:
  by: claude-sonnet-5
  at: 2026-09-09
status: draft
teaching:
  lecture: L02
  role: reference
outcomes:
  - "Read a rate off a time course, and state its units and what the number means physically."
  - "Name every symbol in dx/dt = f(x, p), and say whether a given quantity is a state variable or a parameter for a stated time-scale."
  - "Integrate a one-variable ODE in Python with solve_ivp and plot it."
  - "Compute an inner product and a matrix-vector product by hand, and check whether a given vector lies in a matrix's nullspace."
duration: "2 hours"
draws_on:
  - derivative
  - differentiation-rules
  - partial-derivative
  - implicit-differentiation
  - state-variable-and-parameter
  - linearity-and-nonlinearity
  - local-versus-global-behaviour
  - vector-and-matrix
  - nullspace
---

# L02 Plan — The Mathematical Toolkit

Designed backwards. **A flagged decision before Stage 1:** the wiki's own [[numerical-simulation]]
page — Euler's method, `solve_ivp` internals, error and stiffness — is tagged `teaching.lecture:
L04`, not L02, even though `course/syllabus.md`'s L02 description says "Euler by hand, then
`solve_ivp`". The tag is deliberate: Euler's method is derived from the derivative *and* needs a
model built from a reaction network to run on something real, and that network doesn't exist until
L03. Teaching it here would either be content-free (no model to run it on) or would duplicate L04's
lecture two weeks early.

**Resolution, flagged for the lecturer rather than silently picked:** L02 uses `solve_ivp` as a
**tool** — call it, get a time course, plot it — on the one-variable toy model already introduced in
L01, without deriving how it works inside. Outcome (c) above is satisfied at "can operate the
tool"; "understands the tool" is L04's job, in full, on a model L03 will have built. Say this
explicitly in the lecture: "we are borrowing a black box today; L04 opens it."

A similar, already-logged flag applies to [[nullspace]]: its own Teaching notes argue it lands
better in L03 (once there is a real stoichiometry matrix to find conservation laws in) even though
it is tagged L02. L02 therefore gives the *surprise* — a nonzero product from nonzero vectors — and
promises the biology, rather than working a reaction-network example it doesn't yet have the
vocabulary for.

## Stage 1 — Desired results

### Enduring understandings

1. **A derivative is a rate, and rates have units.** Fluently differentiating a symbol is not the
   same skill as believing the result is a physical quantity — and the whole course only uses the
   second one.
2. **Whether a quantity is a state variable or a parameter is a modelling choice tied to a
   time-scale, not a fact about the quantity.** The same enzyme abundance is a parameter in a
   minutes-long metabolic model and a state variable in an hours-long gene-regulatory one.
3. **Linearity is the exception in biology, and the escape from nonlinearity is local, not
   global.** A tangent line is a real, useful model of a curve near one point — and a real,
   physically absurd one far from it.

### Essential questions

1. *"The concentration is 5 mM and its derivative is −0.2 mM/s. Is there more or less of it in one
   second, and roughly how much?"* (Diagnoses whether the derivative has become physical, not just
   symbolic.)
2. *"Is this quantity a variable or a parameter?"* (There is no context-free answer. L02 answer:
   "tell me the time-scale." L04 sharpens this into the quasi-steady-state assumption.)
3. *"Why can't a linear model have two stable states?"* (No proof expected — the feel that a
   proportionality has nowhere to put a second answer is the target.)

### Students will know

- A derivative is the limiting slope of a secant, and it carries units
- The ten differentiation rules exist to avoid the limit, not to replace understanding it
- The curly $\partial$ means "the other variables were frozen", nothing more
- $\dfrac{d\mathbf{x}}{dt} = f(\mathbf{x}, \mathbf{p})$: what each symbol is, and which ones move
- Linear = direct proportionality; nonlinear is everything else, including every product of two
  concentrations
- A tangent-line approximation is accurate near its operating point and can fail *qualitatively*,
  not just numerically, away from it
- A matrix-vector product is a stack of inner products, and an inner product of nonzero vectors can
  be zero

### Students will be able to

- Compute a derivative from the definition once, by hand, and recognise it agrees with the power
  rule
- Say, for a stated model and time-scale, whether a given quantity is a variable or a parameter
- Read the sign and shape of a derivative off the shape of the original function, without computing
  it symbolically
- Call `solve_ivp` on a one-variable rate function and plot the result
- Compute a small matrix-vector product by hand and check a vector against a nullspace condition

---

## Stage 2 — Assessment evidence

### Performance task — worked, faded, independent (due before L03)

Three problems, deliberately increasing in how much scaffolding is removed —
[[worked-example-fading-designer|fading]] rather than ten repeats of the same problem.

**1. Worked (fully solved in `notes.md`, reproduce it from memory).** Differentiate
$v(s) = \dfrac{V_{max}\,s}{K+s}$ from the quotient rule, state its units if $s$ is a concentration
in µM and $V_{max}$ is a rate in µM·min⁻¹, and say in one sentence what the sign of the derivative
means for the shape of $v$.

**2. Partially faded.** A gene's transcription rate is $g([R]) = \dfrac{\beta}{1 + ([R]/K)^n}$,
where $[R]$ is a repressor concentration. Find $\partial g/\partial [R]$ (the quotient and chain
rules are both needed; the chain-rule step is given, the rest is not). State the sign, and what it
means biologically.

**3. Independent.** A model has $\dfrac{d[X]}{dt} = k_1[A][B] - k_2[X]$, with $[A]$ held constant
over the time-scale of interest and $[B]$ varying. (a) Is $[A]$ a state variable or a parameter, and
why — for *this* time-scale? (b) Is the production term linear in $[B]$? Justify using the
linearity test. (c) Compute $\partial(k_1[A][B])/\partial[B]$ and say what it means.

*Assesses:* Understanding 1 (task 1), Understanding 2 (task 3a), Understanding 3 (task 3b), and
transfer of the partial-derivative and quotient-rule mechanics from a worked case (task 1) to an
unfamiliar rate law (task 2) to a fully independent one embedded in a modelling question (task 3).

*Success criteria:*
- Task 1: correct derivative via the quotient rule *by name*, correct units, and states that the
  derivative is everywhere positive and shrinking — the saturation shape, not just a number.
- Task 2: correct sign (negative — more repressor lowers transcription) reached by applying, not
  re-deriving, the given chain-rule step.
- Task 3: identifies the time-scale as the reason $[A]$ is a parameter here (not "because it's held
  constant" alone — *why* it's reasonable to hold it constant); correctly applies the two-part
  linearity test to a product of variables; correct partial derivative with a biological reading of
  its sign.

### Other evidence

| When | Instrument | Outcome assessed |
|---|---|---|
| 0–10 | Retrieval practice: 3 questions on L01, posted after L01 | Retention into L02 |
| Minute 20 | Cold call: *"What are the units of this slope, and what does the number mean?"* on a real time-course sketch | Outcome (a) |
| Minute 55 | **Hinge question** (below) on mini-whiteboards | Understanding 1 |
| Minute 100 | Cold call: *"Variable or parameter?"* on the enzyme-abundance example at two time-scales | Understanding 2 |
| Minute 120 | Exit ticket: *"Give one quantity from your own biology background that is a parameter at one time-scale and a variable at another."* | Transfer of Understanding 2 |

### The hinge question

Placed right after differentiation rules and partial derivatives, before the break. Every wrong
answer diagnoses a different failure to connect symbol to meaning.

> $\dfrac{d[A]}{dt} = -0.2$ mM/s at the instant you measure it, and $[A] = 5$ mM right now. Which is
> the best statement of what happens over the next second?
>
> **A.** $[A]$ becomes exactly $4.8$ mM.
> **B.** $[A]$ becomes approximately $4.8$ mM, and the estimate gets worse the longer you wait.
> **C.** $[A]$ decreases, but you cannot say anything about the size of the decrease from a
> derivative alone.
> **D.** $[A]$ becomes $-0.2$ mM lower than its starting value, which is a red flag if $[A]$ is a
> concentration.

**B is correct**, and the wrong answers are the useful part:

- **A** — has correctly turned the derivative into a number, but forgotten it is an *instantaneous*
  rate, not a rate that holds constant for a whole second. This is the Euler-method error, one
  lecture before Euler's method has a name.
- **C** — the opposite failure: has learned "derivative = rate" as a slogan without learning how to
  use the number at all.
- **D** — has confused "the derivative is $-0.2$" with "the new value is the old value minus $0.2$",
  ignoring what the two quantities' units mean when combined; a decent answer once you replace "$-0.2$
  mM lower" with "$-0.2$ mM/s $\times$ 1 s lower", which is exactly B.

If more than a third pick A, do not move on to state/parameter — go back to the secant-to-tangent
picture and shrink the interval on the board again.

---

## Stage 3 — Learning plan (120 minutes)

### 0–10 · Retrieval + hook

Three retrieval questions on L01 (posted after that lecture), answered from memory. Then the hook:
sketch a measured time course on the board (concentration vs. time, a curve, no formula) and ask
"how fast is it changing right now, at this point?" Let the room disagree about *how* to answer
before naming anything.

### 10–30 · The derivative, as a rate

[[derivative]]. Average rate of change first — two points, a slope, units — then shrink the
interval on the board until it is a tangent. State (B.1) and (B.2) only after the room has done the
shrinking conceptually. Worked example from the definition: $f(x)=x^2$ at $x_0=3$, factor and
cancel, take the limit, get 6, check against the power rule.

**Land it:** a derivative is a rate, and it has units, every time. Ask the essential question 1
cold, before teaching anything else about it.

### 30–40 · Differentiation rules, as a reference

[[differentiation-rules]]. Do not lecture the table — hand it out. Work example (ii),
$r(s) = 2s/(s+4)$, live, and spend the saved time asking what the *shape* of the derivative says:
positive everywhere, shrinking — a saturating curve's fingerprint. That reading-the-shape skill is
worth more than table fluency.

### 40–50 · Partial derivatives: the same idea, one variable at a time

[[partial-derivative]]. Use $v = k[A][B]$ and nothing else — the mass-action rate they will meet
formally in L03. Compute both partials in two lines, then ask what each means: sensitivity to $A$
rises with more $B$ present, and vanishes if $B$ is absent. State explicitly: "the curly $\partial$
means I froze the other variable; the differentiation is identical."

*(Optional, if time allows and the room is comfortable: [[implicit-differentiation]] in five
minutes, framed as "sometimes you can get the derivative without ever solving for the function" —
promissory note for Lineweaver-Burk in L05. Tagged `stretch` in the wiki; drop without guilt.)*

### 50–60 · Hinge question + break

Mini-whiteboards on the question above. Do not proceed until it lands. Ten-minute break.

### 60–75 · State variables and parameters

[[state-variable-and-parameter]]. Write $\dfrac{d\mathbf{x}}{dt} = f(\mathbf{x}, \mathbf{p})$ and
label every symbol on the board, including $t$ — four minutes, non-negotiable. Then the enzyme
example: same enzyme, parameter in a minutes-scale metabolic model, state variable in an
hours-scale gene-regulatory one. Nothing about the enzyme changed; the question did.

**Cold call:** *"I'm modelling an enzyme converting sugar over ten seconds. Variable or parameter?
What if I watch for ten hours?"*

### 75–85 · Linearity and nonlinearity

[[linearity-and-nonlinearity]]. State the two-part test, check it on $f(x)=kx$ (passes) and
$f(x)=x^2$ (fails, name the cross-term). Land the consequence: mass action for two reactants,
$k[A][B]$, is already nonlinear — so the *simplest* chemistry in this course is already outside
linear theory. Connect back to [[saturation]] from L01 as the two nonlinear shapes that recur.

### 85–100 · Local versus global behaviour

[[local-versus-global-behaviour]]. Show the figure: $f(x) = x/(1+x)$ and its tangent at $x^*=1$.
Walk along the $x$-axis with the room — "still good? still good?" — until they say no, and let them
find the domain of validity themselves. Then reveal the $x=5$ case: the approximation doesn't just
get worse, it predicts a concentration above the physical ceiling. **Local means local**, said as a
warning, not a caveat.

### 100–110 · Vectors and matrices, at the depth this course needs

[[vector-and-matrix]]. Inner product by hand on the board (3-by-4 times 4-by-1, the room calling
out each row). State the shape rule as a consequence, not a separate fact to memorise. This is the
only hand computation they will do — after this, NumPy.

### 110–115 · The nullspace surprise

[[nullspace]]. Open with $[1\;\;{-1}]\cdot[2\;\;2]^T = 0$ — two nonzero vectors, a zero product —
and let the room be surprised. Define the nullspace, state the two closure properties without
proof. **Do not** build a reaction-network example here; promise it: "next week this becomes a
conservation law, and you will find one on the board."

### 115–120 · Wrap-up and Python demo

Run, live, `solve_ivp` on $\dfrac{d[A]}{dt} = k_0 - k_1[A]$ from the L01 demo script, and plot it.
Say explicitly: "you now know what every symbol in this call means; how the solver gets from one
point to the next is L04." Issue the performance task; due before L03. Preview: "next week, a list
of chemical reactions becomes this equation, arrow by arrow."

---

## Tailoring

- **Students confident with calculus already.** They will want to skip to the linear algebra.
  Redirect with the essential question — most can differentiate but freeze on "what does 0.2 mean
  physically", which is the actual target.
- **Students without prior linear algebra.** The 100–115 block is deliberately minimal. If it still
  drags, cut the nullspace surprise to two minutes and let L03 carry more of the weight — the wiki
  itself flags this as the better home for it.
- **Language.** *Rate*, *tangent*, *parameter*, *nullspace* go on the board and stay there, same
  policy as L01.

---

## Alignment check

| Stage 1 outcome | Assessed in Stage 2 | Taught in Stage 3 | ✓ |
|---|---|---|---|
| (a) read a rate off a time course | Minute-20 cold call | 0–30 | ✓ |
| (b) name every symbol in $d\mathbf{x}/dt=f(\mathbf{x},\mathbf{p})$ | Task 3a; minute-100 cold call | 60–75 | ✓ |
| (c) integrate a 1-var ODE in Python and plot it | *(operated, not examined)* | 115–120 | ⚠ |
| (d) inner/matrix-vector product; nullspace check | Task 3 groundwork; exit ticket does not cover it | 100–115 | ⚠ |
| Understanding 1 — derivative as rate | Hinge question; Task 1 | 10–60 | ✓ |
| Understanding 2 — variable/parameter is time-scale-relative | Task 3a; exit ticket | 60–75 | ✓ |
| Understanding 3 — linear is the exception; local escapes it | Task 3b; board Q&A 85–100 | 75–100 | ✓ |

**Two deliberate gaps, both flagged rather than hidden.** Outcome (c) is demonstrated live but not
independently assessed in this lecture — running `solve_ivp` correctly is folded into the L03/L04
problem sets once there is a real model to run it on. Outcome (d) has no dedicated assessment
instrument yet; the nullspace idea is deliberately left as a promise for L03, where
[[nullspace]]'s own Teaching notes say it belongs, and it will be assessed there instead.

## Sources

Built from the wiki pages listed in `draws_on`, all of which trace to
[[ingalls-appendix-b-mathematical-fundamentals]] and [[ingalls-ch01-introduction]] §1.5. Design
framework: Wiggins & McTighe, *Understanding by Design*; constructive alignment per Biggs & Tang;
fading sequence per Renkl & Atkinson's worked-example fading.
