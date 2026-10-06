# L04 — Conservation and Numerical Simulation

**Practical:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/TKBM262615_Practicals/blob/main/notebooks/02_simple_networks.ipynb) `02_simple_networks`

*Source: Ingalls Ch. 2, §2.1.3 and §2.1.4.*

By the end of this lecture you should be able to:

1. State what a conservation relation is, find one in a small closed network by two different
   routes, and say why it holds for every value of the rate constants.
2. Use a conservation to eliminate one differential equation **exactly**, then find the steady
   state algebraically.
3. Derive Euler's method from the definition of the derivative, take three steps by hand, and say
   where the error comes from and how it shrinks with the step size.
4. Integrate a reaction-network model with `scipy.integrate.solve_ivp`, set tolerances
   deliberately, and say what a simulation cannot tell you that a formula can.

There is one sentence to carry from the start, because it is the spine of this lecture and the
bridge into L05: **reduction by conservation is exact.** Nothing is approximated. Next week you
will meet another reduction that looks identical on the page and is a bet. That difference matters
far more than it looks.

## Retrieval: what L03 left you holding

Answer from memory, notes closed:

1. Why is the rate for $A + B \to C$ a product, $k[A][B]$, rather than a sum?
2. A network has five species and three reactions. How many differential equations?
3. What are the units of $k$ in a second-order rate law?

<details>
<summary>Answers</summary>

1. The rate is proportional to the chance that one molecule of A collides with one molecule of B.
   The probability of two independent events happening together is the product of their
   probabilities, not the sum.
2. Five. One per species, whatever the number of reactions. Reactions contribute *terms*, not
   equations.
3. $\text{concentration}^{-1}\,\text{time}^{-1}$. Check it dimensionally: the left side
   $\frac{d[C]}{dt}$ is concentration per time, and the right side $k[A][B]$ is
   $[k] \times \text{concentration}^2$.

</details>

## The hook: count the molecules, not the concentrations

Take the irreversible conversion $A \xrightarrow{k} B$. Every time a molecule of B appears, a
molecule of A has disappeared. Nothing enters the beaker and nothing leaves it.

So the total cannot move.

That is the whole concept. The rest of this section is how to write it down, how to find it when
the network is too complicated to see, and what it buys you.

---

# Part 1 — Conservation in a closed system

## What the word "closed" buys you

A **closed** network has no inflow, no outflow, no synthesis and no degradation. All that happens
is that material is passed around among the species inside it.

**Every closed network has at least one conservation relation.** The phrase "at least one" is
doing work: a closed network with five species may well have two or three independent
conservations. An **open** network may or may not have one, and you are not entitled to assume it.

## Route 1 — read it off the arrows

Look at what gets passed along unchanged. For $A \to B$, every event moves one molecule from A to
B, so $A + B$ is fixed.

This route is fast and intuitive, and it will not last. Once the network has ten species and
fifteen arrows you will not see it. That is why the second route is the one you keep for life.

## Route 2 — add the differential equations

Write the model with mass action, exactly as in L03:

$$\frac{d[A]}{dt} = -k[A], \qquad \frac{d[B]}{dt} = +k[A]$$

Now add them. Add the left sides, add the right sides:

$$\frac{d}{dt}\left(a(t) + b(t)\right) = \frac{da}{dt} + \frac{db}{dt} = -ka + ka = 0$$

A quantity whose derivative is zero for all time is a constant. So:

$$a(t) + b(t) = T \quad \text{for all } t, \qquad T = A_0 + B_0$$

Notice where $T$ comes from: the **initial conditions**, not the rate constants. That is what makes
$T$ useful — it is a number you already know before any simulation is run.

Watching the same answer arrive twice, once through chemistry and once through algebra, is what
makes the algebraic route believable later, when the chemistry is too complicated to eyeball.

## Conserved concentration is not conserved mass

This is the main misconception on this topic, and the syllabus's own phrase "mass conservation"
invites it.

What is conserved in $a + b = T$ is a **count of molecules**, or equivalently a concentration. Is
mass conserved? Only if A and B have the same molecular mass, and they need not. Ingalls separates the two terms deliberately (p. 29), and that care is worth passing on.

> Ask yourself: what does $ATP \to ADP + P_i$ conserve? The count of adenine groups, yes. Total
> mass in a closed system, yes as well, since nothing leaves. But the concentration of ATP alone,
> clearly not.

## Structural, not parametric

Does the conservation $a + b = T$ depend on the value of $k$?

