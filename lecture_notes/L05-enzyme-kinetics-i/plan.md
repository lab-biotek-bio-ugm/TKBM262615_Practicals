---
type: Concept
title: "L05 Plan — Enzyme Kinetics I"
description: Backwards-design plan for the fifth lecture (Kinematika Enzim I) — the enzyme mechanism, the quasi-steady-state assumption on the ES complex, the Michaelis-Menten derivation, and reading Vmax and KM.
tags: [course, lecture-plan, L05]
sources:
  - id: wiki-l05
    resource: /index.md
    title: "Wiki pages tagged teaching.lecture: L05"
generated:
  by: claude-opus-5
  at: 2026-09-09
status: draft
teaching:
  lecture: L05
  role: reference
outcomes:
  - "Write the elementary mass-action equations for the mechanism E + S ⇌ ES → E + P and use the enzyme conservation to remove one of them."
  - "State the quasi-steady-state assumption for the ES complex, give both independent reasons the complex is fast, and say why the result is a function of time rather than a constant."
  - "Derive the Michaelis-Menten rate law from that assumption, naming every simplification used."
  - "Read Vmax and KM off a saturation curve, say what each does and does not depend on, and give the condition under which KM approximates a binding affinity."
duration: "2 hours"
draws_on:
  - enzyme-catalysis
  - separation-of-time-scales
  - quasi-steady-state-approximation
  - rapid-equilibrium-approximation
  - michaelis-menten-kinetics
  - conservation-relation
  - saturation
notes: [notes.md, notes.id.md]      # English and Bahasa Indonesia; keep the pair in step
practical: "TKBM262615_Practicals/notebooks/04_enzyme_kinetics.ipynb"   # being updated; not yet published
revised:
  by: claude-opus-5
  at: 2026-09-16
  note: "Re-scoped to the four RPS topics for Kinematika Enzim I; kinetic order moved to L06, two-substrate reactions to further reading; problem set written into the notes; deck rebuilt on the 2026 UGM template."
---

# L05 Plan — Enzyme Kinetics I (Kinematika Enzim I)

**Topics, as set in the course plan (RPS):** the enzyme mechanism $E + S \rightleftharpoons ES \to E + P$;
the quasi-steady-state assumption for the ES complex; the derivation of the Michaelis-Menten
equation; interpreting $V_{max}$ and $K_M$. Everything below serves those four and nothing else is
assessed.

Designed backwards.

**Scope note, and it is a deliberate re-cut.** An earlier version of this lecture opened by telling
students that everything in it was L04's quasi-steady-state approximation reapplied, and leaned on
L04 to have taught the QSSA in the abstract. L04 has since been re-cut around conservation and
numerics, so **the QSSA is now taught here, from scratch, on the network that motivates it.**

That is the better order, not merely the necessary one. The abstract network
$\to A \rightleftharpoons B \to$ is a fine vehicle for the technique and a poor advertisement for
it: nobody wants that reduction badly enough to work for it. The enzyme mechanism is different.
Students arrive already knowing the Michaelis-Menten equation as something to memorise, and
already believing (wrongly) that $K_M$ measures binding affinity. Deriving it gives the technique
something to be *for*.

What L04 does supply, and what this lecture leans on hard, is the **exact** reduction: the enzyme
conservation $e_T = e + c$ is L04's move applied to a real system, and it is used here fifteen
minutes before a reduction that looks identical on the board and is an approximation. Make that
contrast explicit both times.

Rapid equilibrium survives as a fifteen-minute contrast rather than a technique to master, framed
historically: Michaelis and Menten (1913) assumed equilibrium, Briggs and Haldane (1925) used the
QSSA, and the two give different expressions for $K_M$ from the same data. That framing does real
work — it is the honest answer to "so which formula for $K_M$ is right", and it sets up the hinge
question.

## Stage 1 — Desired results

### Enduring understandings

