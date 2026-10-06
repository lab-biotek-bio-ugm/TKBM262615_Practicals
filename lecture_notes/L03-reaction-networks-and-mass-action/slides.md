---
title: Reaction Networks and Mass Action
subtitle: TKBM262615 - Lecture 3
author: Matin Nuhamunada
date: 2026-09-23
---

<!-- layout: quote -->
> The assumption of irreversibility is necessarily an approximation. The laws of thermodynamics
> dictate that all chemical reactions are reversible.
> -- Brian Ingalls, Mathematical Modelling in Systems Biology
<!-- notes: read it aloud. This is the course naming its own approximations, on cue. -->

---

# Retrieval - what L02 left you holding
- Units of d[A]/dt, and what the number means
- Variable or parameter - a fact, or a choice?
- Why is k[A][B] nonlinear?
<!-- notes: from memory, no notes. Posted after L02. -->

---

# You've run this model twice already
$$\frac{d[A]}{dt} = k_0 - k_1[A]$$
- L01: simulated it. L02: named every symbol.
- Where did the equation come from?
<!-- notes: today's answer - a picture, two arrows, a four-step recipe. -->

---

<!-- layout: section -->
# Part 1 - Reaction networks

---

# A list of arrows is a network
$$A+B\to C+D, \quad D\to B, \quad C\to E+F$$
- Species become nodes, reactions become edges
- "Graph" means graph-theory, not a plot
<!-- notes: flag the notational trap before it causes ten minutes of confusion. -->

---

# Closed or open?
- Closed: nothing enters or leaves - thermal equilibrium
- Open: exchange reactions - dynamic equilibrium
- A steady jet of water: unmoving shape, moving water
<!-- notes: is a cell open or closed? what would it mean if it were closed? -->

---

# Most biochemical networks are open
- Closed steady state: every rate is zero
- Open steady state: rates balance, none are zero
- A cell at thermal equilibrium is, thermodynamically, dead
<!-- notes: closed does not mean finished, open does not mean still running. -->

---

<!-- layout: section -->
# Part 2 - The law of mass action

---

# Why a product, not a sum?
- A reaction needs its reactants to meet
- Double A: double the chance any B meets it
- Two independent chances multiply
<!-- notes: what does k([A]+[B]) give when B=0? nonsense - a positive rate with no B present. -->

---

# Units are the cheapest check you own
- Zero reactants: k in concentration/time
- One reactant: k in 1/time
- Two reactants: k in 1/(concentration*time)
<!-- notes: a rate constant of 0.4 mM^-1 min^-1 - how many reactants? two, before you've seen the diagram. -->

---

<!-- layout: section -->
# Part 3 - Writing ODEs from a network

---

# Four steps, every time
- 1. Rate each reaction, by mass action
- 2. One equation per SPECIES, not per reaction
- 3. Include stoichiometric factors
- 4. Check units, last, always
<!-- notes: step 2 is where nearly everyone goes wrong the first time. -->

---

<!-- layout: picture -->
# One reaction, four consequences
![One reaction, four consequences: A overshoots while B accumulates](../../build/l03-figure-2-8.png)
v3 = k3[A][B] appears in all four equations.
<!-- notes: build this live on the board, species by species. Do A first, then B/C/D in pairs. -->

---

# A overshoots - and here's why
- C and D need both A and B to form
- B has to accumulate first
- Until then, A is made faster than it's used
<!-- notes: the reasoning is worth learning to do, not just the plot. -->

---

<!-- layout: section -->
# Part 4 - The hinge question

---

# How many equations does this need?
$$A+B\to C+D, \quad D\to B, \quad C\to E+F$$
- A: 3 - one per reaction  B: 6 - one per species
- C: 2 - only species in 2+ reactions  D: 4 - products only
<!-- notes: mini-whiteboards. B is correct - six species, six equations, regardless of arrow count. Break after. -->

---

<!-- layout: section -->
# Part 5 - Exponential decay

---

# One species, one reaction, guess the answer
$$\frac{da}{dt} = -ka \;\Rightarrow\; a(t) = A_0 e^{-kt}$$
- Ingalls: "direct (and rather unsatisfactory) - we guess"
- Verified by substitution, not derived
<!-- notes: when does A run out? never. This motivates the time constant next. -->

---

# Not every decay looks like this
- A + A -> : rate k[A]^2, nonlinear
- Solution is 1/(2kt + 1/A0) - not an exponential
- Falls off far more slowly at long times
<!-- notes: exponential relaxation is what LINEAR systems do. -->

---

<!-- layout: section -->
# Part 6 - Time constant

---

# tau = 1/k: how long is "long enough"
- After 1 tau: ~37% remains
- After 3 tau: ~5%. After 5 tau: <1%
- Not "the end" - the point where the rest stops mattering
<!-- notes: run for a few time constants, not because it's over, but because it's close enough. -->

---

# Decay sets the clock, not production
$$a^{ss}=k_0/k_1 \quad \tau = 1/k_1$$
- Steady state depends on both k0 and k1
- Speed depends on k1 alone
<!-- notes: to respond fast, degrade fast - and that costs the cell something. -->

---

<!-- layout: section -->
# Part 7 - Equilibrium and conservation

---

# Two equations, one piece of information
$$0=k_-b^{ss}-k_+a^{ss}, \quad 0=k_+a^{ss}-k_-b^{ss}$$
- These are the same equation
- Steady state alone can't pin down a and b
<!-- notes: slow down here. Students find this unsettling - that's the point. -->

---

# The ratio is free; the amounts need more
$$K_{eq} = \frac{k_+}{k_-} = \frac{[B]^{ss}}{[A]^{ss}}$$
- Ratio depends only on rate constants
- Amounts depend on what you started with
<!-- notes: double the starting A. What happens to Keq? Nothing. To b_ss? It doubles. -->

---

<!-- layout: section -->
# Part 8 - The nullspace payoff

---

# A surprise, now with a body
$$N = [\,-1,\; 1\,]^T \quad (A \to B)$$
- Rows are species, columns are reactions
- A left-nullspace vector is a conservation law
<!-- notes: build N on the board by hand for A -> B before running any code. -->

---

# The same computation, scaled up
```
null_space(N.T)  # [0.577 0.577 0.577] -- a+b+c
```
- Two species or three - the method doesn't change
- The matrix never mentions k+ or k-
<!-- notes: change k+ in your head - what happens to the nullspace? nothing. structural, not parametric. -->

---

<!-- layout: section -->
# Part 9 - Wrap-up

---

# What to carry into L04
- One equation per species, always
- Units tell you structure before the diagram does
- A conservation is structural - check before you simulate
<!-- notes: preview - "you have equations now. Next week: what do they settle to, and does the system return if nudged?" Issue the fading problem set. -->
