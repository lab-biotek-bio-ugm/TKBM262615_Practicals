---
type: Concept
title: "L03 Plan — Reaction Networks and Mass Action"
description: Backwards-design plan for the third lecture — turning a list of reactions into equations, one rate per arrow, one equation per species, and finding a network's conservation laws.
tags: [course, lecture-plan, L03]
sources:
  - id: wiki-l03
    resource: /index.md
    title: "Wiki pages tagged teaching.lecture: L03"
generated:
  by: claude-sonnet-5
  at: 2026-09-09
status: draft
teaching:
  lecture: L03
  role: reference
outcomes:
  - "Draw the interaction graph for a list of reactions, and say whether the network is open or closed."
  - "Write the ODE system for a small reaction network by inspection: one equation per species, one rate per reaction, correct stoichiometric factors."
  - "Give the units of any rate constant, and read a reaction's kinetic order off those units."
  - "State one condition under which mass action is the wrong rate law, and find a network's conservation relation by inspection and by computing a nullspace."
duration: "2 hours"
draws_on:
  - reaction-network
  - law-of-mass-action
  - writing-odes-from-a-reaction-network
  - exponential-decay
  - time-constant
  - equilibrium-constant
  - conservation-relation
---

# L03 Plan — Reaction Networks and Mass Action

Designed backwards. This is the lecture the first two exist to set up: L01 argued equations are
necessary, L02 built the calculus and just enough linear algebra. Here the two payoffs promised
earlier both land — `solve_ivp` finally runs on a network built *in this lecture*, not a toy, and
the [[nullspace]] surprise from L02 becomes an actual conservation law, exactly as
[[nullspace]]'s own Teaching notes said it should: "this page is better taught in L03 than L02...
the linear algebra should arrive as a tool for a question they already have."

**A deliberate design choice, stated up front.** The problem set below is not three fresh
exercises — it follows the exact fading sequence [[writing-odes-from-a-reaction-network]]'s own
Teaching notes prescribe: "do Figure 2.8 completely; give the next network with the rates written
but no equations; give the third as a bare reaction list." Levels 2 and 3 are original networks
(not from the book), built to isolate specific mechanics: level 2 keeps a closed, conserved system
so the conservation route gets a second worked case; level 3 is open and needs a self-reaction's
stoichiometric factor, so it forces the "one equation per species, not per reaction" discipline
onto unfamiliar ground.

## Stage 1 — Desired results

### Enduring understandings

1. **A network's equations come from a mechanical, four-step procedure, not from staring at the
   diagram until an answer appears.** Rate each reaction, credit and debit each species, include
   stoichiometric factors, check units. The procedure is short; skipping a step is where errors
   live.
2. **"One equation per species" is not the same claim as "one equation per reaction."** A single
   reaction can appear, with different signs, in every equation of every species it touches.
3. **A conservation relation is exact, structural, and comes from the same linear algebra
   introduced last lecture as a curiosity.** It does not depend on the rate constants — only on
   which arrows exist — and finding one can turn a system of ODEs into one ODE plus arithmetic.

### Essential questions

1. *"$k_3$ has units of mM⁻¹·s⁻¹. What does that tell you about reaction 3, before you've looked
   at the diagram?"* (Two reactants. Units carry structure.)
2. *"How many differential equations does this network need?"* (One per species — answered wrong,
   almost universally, the first time, by counting reactions instead.)
3. *"Does this conservation depend on the rate constants?"* (No — and that "no" is the seed of
   everything Chapter 5 does with network structure.)

### Students will know

- Closed networks reach thermal equilibrium (all rates zero); open networks reach dynamic
  equilibrium (rates balance, none are zero)
- The law of mass action, why it's a product and not a sum, and what a rate constant's units say
  about its reaction's kinetic order
- The four-step procedure for writing ODEs from a reaction list, including stoichiometric factors
- A conservation relation is exact, structural, and findable two ways: by inspection, and as a
  nullspace vector of the stoichiometry matrix
- Exponential decay is what *linear* relaxation looks like, is characterised by a time constant
  $\tau=1/k$, and is not the only shape a chemical system relaxes with

### Students will be able to

- Draw an interaction graph from a reaction list and classify it open or closed
- Read a rate constant's units and state how many reactants its reaction has
- Write a small network's ODE system by inspection, with correct signs and stoichiometric factors
- Check every equation's units as the last step, automatically
- Find a conservation relation by inspection on a simple network, and verify it as a nullspace
  vector in Python

---

## Stage 2 — Assessment evidence

### Performance task — fading sequence (due before L04)

Per [[writing-odes-from-a-reaction-network]]'s own prescribed sequence.

**Level 1 — worked in `notes.md`, reproduce from memory.** Ingalls' Figure 2.8 network (five
reactions, four species, rates given). Write all four equations and check units on one of them.

**Level 2 — rates given, no equations.** $A \underset{k_-}{\overset{k_+}{\rightleftharpoons}} B$,
then $B \xrightarrow{k_2} C$. Rates $v_1=k_+[A]$, $v_2=k_-[B]$, $v_3=k_2[B]$ are given. Write the
three species equations, check units, and state whether the network has a conservation relation —
if so, what it is, found by inspection.