1. **Mass action did not fail; it was applied at the wrong level.** "$S \to P$, catalysed by an
   enzyme" is not an elementary reaction. It is binding, unbinding and conversion, and mass action
   applies perfectly well to those three. Every saturating rate law in this course comes from
   descending one level and then climbing back.
2. **The quasi-steady-state assumption replaces a differential description with an algebraic one;
   it does not freeze anything.** $c^{qss}$ is a function of $s(t)$, so it moves throughout. The
   shorthand "set the derivative to zero" is what creates the misconception, so use Ingalls'
   longer phrasing instead.
3. **$V_{max}$ and $K_M$ are what you can measure; their decomposition into rate constants depends
   on which approximation you used.** $V_{max}$ scales with the enzyme you happen to have added;
   $K_M$ is a half-saturating concentration and only sometimes a binding affinity.

### Essential questions

1. *"What would have to be true for the rate to stop rising as you add substrate?"* (You run out
   of enzyme. Saturation gets a physical cause rather than a curve shape.)
2. *"Is there a $t$ in the expression for $c^{qss}$? What does that mean?"* (Yes, inside $s(t)$.
   It means the complex is not constant — it is always caught up.)
3. *"I doubled the enzyme concentration. What happens to $V_{max}$? To $K_M$?"* ($V_{max}$ doubles,
   $K_M$ is unchanged. The diagnostic that separates the two constants, and the setup for L06.)

### Students will know

- The mechanism $S + E \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} C \xrightarrow{k_2} P + E$,
  and the two simplifications that produced it (lumped complexes; no product rebinding)
- A catalyst cannot shift an equilibrium, and this is a thermodynamic necessity rather than an
  observed regularity — the perpetual-motion argument makes it a theorem
- The four mass-action equations, the mirror symmetry $\frac{de}{dt} = -\frac{dc}{dt}$, and the
  enzyme conservation $e_T = e + c$ that removes one of them exactly
- **Two independent reasons** the complex is fast: time constants ($\frac{1}{k_1+k_{-1}}$ against
  $\frac{1}{k_2}$) and concentrations ($s \gg e_T$). The second is the one students overlook and
  often the dominant one
- $c^{qss}(t) = \frac{k_1e_Ts(t)}{k_{-1}+k_2+k_1s(t)}$, and that it tracks $s$
- $V_{max} = k_2e_T$, $K_M = \frac{k_{-1}+k_2}{k_1}$, $v = \frac{V_{max}s}{K_M+s}$, derived
- $k_{cat} = V_{max}/e_T$ is the property of the protein; $V_{max}$ is the property of the tube
- The first-order and zero-order regimes, and that the reduction's error is sequestration, scaling
  with $e_T$

### Students will be able to

- Build the four mass-action equations from the mechanism by inspection
- Derive the enzyme conservation by the L04 route and use it to eliminate $e$
- Apply the QSSA to the complex, doing the collection-of-terms step correctly
- Complete the derivation to (3.5) and name each simplification as it is used
- Read $V_{max}$ and $K_M$ off a curve, and check $v(K_M) = V_{max}/2$ in one line
- Say the condition under which $K_M \approx k_{-1}/k_1$, and what $K_M$ becomes when it does not
  hold

---

## Stage 2 — Assessment evidence

### Performance task — the five-rung problem set, due before L06

Written out in full, with answers, at the end of `notes.md` / `notes.id.md`. The rungs fade from a
worked example to an open question (Renkl and Atkinson):

1. **Reproduce** the Michaelis-Menten derivation with notes closed, marking the exact step
   (conservation) and the approximate one (QSSA).
2. **Numbers.** From $k_1, k_{-1}, k_2, e_T$ compute $V_{max}$, $K_M$, $k_{cat}$; the rate at
   $K_M$, $3K_M$, $10K_M$; the $s$ for 90% of $V_{max}$; and compare $K_M$ with $K_S$.
3. **Read data (guided).** Estimate $V_{max}$ and $K_M$ by eye from an initial-rate table, then fit
   with `curve_fit` from a skeleton.