No. It holds for **every** $k$. Look back at the derivation: $k$ appeared in both terms and then
cancelled. A conservation is a property of **which arrows exist**, not of how fast they run.

This is what a **structural conservation** means, and it is the seed of everything Ch. 5 does with
metabolic network structure. The practical consequence is large: you can trust a conservation in a
model whose rate constants nobody has ever measured.

## The biological name: moiety conservation

A **moiety** is a group of atoms forming part of a molecule. Many chemical conservations are
**moiety conservations**: some chemical group is passed between molecules without ever being
created or destroyed.

Examples you already know from biochemistry:

- **Adenine nucleotides.** $[ATP] + [ADP] + [AMP]$ is effectively fixed on a timescale of minutes.
  What moves is the phosphate group.
- **Redox cofactors.** $[NAD^+] + [NADH]$ is fixed; what moves is electrons.
- **Enzymes.** An enzyme is not consumed by the reaction it catalyses, so total enzyme is fixed.
  This is the one that saves the Michaelis-Menten derivation next week. Remember it.

## Not every conservation is a sum

You will be tempted to generalise "a conservation is the sum of two concentrations". Do not.

Ingalls Exercise 2.1.8 gives a system in which one reaction produces C and D **together**. Because
they are always born in pairs, what stays fixed is their **difference**, $c - d$, not their sum.

Look for **combinations**, not totals. Route 2 will find them for you; Route 1 will not.

---

# Part 2 — Using a conservation to shrink a model

## The payoff, stated as a payoff

Systems of differential equations are much harder than single differential equations. That is not
just a feeling — in L03 you already saw that nonlinear models generally have no explicit solution
at all.

A conservation hands you one fewer equation, free:

> **Two differential equations** become **one differential equation plus one line of arithmetic.**

Solve for $a(t)$, then read $b(t) = T - a(t)$ off without solving anything further.

## Worked example — the reversible pair

Take $A \rightleftharpoons B$ with forward constant $k_+$ and reverse $k_-$:

$$\frac{da}{dt} = k_-b - k_+a, \qquad \frac{db}{dt} = k_+a - k_-b$$

The two derivatives are exact negatives, so $a + b = T$ again, by Route 2.

Now use it. Substitute $b = T - a$ into the first equation:

$$\frac{da}{dt} = k_-(T - a) - k_+a = k_-T - (k_+ + k_-)a \tag{2.12}$$

Two coupled equations have become one, in one unknown. Look at its shape: this is **exactly** the
production-and-decay model you solved in L03 and in `02_simple_networks.ipynb`, Example II, with $k_-T$
as the production rate and $(k_+ + k_-)$ as the decay constant. A network that looked new turns out
to be an old one in disguise.

## The steady state falls out

Set the derivative to zero and solve. This is **algebra, not calculus** — you never touch the
differential equation:

$$0 = k_-T - (k_+ + k_-)a^{ss} \quad\Longrightarrow\quad
a^{ss} = \frac{k_-T}{k_+ + k_-}, \qquad b^{ss} = \frac{k_+T}{k_+ + k_-} \tag{2.13}$$

**Check:** $a^{ss} + b^{ss} = \frac{(k_- + k_+)T}{k_+ + k_-} = T$. It has to be — a conservation
holds at steady state as it does everywhere else. Say that check out loud as a **requirement**, not
as a pleasant coincidence.

Notice also that only the **ratio** $k_+/k_-$ sets the split. Double both and the answer does not
move. That is exactly what `02_simple_networks.ipynb`, Example IV, shows numerically, and it is what the
hinge question below tests.

## A short aside: what a steady state is

One paragraph, because the hinge question needs it and L05 needs it. The full treatment is Ch. 4,
outside this course.

$$f(\mathbf{x}^{ss}, \mathbf{p}) = 0$$

This says: **the rate of change of every concentration is zero, all at once.** It does not say the
reactions stopped. On $\to A \to$ with production $k_0$ and decay $k_1$, the steady state is
$a^{ss} = k_0/k_1$, and both reactions are running at rate $k_0$ — equal, opposite, and not
remotely zero. Nothing is changing and everything is happening.

Three caveats worth naming once and then leaving: a steady state can exist without ever being
reached on any relevant timescale; it can be unstable, a state the system leaves; and there can be
more than one.

## The hinge question

The closed network $A \rightleftharpoons B$ starts at $a(0) = 3$ mM, $b(0) = 1$ mM. Someone doubles
**both** $k_+$ and $k_-$. Which statement is true of the new steady state?