**Level 3 — bare reaction list, fully independent.** $\to A$ (rate constant $k_0$), $A+A\to B$
(rate constant $k_1$), $B\to$ (rate constant $k_2$). Write the rate law for each reaction from mass
action (attending to the self-reaction's stoichiometry), write both species equations with correct
stoichiometric factors, check units, and state whether this network has a conservation relation —
and why or why not, referring to open versus closed.

*Assesses:* Understanding 1 (all three levels, decreasing scaffolding), Understanding 2 (the
species-vs-reaction count, tested hardest at Level 1 where one reaction touches four equations),
Understanding 3 (Level 2's conservation, and Level 3's *absence* of one, argued from openness rather
than computed).

*Success criteria:*
- Level 1: all four equations correct, $v_3$ correctly appearing in four places with the right
  signs, units check shown as a explicit line of arithmetic, not asserted.
- Level 2: three correct equations; correctly identifies $a+b+c$ (or an equivalent statement) as
  conserved, by summing the equations and showing the right-hand side cancels to zero — not by
  guessing.
- Level 3: correct mass-action rate for the self-reaction ($k_1[A]^2$), correct stoichiometric
  factor of 2 in $A$'s equation, correctly identifies the network as open (exchange reactions in
  and out) and states no conservation is expected — not "I checked and found none," since checking
  isn't required once openness is recognised.

### Other evidence

| When | Instrument | Outcome assessed |
|---|---|---|
| 0–10 | Retrieval: 3 questions on L02, posted after L02 | Retention into L03 |
| Minute 20 | Cold call: *"$k_3$ has units mM⁻¹·s⁻¹ — how many reactants?"* | Essential question 1 |
| Minute 60 | **Hinge question** (below) on mini-whiteboards | Understanding 2 |
| Minute 105 | Cold call: *"Does this conservation depend on $k$?"* on the nullspace demo | Essential question 3 |
| Minute 120 | Exit ticket: *"Write one equation per species for $A \to B \to$ (two reactions), and say how many equations you wrote and why."* | Understanding 2, independently |

### The hinge question

Placed right after the ODE-writing procedure is taught, before the break. Uses
[[reaction-network]]'s own introductory example, so the answer is checkable by anyone who paid
attention to the network's species count, not just its arrow count.

> The network is $A+B\to C+D$, $\;D\to B$, $\;C\to E+F$. How many differential equations do you
> need to write to describe it?
>
> **A.** 3 — one per reaction.
> **B.** 6 — one per species.
> **C.** 2 — only the species that appear in more than one reaction need their own equation.
> **D.** 4 — one per product species only.

**B is correct** — six species (A, B, C, D, E, F), six equations, regardless of the fact that
there are only three reactions. The wrong answers are the useful part:

- **A** — the target misconception, named explicitly in
  [[writing-odes-from-a-reaction-network]]'s Teaching notes: students count arrows because arrows
  are what they can see on the diagram.
- **C** — a partial correction that stops too early: *every* species needs a bookkeeping equation,
  even one that appears in only a single reaction (like $A$ or $B$ appearing once each), because
  its concentration still changes over time.
- **D** — confuses "the ODE describes production" with "only produced species need one"; $A$ and
  $B$ are consumed, and their concentrations change too, so they need equations exactly as much as
  $C$ through $F$ do.

If more than a third pick A, do not proceed to the reversible-reaction example — go back to Figure
2.8 and count equations against reactions on the board again, out loud.

---

## Stage 3 — Learning plan (120 minutes)

### 0–10 · Retrieval + hook

Three retrieval questions on L02 (posted after that lecture). Then the hook: put
$\frac{d[A]}{dt}=k_0-k_1[A]$ on the board — the model students have now simulated *twice*, in L01
and L02, without ever being told where it came from. Ask: "where did this equation come from?"
Today's answer: a picture, two arrows, and a four-step recipe.

### 10–20 · Reaction networks: open and closed

[[reaction-network]]. Ingalls' three-reaction example, redrawn as an interaction graph — flag the
graph-theory notational trap immediately, before anyone is confused by it. Closed versus open:
closed reaches thermal equilibrium (every rate zero, the system has run down); open reaches dynamic
equilibrium (rates balance, none are zero) — the faucet image. **Land it:** most biochemical
networks are open; a cell that reached thermal equilibrium is, thermodynamically, close to what
"dead" means.

**Cold call:** *"Is a cell open or closed? What would it mean if it were closed?"*

### 20–35 · The law of mass action

[[law-of-mass-action]]. Build it from the collision argument, not as a definition to memorise — two
species in a box, how often does an A meet a B, get to "proportional to how many of each," then
write the product. Kinetic order and the rate-constant-units table. Land the units-as-diagnostic
skill hard: it is the cheapest error check in the whole course.

**Cold call (essential question 1):** *"A rate constant is mM⁻¹·s⁻¹. How many reactants does that
reaction have?"*

