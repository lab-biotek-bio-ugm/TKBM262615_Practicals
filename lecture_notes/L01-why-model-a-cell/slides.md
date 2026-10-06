---
title: Why Model a Cell?
subtitle: TKBM262615 - Lecture 1
author: Matin Nuhamunada
date: 2026-09-09
---

<!-- layout: quote -->
> ...the probability of any one of us being here is so small that you'd think the mere fact of
> existing would keep us all in a contented dazzlement of surprise... You'd think we'd never stop
> dancing.
> -- Lewis Thomas, The Lives of a Cell
<!-- notes: read it aloud, no commentary. Let the silence sit for a second before moving on. -->

---

<!-- layout: section -->
# Six lectures, one question each
<!-- notes: one slide, the syllabus through-line table. Do not linger; this is orientation. -->

---

# You know exactly what every part does
- A sensor reads the temperature
- A switch compares it to a set point
- A heater turns on or off
- Can you predict the temperature of the room?
<!-- notes: everyone says yes. Hold for the next slide. -->

---

# The thermostat is in the hallway
- The heater is upstairs
- Sit with the silence
- You will have an answer by minute 55
<!-- notes: the emotional hook. Do not explain it yet. -->

---

<!-- layout: section -->
# Part 1 - What systems biology claims

---

# Fifty years, one molecule at a time
- Not a philosophy - what the instruments allowed
- ~2000: high-throughput methods, the genome draft
- Suddenly: the whole network, at once
<!-- notes: historical arc, gentle, not a revolution. -->

---

# The claim is structural, not a complaint
- Knowing every part does not tell you the whole
- Behaviour can be qualitatively different from the parts
- "Biology done with computers" is a different subject
<!-- notes: two boxes on the board - "what each part does" / "what the network does". Ask what bridges them. Accept "adding up" and hold it for later. -->

---

<!-- layout: two -->
# Reverse or forward engineering?
::: left
- Reverse: infer mechanism from behaviour
- The default when the network already exists
::: right
- Forward: infer behaviour from proposed mechanism
- Synthetic biology - building what didn't exist
<!-- notes: selection is not design - state the limit of the engineering analogy out loud. -->

---

<!-- layout: section -->
# Part 2 - The cartoon and its ambiguity

---

# A drawing is how biology records what it knows
- Plain arrow: conversion or production
- Double arrow: reaction runs both ways
- Blunt arrow: inhibition
- Dashed line: regulation - the regulator isn't consumed
<!-- notes: draw Figure 1.1 on the board - A + B binds reversibly, complex inhibits C to D. -->

---

# What happens to D if you double B?
- Take three answers from the room
- Do not resolve them
- None of you can be shown wrong from this picture
<!-- notes: this is the emotional centre of the lecture. Do not rush it. Cold call, minute ~20. -->

---

<!-- layout: section -->
# Part 3 - Complexity and feedback

---

# A system is anything that talks to itself
- Interacting components, plus a boundary
- One stone: not a system
- A slope of stones that push each other: a system
<!-- notes: Kelly's definition. A cell membrane is the boundary example. -->

---

# Complex does not mean complicated
- A jet engine: many parts, not complex
- Complex: qualitative behaviour from quantitative structure
- Two ingredients: nonlinearity and feedback
<!-- notes: kill the misconception in the first minute of this section. -->

---

# Negative feedback stabilises... usually
- The thermostat: too warm, heating off
- The rule: self-regulation, homeostasis
- The exception: a **lag** can make it oscillate
<!-- notes: this exception is the material, not a footnote. -->

---

# Positive feedback explodes... usually
- Promotes its own activity - a microphone screech
- The exception: **saturation** makes it latch
- Latching is memory
<!-- notes: pair with the previous slide - one table, two rows. -->

---

<!-- layout: picture -->
# Same loop, more lag each time
![The same negative feedback loop, with more lag each time](../../build/l01-feedback-lag.png)
Nothing changes but when the correction arrives.
<!-- notes: draw the hallway-thermostat trace with the room first: they will draw an oscillation unprompted. Then reveal this. -->

