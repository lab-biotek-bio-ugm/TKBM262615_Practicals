# L01 — Why Model a Cell?

*TKBM262615, Lecture 1. Draws on [[systems-biology]], [[synthetic-biology]], [[complex-system]],
[[feedback]], [[interaction-diagram]], [[dynamic-mathematical-model]],
[[simulation-versus-analysis]], [[saturation]], [[deterministic-and-stochastic-models]], and the
four case studies below. Source: Ingalls Ch. 1.*

> ...the probability of any one of us being here is so small that you'd think the mere fact of
> existing would keep us all in a contented dazzlement of surprise... The normal, predictable state
> of matter throughout the universe is randomness, a relaxed sort of equilibrium, with atoms and
> their particles scattered around in an amorphous muddle. We, in brilliant contrast, are
> completely organized structures, squirming with information at every covalent bond... You'd think
> we'd never stop dancing.
>
> — Lewis Thomas, *The Lives of a Cell*

By the end of this lecture you should be able to:

1. State what makes a model *dynamic*, and what a dynamic model commits you to.
2. Give one example where verbal reasoning about a network gives the wrong answer.
3. Distinguish a model used for prediction from one used for explanation.

There is almost no algebra in this lecture. The point of L01 is not to teach modelling — it is to
make you believe modelling is necessary, so that L02 onward feels earned rather than imposed.

## The hook

You know exactly what every component of a household thermostat does: a sensor reads the
temperature, a switch compares it to a set point, a heater turns on or off. Given that, can you
predict the temperature of the room?

Almost everyone says yes. Now add one fact: the thermostat is in the hallway, and the heater is
upstairs.

Hold that. You will come back to it in twenty minutes, and it will have an answer you did not
expect.

## What systems biology actually claims

For most of the twentieth century, molecular biology studied one molecule at a time. That was not
a philosophical stance — it was what the instruments allowed. Watching a single protein or a single
interaction closely was already a full research program.

Around 2000, high-throughput methods changed what was observable. You could suddenly watch many
molecular species at once, and the landmark result was the first draft of the human genome. What
that revealed was not "biology is complicated." It revealed something sharper: **knowing what every
part of a network does does not tell you what the network does.**