### 35–55 · Writing ODEs from a reaction network

[[writing-odes-from-a-reaction-network]]. State the four-step procedure, then build the Figure 2.8
system live, species by species, asking the room for each term — do $A$ first (three terms, a sign
to get wrong), then let pairs do $B$, $C$, $D$. Reveal that $v_3$ appears in **four** equations,
twice with each sign, and ask why. This is where the equation from the 0–10 hook (production +
decay) is revisited as the simplest possible instance of the same procedure, one reaction in, one
out, one species.

### 55–65 · Hinge question + break

Mini-whiteboards on the question above. Do not proceed until it lands. Ten-minute break.

### 65–80 · Exponential decay

[[exponential-decay]]. Example I: $A\to$, one species, one reaction. Do the guess-and-verify
solution honestly — Ingalls' own word for the method is "unsatisfactory," and that honesty is worth
passing on. $a(t)=A_0e^{-kt}$; nothing ever reaches zero.

**Question to ask the room:** *"When does A run out?"* Never — which motivates the next section
rather than leaving it hanging.

### 80–90 · Time constant

[[time-constant]]. $\tau=1/k$; after one $\tau$, about 37% remains. The surprising fact, worth a
slide of its own: **decay** sets the time-scale, not production — $a^{ss}=k_0/k_1$ depends on both,
but *how fast* you get there depends on $k_1$ alone. Connect to biology: making a response fast
means degrading the signal fast, which costs the cell something.

### 90–105 · The reversible pair: equilibrium constant and conservation

[[equilibrium-constant]] and [[conservation-relation]] together, because neither makes sense alone
here. $A \rightleftharpoons B$: write both rate equations, set both to zero, and slow down on the
moment the two steady-state equations turn out to be the same equation — "two equations, one piece
of information" — before revealing that the missing piece is the conservation $a+b=T$. Solve for
$a^{ss}, b^{ss}$ by substitution. Land: the *ratio* depends only on rate constants; the *amounts*
depend on what you started with.

**Cold call:** *"I double how much A I start with. What happens to $K_{eq}$? What happens to
$b^{ss}$?"*

### 105–115 · The nullspace payoff

Revisit the L02 surprise — $[1\;\;{-1}]\cdot[2\;\;2]^T=0$ — and now give it a body. Build the
stoichiometry matrix for $A\to B$ by hand on the board (rows species, columns reactions), and
compute its nullspace live in Python: `null_space(N.T)` returns $[1,1]$ direction, i.e. $a+b$.
**Do not stop at one example** — this is the moment promised twice now, so also run it on the
reversible-plus-decay network from Level 2 of the problem set, and let the room watch the same
computation scale up without changing in kind.

**Cold call (essential question 3):** *"Does this conservation depend on $k_+$ or $k_-$? Change
them in the code and re-run — what happens to the nullspace?"* Nothing — structural, not
parametric.

### 115–120 · Wrap-up

Return to essential question 2. Issue the fading problem set; due before L04. Preview: *"Next
week, you have equations. The question becomes: what do they settle down to, and does the system
go back if you nudge it?"*

---

## Tailoring

- **Students who found L02's linear algebra thin.** This is where it gets a reason to exist. If the
  nullspace demo still feels abstract, run it a third time on a network the room proposes on the
  spot.
- **Students confident with the chemistry already.** Push on the units-as-diagnostic skill and the
  "why is it a product, not a sum" argument — both are more subtle than they look and reward a
  second pass.
- **Language.** *Rate*, *stoichiometric factor*, *conservation*, *nullspace* go on the board and
  stay, same policy as L01–L02.

---

## Alignment check

| Stage 1 outcome | Assessed in Stage 2 | Taught in Stage 3 | ✓ |
|---|---|---|---|
| Draw interaction graph, open/closed | Minute-20 groundwork; exit ticket implicitly | 10–20 | ✓ |
| Write ODE system by inspection | Fading task, all 3 levels; hinge question | 35–55 | ✓ |
| Units of a rate constant / kinetic order | Minute-20 cold call; fading task units checks | 20–35 | ✓ |
| Mass action's failure condition | *(named, not independently assessed)* | 20–35 (bridge to L05) | ⚠ |
| Conservation by inspection and by nullspace | Fading task Level 2 & 3; minute-105 cold call | 90–115 | ✓ |

**One deliberate gap, flagged rather than hidden.** "State one condition under which mass action is
the wrong rate law" (the syllabus's outcome (d)) is stated in class — effective rate constants,
enzyme saturation — but not independently assessed this lecture, because assessing it properly
means deriving Michaelis-Menten, which is L05's job. L03 plants the sentence; L05 is where a student
could actually be tested on it.

## Sources

Built from the wiki pages listed in `draws_on`, all of which trace to
[[ingalls-ch02-reaction-networks]]. Design framework: Wiggins & McTighe, *Understanding by Design*;
constructive alignment per Biggs & Tang; fading sequence per Renkl & Atkinson, following the
sequence [[writing-odes-from-a-reaction-network]]'s own Teaching notes prescribe.