- **A.** $T$ changes, $a^{ss}$ does not.
- **B.** Neither $T$ nor $a^{ss}$ changes.
- **C.** $T$ holds, but $a^{ss}$ changes.
- **D.** Both change.

<details>
<summary>Answer and reasoning</summary>

**B.**

$T = A_0 + B_0 = 4$ mM, set by the initial conditions. The rate constants do not touch it at all —
they cancelled out of the derivation.

And $a^{ss} = \frac{k_-T}{k_+ + k_-}$. Double $k_+$ and $k_-$: the numerator becomes $2k_-T$, the
denominator becomes $2(k_+ + k_-)$, and the factor of two cancels. Only the ratio matters.

**A** thinks rate constants can move a conserved total. **C** is the most common and most
instructive wrong answer: it gets the structural half right, then assumes that changing a parameter
must change the answer. **D** makes both errors.

What *does* change when you double both constants is the **speed** at which the system reaches that
steady state — the time constant $1/(k_+ + k_-)$ halves. Same destination, twice as fast.

</details>

## When the network is too big to see

Route 2 is really a linear-algebra computation, and once you see it that way it runs on a network
of any size.

Build the **stoichiometry matrix** $\mathbf{N}$: rows are species, columns are reactions, entries
are how many molecules of each species each reaction makes or consumes. For $A \to B$, two species
and one reaction:

$$\mathbf{N} = \begin{pmatrix} -1 \\ +1 \end{pmatrix}$$

Now look for a vector of weights $\mathbf{w}$ such that:

$$\mathbf{w}^{T}\mathbf{N} = 0 \quad\Longleftrightarrow\quad \frac{d}{dt}(\mathbf{w}\cdot\mathbf{x}) = 0$$

Read the left side as a sentence: **find the weighted combinations that no reaction disturbs.** If
nothing changes it, it is constant, and that is the definition of a conservation.

The set of such vectors is the **left nullspace** of $\mathbf{N}$ — which is where the
[[nullspace]] you met in L02 finally earns its place.

```python
# /// script
# dependencies = ["numpy", "scipy"]
# ///
"""Finding a conservation from network structure rather than by guessing."""
import numpy as np
from scipy.linalg import null_space

# A -> B: two species (rows), one reaction (column)
N = np.array([[-1.0],
              [+1.0]])

print(null_space(N.T).ravel())     # [0.707 0.707]
```

The answer is $[0.707,\ 0.707]$ rather than $[1,\ 1]$ because `null_space` normalises what it
returns. What carries meaning is the **direction**, not the scale: $[0.707, 0.707]$ is proportional
to $[1, 1]$, which reads "$a + b$". Multiply by $\sqrt{2}$ if you want to see it.

One honest limitation, which the practical explores: beyond a single conservation, `null_space`
returns an arbitrary basis for the space, and its vectors are usually mixtures with no chemical
meaning. The computation tells you *how many* independent conservations exist, which is the hard
part. Deciding which combinations are worth naming is chemistry, and `w @ N == 0` is how you check
a candidate once you have one.

## The word "exact" is doing real work here

Nothing in this reduction is approximated. The reduced model **is the same model**, written
shorter. Integrate the full system and the reduced system with tight tolerances and they will agree
to the limit of what the solver can do.

More than that: the conservation **survives simulation to machine precision**. The reason is worth
a moment. The solver computes both derivatives from the same expression, and that expression makes
them exact negatives at every step. Whatever is added to one species is subtracted from the other,
by an identical floating-point number. So $a + b$ never budges.