That is [[systems-biology|systems biology's]] actual claim. It is not "biology done with
computers" — that description fits bioinformatics, which processes sequence data, and is a
different subject. Systems biology studies intracellular processes as **dynamic systems**, using
models that mimic their behaviour over time.

Put two boxes on the board: *what each part does*, and *what the network does*. The naive bridge
between them is "you add the parts up." Hold that answer — it fails by the end of this hour.

The book draws a limited analogy to engineering: biological systems exist because they carry out
functions, so you can ask about their efficiency and robustness the way you would for a machine.
But the analogy has a hard stop: natural selection is nothing like rational engineering design.
Where you're confident of a network's function, studying it is **reverse engineering**. Where
you're not, borrowing engineering intuition will mislead you. Building networks that did not exist
before — the forward direction — is [[synthetic-biology|synthetic biology]], and you'll meet its
first product later this lecture.

## The cartoon and its ambiguity

Biology's standard way to record what it knows about a network is a drawing: an
[[interaction-diagram]], also called a cartoon model. Ingalls' Figure 1.1 is the reference example:
two species, A and B, bind reversibly to form a complex, and that complex inhibits the rate at
which a third species, C, converts to a fourth, D.

Four conventions carry the whole notation, and you will use them again in L03:

| Symbol | Means |
|---|---|
| plain arrow | conversion or production: the tail becomes, or makes, the head |
| double-headed arrow | the reaction runs both directions |
| blunt-ended arrow | inhibition |
| dashed line | a *regulatory* interaction — the regulator is not consumed |

That last row is the one people miss. A dashed, blunt arrow from the complex to the C→D reaction
says the complex slows that reaction without being used up by it. Solid means matter is flowing;
dashed means influence is flowing, with nothing changing hands.

**Now the question:** what happens to D if you double the supply of B?

Look at the diagram. Write down an answer. You cannot be shown wrong by the picture alone — and
that is not a compliment to the picture. Ingalls states the problem directly:

> A drawback of these cartoon models is that they can leave significant ambiguity regarding system
> behaviour, especially when the interaction network involves feedback.

The diagram tells you A and B bind. It does not tell you how fast, or how tightly — and those
numbers can change the answer not by a little, but qualitatively. Two people can read the same
picture and defend opposite predictions, both reasonably. That gap is the argument for the rest of
this course: turning the cartoon into a [[dynamic-mathematical-model|dynamic mathematical model]]
removes the ambiguity, at a price — you must supply a number for every interaction. For many
cellular processes, that price cannot yet be paid, and this book says so rather than pretending
otherwise.

## Complexity and feedback

### What makes a system

A system, for this course, is a collection of **interacting components** plus a **boundary**.
Kevin Kelly's definition is the one worth keeping: a system is "anything that talks to itself." One
stone sitting on a slope is not a system. A slope of stones that can push each other is, because
now the components act on one another. A cell membrane is a boundary in exactly this sense — it
separates what counts as the system from what counts as environment.

A system is **complex** when its overall behaviour cannot be understood intuitively from its
components. This is not the same claim as "has many parts" — a jet engine has thousands of parts
and is not complex in this sense, because you can still reason your way from the parts to the
whole. The defining feature of a complex system, stated precisely, is this:

> The qualitative nature of a complex system's behaviour can depend on quantitative differences in
> its structure.

Read that twice. It does not say behaviour changes "somewhat." It says a small change in a number
can produce a *different kind* of behaviour — oscillating instead of settling, two stable states
instead of one. Two ingredients produce this, and you need both: nonlinear interactions, and
**feedback loops**. Neither alone is usually enough.

### Feedback, and the exceptions that matter

Feedback is a component acting on its own activity, through the rest of the network. Two flavours,
each with a rule everyone learns and an exception that this course actually cares about.

**Negative feedback.** A component inhibits its own activity — the thermostat again: too warm,
heating off. The rule: negative feedback loops "generally stabilize system behaviour; they are the
key feature of self-regulation and homeostasis." The exception is the sentence people skip:

> Instability and oscillations can arise when there is a **lag** in the action of a negative
> feedback loop.

**Positive feedback.** A component promotes its own activity, and this typically runs away — the
screech when a microphone hears its own amplifier. The exception:

> When constrained by saturation effects, positive feedback can serve as a mechanism to 'lock in' a
> system's long-term behaviour — thus providing a **memory** of past conditions.

| The rule you'll want to memorise | Where it breaks |
|---|---|
| "Negative feedback stabilises" | With a lag, it oscillates |
| "Positive feedback explodes" | With [[saturation]], it latches into memory |

Both exceptions turn on quantities — how much lag, how hard a ceiling — that an
[[interaction-diagram]] never carries. This is the same ambiguity from the last section, now with a
name.

### Seeing the lag, not just being told about it

Here is a single loop: a protein represses its own production. Nothing changes between the three
panels below except **when** the correction arrives.

Let $x(t)$ be the concentration of this protein at time $t$, in arbitrary units — there is no real
protein here, this is a minimal model built to isolate one effect, not a measurement from the book.
The protein represses its own production, and the loop is:

$$\frac{dx}{dt} = \underbrace{\frac{1}{1 + x(t-\tau)^{n}}}_{\text{production, from repression}} - \underbrace{k\,x(t)}_{\text{decay}}$$

Read every symbol before going further:

- $x(t-\tau)$ is the protein's concentration **not now, but $\tau$ time units ago** — the delayed
  value. $\tau$ (Greek tau) is the **lag**, in the same time units as $t$.
- The production term is a saturating, switch-like function of that delayed concentration (the
  sigmoidal shape from [[saturation]]): production is at its maximum, $1$, when the delayed
  concentration is zero, and falls toward zero as the delayed concentration grows. The exponent $n$
  sets how sharp that switch is; here $n = 6$.
- $k$ is a first-order decay rate constant, in units of $\text{time}^{-1}$: the fraction of $x$
  removed per unit time, independent of everything else. Here $k = 1$.

This is exactly the loop from [[feedback]] — a component repressing its own production — with one
knob added: $\tau$. Nothing about the strength of the repression or the rate of decay changes across
the three cases below. Only the delay does.

The equation has $x(t-\tau)$ in it, which an ordinary differential equation solver like
`scipy.integrate.solve_ivp` cannot handle directly — it needs the whole recent history of $x$, not
just its current value. L02 introduces `solve_ivp` properly; here the delayed value is just held
fixed across each small time step while stepping forward, which is enough to see the qualitative
point.

![The same negative feedback loop, with more lag each time](../../build/l01-feedback-lag.png)

*(Regenerated by `figs/feedback_lag.py`; the "settles / rings / oscillates" labels are measured
from the simulation and asserted in the script, not asserted by eye.)*

No lag, and the loop settles to a steady value. A little lag, and it overshoots, corrects, and
rings before settling — like a car's suspension after a bump. More lag, and it never settles: the
correction always arrives late enough to overshoot the target, forever. **The loop, its strength,
and every rate constant are identical in all three panels.** The only thing that changed is when
the correction arrives — which is your hallway thermostat.

> [!question]- Hinge question
> A signalling pathway has a single negative feedback loop and no other regulation. Its output
> **oscillates** for hours. What is the most likely explanation?
>
> **A.** The feedback is actually positive — someone drew the diagram wrong.
> **B.** There is a delay in the feedback.
> **C.** Negative feedback always oscillates; this is normal.
> **D.** There must be a second, hidden loop.
>
> **Answer: B.** A believes the "stabilises" rule is absolute, so an oscillation must mean a
> drawing error. C over-corrects from this lecture and loses the default case — negative feedback
> usually *does* stabilise. D is reasonable systems thinking, but reaches for extra machinery before
> asking what the one loop you were given can already do.

## What a model is, and what it buys you

A [[dynamic-mathematical-model]] is a set of equations describing how a system changes over time,
written from the underlying mechanism, and treated as a hypothesis whose consequences you can
compute.

Every model is an abstraction — Ingalls' example is a ball-and-stick model of a molecule. It shows
you the bonds and hides the polarity. That is not a flaw; a model that kept everything would be the
thing itself, and no easier to reason about than the cell you started with.

Two kinds matter here:

- **Mechanistic**: each part of the model stands for some part of the real system. Change a model
  component and you have mimicked changing the real thing. This is the only kind that answers "what
  if we inhibit this enzyme?" — and it is what this course builds, starting in L03.
- **Descriptive**: a fitted curve summarising data. It reproduces what you already measured and
  tells you little about why. Useful, but not what this course is about.

Moving from a cartoon to a model has a real cost: a number for every interaction in the diagram.
What you get for that cost, in increasing order of how surprising it is:

1. **Building it audits your biology.** Writing the equations forces you to state the mechanism
   precisely, and precision exposes gaps the cartoon hid.
2. **It communicates unambiguously.** Two people reading the same equations get the same model.
   Two people reading the same cartoon, as you just saw, often do not.
3. **It is a working hypothesis you can interrogate cheaply.** You can compute what it predicts, at
   no cost, under conditions no laboratory could produce, observing every variable at every time
   point.
4. **A negative result falsifies the biology.** Because a model can be investigated exhaustively, a
   model that cannot reproduce an experiment falsifies the assumptions it was built from. The
   biology gets refined, then the model, then the next experiment.

The natural question to ask about a model is not "is it right?" A model is a hypothesis, not a
verdict — a cartoon is a hypothesis too, the difference is that you can compute this one's
consequences. The better question: "what does this model commit us to, and does the cell agree?"
A useful check on your own thinking: if you cannot say what observation would make you abandon a
model, you are holding a belief about it, not a hypothesis.

## Simulation versus analysis, in ninety seconds

Once you have a model, there are two ways to interrogate it.

**Simulate it.** Choose parameter values and initial conditions, run a numerical solver, and read
off the time course. Cheap, fast, complete: you see every variable at every time point.

**Analyse it.** Work on the equations themselves and derive a statement that holds for a whole range
of conditions at once — harder, and it needs more mathematics, but the payoff is bigger.

> Whereas simulations indicate **how** a system behaves, model analysis reveals **why** a system
> behaves as it does.

One tiny model makes the difference concrete. A single species produced at a constant rate and
degraded in proportion to its own amount:

$$\frac{d[A]}{dt} = k_0 - k_1[A]$$

Name the symbols: $[A]$ is the concentration of species A, in some concentration unit; $k_0$ is a
zero-order production rate, in $\text{concentration}\cdot\text{time}^{-1}$; $k_1$ is a first-order
decay rate constant, in $\text{time}^{-1}$. Check the units balance: $k_1[A]$ has units
$\text{time}^{-1}\cdot\text{concentration} = \text{concentration}\cdot\text{time}^{-1}$, matching
$k_0$ and matching the left-hand side, $d[A]/dt$. This kind of check costs one line and catches a
real class of mistakes.

**By simulation:** pick $k_0 = 2$ and $k_1 = 0.5$, start from $[A] = 0$, integrate forward, and
watch the curve flatten out near $4$. Pick different numbers, get a different curve. You have
learned one fact per run.

**By analysis:** you want the value $[A]$ settles to — its [[steady-state|steady state]] — which by
definition is where nothing is changing anymore, so you set the derivative to zero and solve:

$$0 = k_0 - k_1[A]^{ss} \;\Longrightarrow\; [A]^{ss} = \frac{k_0}{k_1}$$

One line, and it holds for *every* pair of values: doubling the production rate doubles the steady
state, and the steady state does not depend on where you started. Fifty simulations might have
suggested that pattern. This proves it.

```python
# /// script
# dependencies = ["numpy", "scipy"]
# ///
"""L01 demo — simulation and analysis agree on the steady state of dA/dt = k0 - k1*A.

Run: uvx --with numpy --with scipy python notes_demo.py
"""
import numpy as np
from scipy.integrate import solve_ivp


def rhs(t, A, k0, k1):
    return [k0 - k1 * A[0]]


def main():
    k0, k1 = 2.0, 0.5                      # concentration/time, 1/time
    sol = solve_ivp(rhs, (0, 40), [0.0], args=(k0, k1), dense_output=True)
    simulated = sol.y[0, -1]
    analysed = k0 / k1
    assert abs(simulated - analysed) < 1e-3, (simulated, analysed)
    print(f"simulation at t=40: {simulated:.4f}   analysis, k0/k1: {analysed:.4f}")


if __name__ == "__main__":
    main()
```

Neither tool replaces the other. Most models in this book are nonlinear enough that a closed-form
analysis like this one is not available, which is exactly why L04 spends real time on numerical
simulation. Analysis wherever you can get it, simulation everywhere else, and each used to check
the other.

*(Ten-minute break here.)*

## Four case studies, four different uses of a model

Same message across all four: the biology differs, but each shows a **different job a model can
do**. The point is the use, not the mechanism — you are not expected to remember the biochemistry.

### 1. Finding a drug target — *Trypanosoma brucei* glycolysis

*T. brucei* causes sleeping sickness, and as a eukaryote it is not susceptible to bacterial
antibiotics. Its energy metabolism (glycolysis) is essential to both the parasite and its human
host — normally a hopeless drug target — except that the parasite's version of these enzymes
differs enough from the human one that a drug could hit one and largely spare the other.

The question, which is a question about [[steady-state|steady-state]] behaviour, is which enzyme to
target. Bakker and colleagues (1999) built a model and used it to test how the pathway's output
responds to perturbing each enzyme in turn. The result: five enzymes were confirmed as good
targets, and **three enzymes that had been widely believed to be good targets turned out not to
be** — inhibiting them barely moved the pathway's output.

The negative result is the more valuable half. Three reasonable, widely held beliefs were wrong,
and the model found that out before anyone spent years of a drug-discovery program discovering it
in the lab. *What a model bought here: it found something — including what was not there.*

### 2. Explaining a design choice — NF-κB oscillation

NF-κB is a transcription factor involved in cell division, inflammation, and cell death. At rest it
is held inactive by inhibitor proteins called IκB; a stimulus degrades IκB, NF-κB acts, and NF-κB
in turn drives production of more IκB — a [[feedback|negative feedback]] loop that shuts the
response off.

Here is the puzzle: there are *three* IκB isoforms, not one, and knocking out different ones gives
qualitatively different results. With all three present, the wild-type cell shows a
quickly-damped oscillation settling to a steady active level. Remove one isoform and the response
becomes pathologically high. Remove the other two and the oscillation never damps.

Hoffmann and colleagues (2002) used a model to take the loop apart, and found the division of
labour: one isoform provides feedback fast enough to quench the response quickly — fast enough that
on its own it would overshoot and oscillate, exactly the lag problem you just watched in the
feedback figure. The other two provide a steadier, non-oscillating brake that damps that overshoot.
One inhibitor for speed, two more to stop speed from meaning instability. *What a model bought
here: it explained why the network needs a part that a diagram alone gives no reason for.*

### 3. Designing before building — the Collins toggle switch

A toggle switch flips between two stable states and stays flipped until told otherwise — it is
**bistable**. Gardner, Cantor and Collins (2000) built the first engineered genetic version: two
genes, each repressing the other.

Trace the loop out loud: gene 1 represses gene 2, so less gene 2 means less repression of gene 1,
so more gene 1. Each protein indirectly promotes itself — this is [[feedback|positive feedback]],
built entirely out of two negative interactions. What keeps it from running away is
[[saturation]]: repression cannot exceed complete, and expression cannot exceed maximal. Positive
feedback with a ceiling is exactly what latches into memory.

If the two genes were symmetric, intuition would be enough. They could not be symmetric — the
designers had to choose from the small set of genes already characterised in the lab — and once
asymmetric, intuition has nothing to say: the stronger repressor might simply always win, and then
there is no switch, just one gene permanently on. This is [[complex-system|complexity]], stated as
an engineering problem rather than an observation.

Rather than build and test every combination on the bench, Gardner and colleagues built a simple,
generic model first, and it told them two things: bistability fails below a threshold expression
rate, even in the symmetric case; and enough nonlinearity in the gene-repression interaction can
compensate for asymmetry. Guided by those two facts, they built working switches. *What a model
bought here: the design itself, before a single cell was constructed.*

### 4. Proving a mechanism sufficient — Hodgkin and Huxley

Neurons signal by changing the voltage across their membrane; an **action potential** is a sweeping
change in that voltage that propagates along the cell. Hodgkin and Huxley (1952) had measured that
membrane permeability to different ions is ion-specific, and correctly inferred that this reflects
distinct, voltage-sensitive channels. The proposed loop — voltage changes permeability, permeability
changes ion flow, ion flow changes voltage further — is feedback in both directions at once, and no
amount of staring at that loop tells you whether it *produces* an action potential.

So they built a model of membrane voltage and ion transport from the measured channel properties —
not fitted to reproduce an action potential, but built from independent measurements, which is why
what came out is evidence and not a foregone conclusion. Two brief voltage stimuli, one just 3%
stronger than the other: the weaker one relaxes back to rest and nothing happens; the stronger one
produces a full action potential, a dramatic and categorically different response. A 3% change in
input, a different *kind* of output — [[complex-system|complexity]], measured. *What a model
bought here: proof that a proposed mechanism was capable of the behaviour at all.*

## The honest boundary: this course is deterministic

Everything above assumes a **deterministic** model: run it twice under identical conditions and you
get the identical answer, to the last digit. A **stochastic** model instead produces a distribution
— each run is one sample, and you need many runs to see the shape.

Deterministic models are far more tractable to simulate and to analyse, which is the practical
reason this course uses them. The assumption behind that choice is specific: there are enough
molecules present that the randomness of individual reaction events averages away. This is
reasonable for species present in thousands of copies. It gets worse, not just less accurate, for a
gene present in one or two copies per cell, where "thermal agitation of individual molecules is a
significant source of randomness" — the noise is not a nuisance around the real behaviour, the
noise *is* the behaviour. That regime is outside this course.

> [!note] Inference
> One consequence worth stating even though the book does not spell it out in Chapter 1: a
> deterministic model of a bistable system — like the toggle switch above — predicts a population
> sitting in one state. A real population of cells may in fact be split between both states, and
> the deterministic average can describe a condition no individual cell is actually in. Attributed
> to me, not to the book.

## Where this leaves you

Return to the thermostat. You said you could predict the room's temperature, and then the
thermostat moved to the hallway. Now you have language for what happened: a negative feedback loop,
stabilising by rule, made unstable by a lag you could not see in the arrangement of parts — only in
the numbers.

Three claims to leave with:

1. The behaviour of a network does not follow from the behaviour of its parts. That is a structural
   claim about [[complex-system|complex systems]], not a complaint about how hard biology is.
2. A cartoon diagram is ambiguous about behaviour whenever there is feedback, and the ambiguity is
   removed only by supplying a number for every interaction.
3. A model is a hypothesis whose consequences you can compute — which is exactly what makes a
   failed model valuable: it falsifies the biology it was built on.

**Next lecture:** L02 takes the derivative apart, because from here on, every model in this course
is a statement about a rate.

## Problem set

### Performance task — "Two negatives" (due before L03)

Here is a two-gene circuit. Gene 1's protein represses Gene 2. Gene 2's protein represses Gene 1.
Nothing else is specified.

**(a)** Trace the loop and state its overall sign. Justify in one sentence.

**(b)** A colleague says: "Obviously this is a switch — it will sit in one of two states." Under
what circumstances are they right, and under what circumstances is the circuit useless? You may not
use any equations.

**(c)** What is the smallest piece of *quantitative* information you would ask for to settle it?

> [!success]- Model answer (don't open until you've tried it)
> **(a)** The loop is **positive**. Gene 1's protein represses Gene 2; less Gene 2 means less
> repression of Gene 1; so more Gene 1. Each protein indirectly promotes itself. Composing two
> negative effects gives a net positive effect on the loop — the same reasoning as the toggle switch
> above.
>
> **(b)** The colleague is right only if the mutual repression is *balanced enough* and
> *nonlinear enough* — exactly the two conditions the toggle-switch model found. If one repressor is
> much stronger than the other, or the repression is too weak (too close to linear), the stronger
> gene may simply win permanently: one stable state, and no switch. The diagram cannot tell you
> which case you are in.
>
> **(c)** Something genuinely quantitative: the relative strengths of the two repressions, their
> expression rates, or the steepness (nonlinearity) of each repression response. Naming the *loop
> sign* again, or restating the diagram, does not count — that information is already on the page.

### Retrieval practice — post before L02

Answer from memory, no notes:

1. Give one example from today where verbal reasoning about a network gave the wrong answer, and
   say what was wrong with the reasoning.
2. "Negative feedback always stabilises a system." Is this true? If not, what is missing from it?
3. Name one thing a model bought in one of today's four case studies, in one sentence.