4. **Independent derivation.** The 1913 rapid-equilibrium version (Ingalls Exercise 3.1.1), plus a
   paragraph on what a measured $K_M$ actually is.
5. **Independent, computational.** Find the $e_T$ at which the reduction's [S] error falls to 1%
   of $s(0)$ (answer: about 0.057 mM, $s(0)/e_T \approx 87$) and connect it to $s \gg e_T$.

*Assesses:* Understanding 1 (rungs 1, 4), Understanding 2 (rungs 1, 5), Understanding 3 (rungs 2–4).

*Success criteria:* the collection-of-terms step shown, not skipped; the conservation named as the
exact step; rung 2(d) answered from the numbers ($K_M$ is eleven times $K_S$ because $k_2 \gg
k_{-1}$); rung 4's paragraph recognises that the experiment measures $K_M$ and $V_{max}$
themselves, not their decomposition. A student who concludes one derivation is simply "wrong" has
missed the point.

### Other evidence

| When | Instrument | Outcome assessed |
|---|---|---|
| 0–10 | Retrieval: 3 questions on L04, posted after L04 | Retention; especially "why is a conservation exact" |
| Minute 20 | Cold call (essential question 1): what would make the rate stop rising? | Understanding 1 |
| Minute 40 | Cold call: if $\frac{de}{dt} = -\frac{dc}{dt}$, what is constant? | L04 transfer, live |
| Minute 62 | **Cold call (essential question 2)** on $c^{qss}$: is there a $t$ in it? | Understanding 2, the misconception, directly |
| Minute 85 | **Hinge question** (below) on mini-whiteboards | Understanding 3 |
| Minute 100 | Cold call (essential question 3): double the enzyme | Understanding 3; sets up L06 |
| Minute 120 | Exit ticket: *"Name the one assumption in today's derivation that was not an approximation."* | Understandings 1–2; the L04 link |

### The hinge question

Placed at the end of Part 4, immediately after the rate law is named.

> $K_M = \frac{k_{-1}+k_2}{k_1}$. Does $K_M$ measure how tightly the enzyme binds its substrate?
>
> **A.** Always — that is what $K_M$ is.
> **B.** Only when $k_2 \gg k_{-1}$.
> **C.** Only when $k_2 \ll k_{-1}$, in which case $K_M \approx k_{-1}/k_1$.
> **D.** Never.

**C is correct.** Check both limits live rather than asserting the answer:

- Set $k_2 = 0$. No catalysis, and $K_M = k_{-1}/k_1$ exactly — the dissociation constant, which
  genuinely is a binding affinity.
- Make $k_2$ large. Then $K_M \approx k_2/k_1$, which contains no information about unbinding at
  all. An enzyme with a large $K_M$ under these conditions may bind its substrate very tightly.

- **A** is the misconception carried in from biochemistry, and it is the reason this question
  exists. It is worth saying that the textbook shorthand is not exactly wrong, it is a special
  case being reported as a definition.
- **B** has the inequality backwards.
- **D** overcorrects: there is a real and common regime in which $K_M$ *is* the dissociation
  constant.

Do not proceed until it lands. Break immediately after.

---

## Stage 3 — Learning plan (120 minutes)

### 0–10 · Retrieval + hook

Three retrieval questions on L04: why a conservation is exact and a reduction using it free; what
Euler assumes across one step; what halving the step size does to the error. The first is the one
today needs.

Then the hook, drawn on the board rather than shown: mass action predicts $v = k[S]$, a straight
line through the origin with no ceiling. What is measured bends over and flattens. Ask which is
wrong, the law or the measurement. Neither — and resist answering for them for a few seconds.

### 10–25 · What an enzyme actually does

[[enzyme-catalysis]]. The active site, the barrier, the transition state. Then the point that
carries weight: both directions speed up by the same factor, so **the equilibrium is untouched**.
Derive that as a consequence rather than stating it as a rule — if a catalyst could shift an
equilibrium you could cycle two catalysts and extract work from nothing, so it cannot. The rule is
a theorem.