---

# The hinge question
$$\frac{dx}{dt} = \frac{1}{1+x(t-\tau)^{n}} - k\,x(t)$$
- One negative loop, no other regulation, sustained oscillation
- A: the diagram is wrong  B: there is a delay
- C: negative feedback always oscillates  D: a hidden loop
<!-- notes: mini-whiteboards. B is correct. If more than a third pick A, go back to the thermostat. -->

---

<!-- layout: section -->
# Part 4 - What a model buys you

---

# A model is an abstraction, on purpose
- Shows the bonds, hides the polarity
- Mechanistic: parts stand for real parts
- Descriptive: fits data, explains little
<!-- notes: ball-and-stick molecule analogy. This course builds mechanistic models from L03. -->

---

# Four returns, in increasing order of surprise
- It audits your biology
- It communicates without ambiguity
- It's a hypothesis you can compute cheaply
- A negative result falsifies the biology it was built on
<!-- notes: slow down on the fourth. That's the strongest claim in the chapter. -->

---

# How you'll know if it's working
- Wrong question: "is the model right?"
- Right question: "what does it commit us to?"
- What would make you abandon it?
<!-- notes: if a student can't answer the last one, they're holding a belief, not a hypothesis. -->

---

# Simulation shows how; analysis shows why
$$\frac{d[A]}{dt} = k_0 - k_1[A]$$
- Simulate: pick numbers, run it, read the curve
- Analyse: set the derivative to zero, solve once
<!-- notes: run the simulation live with three parameter choices, then the one-line analysis. -->

---

# One line, every case at once
$$[A]^{ss} = \frac{k_0}{k_1}$$
- Doubling production doubles the steady state
- True for every $k_0$, $k_1$ - not just the ones you tried
<!-- notes: "I ran it a thousand times and it settled - have I shown it always settles?" No. -->

---

<!-- layout: section -->
# Part 5 - Four case studies, four uses

---

# 1. Finding a target - T. brucei glycolysis
- Sleeping sickness; the parasite's enzymes differ from ours
- Five good drug targets found
- Three widely-believed targets ruled out
<!-- notes: ask what that negative result would have cost to find out in the lab. -->

---

# 2. Explaining a design - NF-kB oscillation
- Negative feedback: NF-kB drives its own inhibitor, IkB
- Three IkB isoforms, not one - why?
- One for speed, two to stop speed meaning instability
<!-- notes: callback to the lagged feedback figure directly. -->

---

# 3. Designing before building - the toggle switch
- Mutual repression: two negatives, one positive loop
- Symmetric case: intuition works
- Asymmetric case: the model found the two conditions that matter
<!-- notes: trace the loop aloud with the room - "1 represses 2, so less 2, so more 1." -->

---

# 4. Proving sufficiency - Hodgkin-Huxley
- Channels measured; would they produce an action potential?
- Two stimuli, 3% apart
- One relaxes back; the other fires
<!-- notes: ask the room to predict the second response before revealing it. Nearly everyone guesses "a bit bigger." -->

---

<!-- layout: section -->
# Part 6 - What's being left out

---

# This course is deterministic
- Same conditions in, same answer out, every time
- Fair when molecule counts are large
- Fails for a gene present in one or two copies
<!-- notes: ask how many copies of a protein are in a cell, then how many copies of the gene. The gap is the point. -->

---

# Back to the thermostat
- You said yes, you could predict the room
- Then the thermostat moved to the hallway
- A lag turned a stabilising loop into an oscillating one
<!-- notes: compare with their answer at minute 5. -->

---

# What to carry into L02
- Parts don't determine the whole
- A diagram is ambiguous wherever there's feedback
- A model is a hypothesis you can compute - and falsify
<!-- notes: preview - "next week we take the derivative apart, because everything after is a statement about a rate." Issue the performance task. -->
