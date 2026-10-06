---
title: The Mathematical Toolkit
subtitle: TKBM262615 - Lecture 2
author: Matin Nuhamunada
date: 2026-09-16
---

<!-- layout: quote -->
> Differential equation models of biochemical and genetic systems are invariably nonlinear.
> -- Brian Ingalls, Mathematical Modelling in Systems Biology
<!-- notes: read it aloud. This is the sentence that makes the rest of the lecture necessary. -->

---

# Retrieval - what L01 left you holding
- Where did verbal reasoning about a network go wrong?
- Does negative feedback always stabilise?
- Name one thing a model bought last week
<!-- notes: from memory, no notes. Posted after L01. -->

---

# How fast is it changing right now?
- A measured time course, no formula
- Pick a point - steeper means faster
- You already have the intuition; today it gets units
<!-- notes: sketch a rising, bending curve on the board. Point to a spot on the bend. -->

---

<!-- layout: section -->
# Part 1 - The derivative, as a rate

---

# Two points make a slope
$$\frac{5\text{ mM} - 2\text{ mM}}{20\text{ s} - 10\text{ s}} = 0.3\ \text{mM}\cdot\text{s}^{-1}$$
- Rise over run - a slope with units
- Now ask for the rate at one instant, not an average
<!-- notes: build this on the board from two real numbers before naming anything. -->

---

# Shrink the interval
- Move the second point closer to the first
- The line through them pivots onto the tangent
- 0/0 says nothing - the limit is what it approaches
<!-- notes: do this by hand on the board, several times, before showing (B.2). -->

---

# The derivative, defined
$$\left.\frac{d}{dx}f(x)\right|_{x=x_0} = \lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$$
- A number at a point; a function without the bar
- It has units, every time
<!-- notes: ask the essential question cold - "5 mM, derivative -0.2 mM/s, more or less in one second?" -->

---

# Worked: d/dx(x^2) at x=3, from scratch
$$\frac{x^2-9}{x-3} = \frac{(x-3)(x+3)}{x-3} = x+3 \;\to\; 6$$
- Cancel because the limit never looks at x=3 itself
- Matches the power rule: 2x at x=3 is also 6
<!-- notes: the definition earning its keep once, before you stop using it directly. -->

---

<!-- layout: section -->
# Part 2 - Rules, and reading shapes

---

# Ten rules, so you stop using the limit
- Constant, identity, power, exp, log
- Scalar multiple, addition - this is linearity
- Product, quotient, chain - where it isn't
<!-- notes: hand out the table. Do not lecture it. -->

---

# The derivative tells you the shape
$$r(s)=\frac{2s}{s+4} \;\Rightarrow\; \frac{dr}{ds}=\frac{8}{(s+4)^2}$$
- Positive everywhere, shrinking as s grows
- That's a saturating curve's fingerprint
<!-- notes: work this live, then spend the saved time on what the derivative's shape means. -->

---

# Same idea, one variable at a time
$$v([A],[B]) = k[A][B] \;\Rightarrow\; \frac{\partial v}{\partial[A]} = k[B]$$
- Freeze the other variable, differentiate as usual
- Curly d = "something was held fixed", nothing more
<!-- notes: no B present, no sensitivity to A - satisfying that the maths says so unprompted. -->

---

<!-- layout: section -->
# Part 3 - The hinge question

---

# What happens in the next second?
$$\frac{d[A]}{dt}=-0.2\text{ mM/s at }[A]=5\text{ mM}$$
- A: exactly 4.8 mM  B: approximately 4.8, worse over time
- C: decreases, can't say how much  D: -0.2 mM lower
<!-- notes: mini-whiteboards. B is correct - A is the Euler-method error, one lecture early. Break after. -->

---

<!-- layout: section -->
# Part 4 - State and parameter

---

# Label every symbol
$$\frac{d\mathbf{x}}{dt} = f(\mathbf{x},\mathbf{p})$$
- x: state, what the model tracks - moves
- p: parameters, fixed for one run - doesn't move
<!-- notes: four minutes, non-negotiable. Include t explicitly. -->

---

# The same enzyme, two answers
- Minutes-scale metabolic model: enzyme is a parameter
- Hours-scale gene-regulatory model: enzyme is a state variable
- Nothing about the enzyme changed
<!-- notes: cold call - "ten seconds, variable or parameter? ten hours?" -->

---

<!-- layout: section -->
# Part 5 - Linear is the exception

---

# The test for linearity
$$f(x_1+x_2)=f(x_1)+f(x_2) \qquad f(cx)=c\,f(x)$$
- kx passes both
- x^2 fails - a cross-term appears
<!-- notes: expand (x1+x2)^2 on the board and point at 2*x1*x2. -->

---

# Even the simplest chemistry is nonlinear
- Mass action for A + B -> C is k[A][B]
- A product of variables always fails the test
- No linear model has two stable states
<!-- notes: why can't a linear model have two stable states? no proof expected. -->

---

<!-- layout: section -->
# Part 6 - Local versus global

---

# A curve, seen closely, is a line
$$f(x) \approx f(x^*) + f'(x^*)(x-x^*)$$
- Value at the point, plus slope times displacement
- Good near x*, degrades away from it
<!-- notes: "intuition might suggest this is too handicapped to be useful" - state the objection before answering it. -->

---

<!-- layout: picture -->
# Local means local
![Local means local: the tangent line, and where it breaks](../../build/l02-local-linear.png)
x=1.1: off by 0.001. x=5: predicts above the ceiling.
<!-- notes: walk the x-axis with the room - "still good? still good?" - until they say no. -->

---

<!-- layout: section -->
# Part 7 - Just enough linear algebra

---

# Rows first, then columns
$$M \cdot y = [\,-49,\; -10,\; -6\,]^T$$
- A matrix-vector product is one inner product per row
- The shape rule follows from that, not a separate fact
<!-- notes: do the 3-by-4 times 4-by-1 by hand, room calling out each row. Last hand computation - NumPy after. -->

---

# A surprise: nonzero times nonzero is zero
$$[\,1,\;-1\,]\cdot[\,2,\;2\,]^T = 0$$
- For numbers this can't happen
- For vectors, contributions cancel
<!-- notes: let the room sit with the surprise for a second before defining anything. -->

---

# The nullspace is a conservation law
- Mv = 0: v is in the nullspace of M
- Closed under scaling and combination - a whole space
- Next week: a real network, a real conservation law
<!-- notes: do not build a reaction-network example yet - promise it for L03. -->

---

<!-- layout: section -->
# Part 8 - Putting it to work

---

# You already know every symbol here
```
sol = solve_ivp(rhs, (0, 20), [0.0], args=(k0, k1))
```
- rhs is f, (0,20) is the time span, [0.0] is x(0)
- args=(k0, k1) is p - passed in, not global
<!-- notes: run this live. How the solver steps is L04's job, in full, once L03 gives it a real model. -->

---

# What to carry into L03
- A derivative is a rate with units, always
- Variable or parameter depends on the time-scale
- A product of variables is nonlinear - even the simplest one
<!-- notes: preview - "next week, a list of reactions becomes this equation, arrow by arrow." Issue the performance task. -->