Then the diagnosis, which the whole lecture rests on: "$S \to P$, catalysed by an enzyme" is not
elementary. It is three reactions. Mass action applies to those three.

Write the mechanism (3.2) and name both simplifications openly, as Ingalls does: the two complexes
are lumped (itself a rapid-equilibrium assumption), and product never rebinds — justified because
rate measurements are made in the absence of product, and it is what makes the rate law
irreversible.

**Cold call (essential question 1):** what would have to be true for the rate to stop rising?
Someone will say "you run out of enzyme". Accept it warmly; they have just derived the physical
cause of saturation themselves.

### 25–45 · Writing the equations down

Build all four mass-action equations on the board, asking the room for each term. This is pure L03
practice and should feel easy — say so.

Then the mirror symmetry $\frac{de}{dt} = -\frac{dc}{dt}$, term by term.

**Cold call:** if two derivatives are always opposite, what can you say about the sum? Zero. And a
quantity whose derivative is zero is constant. They have just re-derived L04's second route on a
system that matters.

Name it: the enzyme is a **conserved moiety**, $e_T = e + c$, and this was the example promised
last week. Substitute $e = e_T - c$ and one equation disappears. **Say that this reduction is
exact**, because in twenty minutes another one will look identical and not be.

Close the section honestly: three equations left, still nonlinear, the $sc$ product will not
integrate by hand. We have used the only exact reduction available and still cannot solve it. That
is what makes the next move necessary rather than merely convenient.

### 45–65 · The quasi-steady-state assumption

[[separation-of-time-scales]] introduced just in time, not as a prior lecture's machinery: two
clocks in one mechanism (Ingalls Figure 3.3A), and a factor of ten is enough. Show the full-mechanism
time course on a log axis (`l05-mechanism-timecourse.png`): complex half-formed at 0.004 s,
half the substrate converted at 0.29 s, a factor of about 66.

Then **both** reasons the complex is fast, with the second given equal billing:
$\frac{1}{k_1+k_{-1}}$ against $\frac{1}{k_2}$, *and* $s \gg e_T$ in the cell. Flag now that the
second reason will come back at the end of the lecture as the condition that limits the result.

State the procedure generally before applying it — the unit of approximation is a **species**, and
every reaction touching it must be fast — then apply it. Do the collection-of-terms step live and
slowly; ninety seconds, and it is where students lose the thread.

**Cold call (essential question 2), the misconception directly:** is there a $t$ in $c^{qss}$?
Point at the $s(t)$. Use Ingalls' longer phrasing rather than "set the derivative to zero": we
replace the differential description of $c$ with an algebraic one saying the complex instantly
reaches the steady state it would attain if everything else were held fixed. The phrase to keep is
**"from C's point of view"**. C is not frozen; C is always caught up.

Then the figure, panel B first: the algebraic formula tracking the real complex to 2.3% of the
enzyme pool, and both of them moving.

### 65–80 · What if you assume equilibrium instead?

[[rapid-equilibrium-approximation]] as history and contrast, not as a technique to drill. Michaelis
and Menten (1913) assumed the binding step sits at equilibrium and got $K_M = k_{-1}/k_1$; Briggs
and Haldane (1925) applied the QSSA and got $K_M = \frac{k_{-1}+k_2}{k_1}$. Same curve, same data,
different decomposition.

Then the comparison figure on the simpler network, where the argument shows naked: the equilibrium
assumption imposes a condition the true steady state does not satisfy when flux runs through the
reaction, so its error never closes. The QSSA imposes $\frac{dc}{dt} = 0$, which is exactly the
condition the true steady state does satisfy. One structural fact, two fates.

### 80–95 · The Michaelis-Menten equation, then the hinge