Notice what that argument did **not** mention: accuracy. It holds for crude Euler exactly as it
holds for a good solver. A conservation is a structural property, and structure does not care about
step size. (This week's Level 3 problem asks you about precisely this.)

Bank the sentence. Next week you will meet a reduction that looks identical on the board and
produces a **different** model.

---

# Part 3 — Euler's method

## Three lectures of trusting a black box

Since L01 you have called `solve_ivp` and accepted the curve that came out. Today the box opens.

Why numerical simulation is necessary at all, in Ingalls' own words: differential equation models
of biochemical and genetic systems are **invariably nonlinear**, and nonlinear models do not
typically admit explicit solutions. This is not a failure of cleverness. There is no formula.

## What a solver actually computes

A numerical solver does **not** compute a function. It computes a list of numbers: the
concentration at $t = 0$, at $t = h$, at $t = 2h$, and so on. The first step is choosing that
**mesh** of time points. Then you need an **update formula** to get from one to the next.

The simplest one is Euler's method, and it comes straight from the definition of the derivative.

## The derivation, in three lines

Recall from L02 that the derivative is the limit of a difference quotient. For small $h$ it is
approximately that quotient:

$$\frac{d}{dt}a(t) \;\approx\; \frac{a(t+h) - a(t)}{h}$$

Substitute it into the model $\frac{da}{dt} = f(a)$:

$$\frac{a(t+h) - a(t)}{h} \;\approx\; f(a(t))$$

Now **treat the approximation as an equality** and rearrange:

$$a(t+h) = a(t) + h\,f(a(t)) \tag{2.16}$$

That last line is the whole trick, and the step from $\approx$ to $=$ is where **all** of the error
enters. There is no other source of error in the method.

Read the result as a sentence, not as symbols:

> The new value is the old value, plus the step size times the rate of change at the old value.

A student who can say that sentence has understood Euler's method. The rest is arithmetic.

What it assumes: **the rate holds constant across the step.** It does not. That is the error.

## Three steps by hand

Do this on paper before reading the answer. Take $\frac{da}{dt} = -a$ with $a(0) = 1$ and
$h = 2/3$, and run three steps to $t = 2$.

The arithmetic


$$a(2/3) = 1 + \tfrac{2}{3}(-1) = \tfrac{1}{3}$$
$$a(4/3) = \tfrac{1}{3} + \tfrac{2}{3}\left(-\tfrac{1}{3}\right) = \tfrac{1}{9}$$
$$a(2) = \tfrac{1}{9} + \tfrac{2}{3}\left(-\tfrac{1}{9}\right) = \tfrac{1}{27} = 0.037$$

The exact value is $e^{-2} = 0.135$. Your approximation is **73%** low.

Seeing your own bad approximation is worth more than any warning about the limits of numerical
methods.

## The price of accuracy

```python
# /// script
# dependencies = ["numpy", "scipy"]
# ///
"""Euler by hand against solve_ivp, on the one model we can solve exactly."""
import numpy as np
from scipy.integrate import solve_ivp

def euler(f, y0, t_end, h):
    """Ingalls' equation (2.16), applied repeatedly."""
    n = int(round(t_end / h))          # NOT np.arange(0, t_end + h, h) -- see the note below
    ts = np.linspace(0, t_end, n + 1)
    ys = np.empty_like(ts)
    ys[0] = y0
    for i in range(n):
        ys[i + 1] = ys[i] + h * f(ys[i])
    return ts, ys

f = lambda a: -a                        # da/dt = -a, so the exact answer is exp(-t)
exact = np.exp(-2.0)

for h in (2 / 3, 1 / 3, 1 / 30):
    _, ys = euler(f, 1.0, 2.0, h)
    print(f"h={h:6.4f}  euler={ys[-1]:.6f}  exact={exact:.6f}  error={abs(ys[-1] - exact):.6f}")

ref = solve_ivp(lambda t, y: [-y[0]], [0, 2], [1.0], rtol=1e-12, atol=1e-14)
print(f"solve_ivp  error={abs(ref.y[0, -1] - exact):.2e}")
```

Output:

```
h=0.6667  euler=0.037037  exact=0.135335  error=0.098298
h=0.3333  euler=0.087791  exact=0.135335  error=0.047544
h=0.0333  euler=0.130799  exact=0.135335  error=0.004536
solve_ivp  error=5.75e-14
```

Two things to draw out of those numbers.

**Halving $h$ halves the error.** From 0.0983 to 0.0475. That is what "first-order method" means,
and it is a bad deal: ten times the work for ten times the accuracy. To gain three more digits you
would run a thousand times as many steps.

**`solve_ivp` is twelve orders of magnitude better** than Euler at $h = 1/30$, because it uses a
higher-order method with an adaptive step size. Euler is for **understanding**, not for using.

## Euler can also go unstable

If $h$ is too large the numerical answer oscillates or grows, while the true solution decays
quietly the whole time. Try $\frac{da}{dt} = -a$ with $h = 2.5$: the values alternate in sign and
grow without bound.

That is a property of the **method**, not of the biology. It is also why real solvers choose their
own step size rather than leaving it to you.

## A mesh bug worth seeing fail once

The obvious way to build the mesh, `np.arange(0, t_end + h, h)`, is **wrong**.

With $h = 1/3$ and $t_{end} = 2$, floating-point rounding lets `arange` emit a final point at
$t = 2.333$. Your loop takes **seven** steps instead of six and reports the concentration at the
wrong time.

The symptom is subtle, which is what makes it dangerous: the answer is still a plausible number,
and the error **stops halving** when you halve $h$. That looks like a property of the method rather
than a bug.

The rule is one sentence: **never build a floating-point mesh with `arange`.**
`np.linspace(0, t_end, n + 1)` with an integer $n$ lands on $t_{end}$ exactly.

---

# Part 4 — Solving ODEs in Python

## The whole call, with nothing hidden

```python
# /// script
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""Closed A <-> B: the full model, the reduced model, and the conservation check."""
import numpy as np
from scipy.integrate import solve_ivp

kp, km = 0.8, 0.2          # k+ and k- in 1/s
A0, B0 = 3.0, 1.0          # mM
T = A0 + B0

def reversible(t, y, kp, km):
    """Right-hand side of the full model. Time first, even though the model ignores it."""
    a, b = y
    return [-kp * a + km * b,
            kp * a - km * b]

def reduced(t, y, kp, km, T):
    """Equation (2.12): one equation, because b = T - a."""
    a = y[0]
    return [km * (T - a) - kp * a]

tol = dict(rtol=1e-8, atol=1e-10, dense_output=True)
full = solve_ivp(reversible, [0, 20], [A0, B0], args=(kp, km), **tol)
red = solve_ivp(reduced, [0, 20], [A0], args=(kp, km, T), **tol)

t = np.linspace(0, 20, 200)
a_full, b_full = full.sol(t)
a_red = red.sol(t)[0]

print(f"conservation held to {np.max(np.abs(a_full + b_full - T)):.2e} mM")
print(f"full vs reduced agree to {np.max(np.abs(a_full - a_red)):.2e} mM")
print(f"steady state: theory a={km * T / (kp + km):.4f}, numeric a={a_full[-1]:.4f}")
```

Output:

```
conservation held to 8.88e-16 mM
full vs reduced agree to 5.25e-09 mM
steady state: theory a=0.8000, numeric a=0.8000
```

Notice that the two check numbers differ by **seven orders of magnitude**, and that this is not an
accident. The conservation holds to machine precision ($10^{-16}$) because it is structural. The
agreement between two separate integrations is only as good as the tolerance you asked for
($10^{-8}$). An exact structural property stays exact under simulation; a numerical agreement is
only as good as you paid for.

## Four settings worth knowing

**`args`** — pass parameters as arguments, not as globals. A model with global parameters cannot be
reused and cannot be swept.

**`dense_output=True`** — gives you `sol.sol(t)` at any $t$, not only at the points the solver
happened to choose. This decouples "where the solver stepped" from "where I want to plot", which
really are different questions.

**`rtol`, `atol`** — the default is `rtol=1e-3`, and that is loose. Two independent integrations of
the same system can disagree in the fourth decimal place at the defaults. Neither has a bug.
**Set tolerances whenever you intend to compare two results.**

**`method`** — if a simulation is inexplicably slow, or the solver is taking tiny steps, the system
may be **stiff**: very different time constants in one model. Try `method="LSODA"` or
`method="Radau"`. Stiffness is not covered in Ch. 2, but you will hit it next week on the
enzyme-substrate complex. Recognising the name is enough for now.

One note on the signature: `rhs(t, y, *args)` — **time first**, even when the model does not use
time at all. This is the most common source of confusing errors for beginners. And use `solve_ivp`
rather than the older `odeint`; the argument order differs and the interface is worse.

## What a simulation will not give you

Ingalls gives this a full paragraph, and it deserves the same weight in your head. Students who
have just learned to call a solver conclude that simulation supersedes algebra. It does not.

1. **One simulation run is one initial condition.** An analytic formula covers all of them at once.
   Want a different starting point? Run it again.
2. **A formula shows the parameter dependence.** From $a^{ss} = k_0/k_1$ you read straight off that
   doubling $k_0$ doubles the steady state. A simulation fixes the parameters, so exploring them
   means running many simulations and inferring the pattern — and inferring a pattern is not the
   same as knowing it.

Ingalls' next sentence is also true and should also be said: "Nevertheless, in what follows we will
rarely encounter differential equation models for which analytic solutions can be derived." Both
halves hold at once. Simulation does not replace analysis; it is what is left when analysis is
unavailable.