Substitute back. Let the messy form (3.4) sit on the board for a few seconds before tidying —
students need to see the mess. Divide by $k_1$, and **only then** name the two groupings.
Deliberately do not present $V_{max}$ and $K_M$ as definitions; students who watch them arrive as
tidying-up understand why they are the measurable quantities.

Hinge question, mini-whiteboards. Break after.

### 95–112 · Reading the two constants

$V_{max} = k_2e_T$ scales with how much enzyme is in the tube. **Cold call (essential question 3):**
double the enzyme — what happens to each constant? Then $k_{cat} = V_{max}/e_T$ as the property of
the protein, with the practical consequence: two labs reporting different $V_{max}$ for the same
enzyme may both be right.

$K_M$ as the half-saturating concentration, checked by substituting $s = K_M$ in one line, then
pointed at on panel A of the figure. The two limiting regimes, one line each on the board. Then
what a cell can and cannot control: adding substrate to a saturated pathway does nothing, and only
more enzyme or a better one helps. This is where Ch. 3 stops being algebra.

Finally, where the reduction breaks — panel C. The transient is wrong by construction; substrate
sequestered inside C makes the reduced model overcount free S; and the error scales with $e_T$
(0.84 mM at $e_T = 1$, 0.009 mM at $e_T = 0.01$). Ingalls exaggerates it deliberately so the
mechanism is visible. Run both values live if time allows.

### 112–118 · Practical and problem set

Point at the further-reading slide in one sentence: kinetic order opens L06, and two-substrate
reactions are in the notes and the wiki, not assessed. Then the practical (notebook 04) and the
five-rung problem set. Use any spare minutes to run the $e_T$ sweep live.

### 118–120 · Wrap-up

Three sentences to carry, then the exit ticket. Preview: *"Next week the cell turns this rate down
on purpose, two different ways, each moving a different constant. Then the curve itself becomes a
switch."*

---

## Tailoring

- **If time runs short,** shorten the problem-set walkthrough, never the derivation. A rushed
  Michaelis-Menten derivation cannot be repaired later, because students will have encoded it as a
  ritual.
- **Do not cut the rapid-equilibrium contrast to save time either.** It is what makes the hinge
  question answerable rather than guessable, and it is fifteen minutes.
- **If the room is quick,** run the $e_T$ sweep live at the end and let them predict the gap before
  seeing it.
- **Language.** *Complex*, *quasi-steady-state*, *saturating*, *half-saturating*, *turnover* go on
  the board and stay.

---

## Alignment check

| Stage 1 outcome | Assessed in Stage 2 | Taught in Stage 3 | ✓ |
|---|---|---|---|
| Mass action on the elementary steps; enzyme conservation | Minute-40 cold call; task L1 | 25–45 | ✓ |
| State the QSSA, both reasons, and why it is not constant | Minute-62 cold call; exit ticket; task L1 | 45–65 | ✓ |
| Derive Michaelis-Menten, naming every simplification | Task L1, L2 | 80–95 | ✓ |
| Read Vmax and KM; give the binding-affinity condition | Hinge question; minute-100 cold call; task L3 | 95–112 | ✓ |

All four outcomes get both an instrument and a teaching block. Kinetic order is now taught and
assessed in L06, where it measures how switch-like a response is; two-substrate reactions are
reference material.

## Sources

Built from the wiki pages listed in `draws_on`, which trace to
[[ingalls-ch03-biochemical-kinetics]] §3.1.1 (Figures 3.3, 3.4; equations 3.1–3.5, 3.8, 3.9;
Exercises 3.1.1, 3.1.3) and §3.1.2, and to [[ingalls-ch02-reaction-networks]] §2.2 for the
reduction techniques. Michaelis and Menten (1913); Briggs and Haldane (1925); rigorous treatment of
the QSSA in Segel and Slemrod (1989). Design framework: Wiggins & McTighe, *Understanding by
Design*; constructive alignment per Biggs & Tang; fading sequence per Renkl & Atkinson.
