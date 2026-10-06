# L07 — Constraint-Based Analysis: the S matrix and flux balance

**Practicals** (repo [`lab-biotek-bio-ugm/cell-factory-design-course`](https://github.com/lab-biotek-bio-ugm/cell-factory-design-course)):
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/01-Getting-started.ipynb) `01-Getting-started` ·
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/02-Genome-scale-metabolic-models.ipynb) `02-Genome-scale-metabolic-models` ·
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/03-Pathway-visualization.ipynb) `03-Pathway-visualization`

*Practical content:* the three notebooks load a genome-scale model of *E. coli*, run flux balance analysis, take the model apart (metabolites, reactions, genes, the $S$ matrix) and draw the fluxes on pathway maps. The toy network and the linear program below are in these notes only.

*Source: Ingalls §5.4, especially §5.4.2 (a starred section); notebooks 01–03 of the cell-factory course. Ingalls writes the stoichiometry matrix as $N$; constraint-based modelling, and cobrapy, call it $S$. It is the same matrix you built in L04.*

By the end of this lecture you should be able to:

1. Build the stoichiometry matrix $S$ from a list of reactions: rows are metabolites, columns are reactions, substrates are negative, products positive, and exchange reactions have one end outside the model.
2. Derive $S\mathbf{v} = 0$ from $\frac{d\mathbf{x}}{dt} = S\mathbf{v}$, and say what the steady-state assumption keeps and what it throws away.
3. Say why a genome-scale network has many more steady-state flux patterns than one, name the space that holds them (the right null space), and say how bounds and an objective pick one.
4. Run flux balance analysis (FBA) in cobrapy, read the growth rate, the fluxes and the solver status, and state four things the answer does not tell you.

## Retrieval: what L06 left you holding

From memory, no notes:

1. A competitive inhibitor is added. What happens to $V_{max}$ and to $K_M$, and why does adding more substrate undo it?
2. A Hill function has $n = 4$. What is its kinetic order at $x = K$, and how much must the input change to go from 10% to 90% of the response?
3. Why is a Hill-type switch *soft*, and what would it need to behave like a memory?

<details>
<summary>Answers</summary>

1. $V_{max}$ is unchanged; $K_M$ is multiplied by $(1 + i/K_i)$. The inhibitor and the substrate compete for the same site, so enough substrate wins the site back and the enzyme still reaches $V_{max}$.
2. Kinetic order $n(1-Y) = 4 \times \frac{1}{2} = 2$ at $x = K$. The 10%–90% span is $81^{1/n} = 3$-fold.
3. It is a smooth function of the *present* input, so it has no memory: remove the input and the output returns. Memory needs feedback.

</details>

Today leans on a lecture before L06: the stoichiometry matrix $N$ and the left null space of L04.

## The hook: a model with no constants

Every model since L03 needed numbers you had to measure: $k_1$, $k_{-1}$, $k_2$, $K_i$, $n$. Ingalls' enzyme constants came from decades of bench work on one enzyme.

Now take *E. coli*. The model in notebook 01, *i*JO1366, has 1805 metabolites and 2583 reactions (notebook 02 counts them). For most of those reactions nobody has measured a rate constant inside a living cell. Yet one line of Python, `model.optimize()`, returns a growth rate of 0.98 h⁻¹ — a doubling time of about 42 minutes, close to what the bacterium does in glucose minimal medium.

How can a model with no rate constants predict anything? It pays a price, and today is about what the price is. **Give up time. Keep structure.** The network of arrows, with the number of molecules each arrow moves, is known for the whole genome. The rates are not. So ask a different question: not *what does this cell do from this starting point*, but *what could this network possibly do at steady state, and which of those things is best?*

---

# Part 1 — The stoichiometry matrix $S$

## From arrows to numbers

In L03 you turned arrows into equations. In L04 you collected the coefficients in a matrix:

$$\frac{d\mathbf{x}}{dt} = S\,\mathbf{v}$$

$\mathbf{x}$ holds one concentration per metabolite and $\mathbf{v}$ one rate per reaction. In constraint-based modelling $\mathbf{v}$ is called the **flux vector**, with units mmol per gram dry weight per hour (mmol gDW⁻¹ h⁻¹). The matrix $S$ has

- **one row per metabolite** and **one column per reaction**,
- a **negative** entry where the reaction consumes the metabolite and a **positive** one where it produces it, the entry's size being the stoichiometric coefficient,
- zero everywhere else.

Read a column and you learn what one reaction does. Read a row and you learn everything that touches one metabolite.

## A toy cell

Four metabolites ($A$, $B$, $C$, $E$, a stand-in for ATP) and seven reactions:

| Reaction | Arrow | Role |
|---|---|---|
| R1 | $\to A$ | **uptake**: $A$ enters from outside |
| R2 | $A \to B + E$ | makes a building block and energy |
| R3a | $A \to C$ | makes the second building block |
| R3b | $A \to C$ | a second route to $C$ (an isozyme, say) |
| R4 | $B + C \to$ biomass | **growth**: drains $B$ and $C$ in a fixed 1:1 ratio |
| R5 | $B \to$ | **by-product** leaves the cell |
| R6 | $E \to$ | **maintenance**: energy is burnt just to stay alive |

R1, R5 and R6 are **exchange** reactions. Each has one end outside the model, so its column has only one non-zero entry. R4, the biomass reaction, is a drain too: it removes building blocks in the proportions a new cell needs. Written as a matrix:

$$S = \begin{pmatrix}
 1 & -1 & -1 & -1 &  0 &  0 &  0 \\
 0 &  1 &  0 &  0 & -1 & -1 &  0 \\
 0 &  0 &  1 &  1 & -1 &  0 &  0 \\
 0 &  1 &  0 &  0 &  0 &  0 & -1
\end{pmatrix}
\qquad
\begin{matrix} A \\ B \\ C \\ E \end{matrix}$$

The rows are $A, B, C, E$ from top to bottom and the columns are R1, R2, R3a, R3b, R4, R5, R6 from left to right. Check one column: R2 consumes $A$ ($-1$) and produces $B$ and $E$ ($+1$ each), which is its column.

## What $S$ contains, and what it does not

$S$ contains only **which arrows exist and how many molecules each moves**. It has no rate constants, no concentrations and no rate laws. That is why it can be written down for a whole genome: it comes from the genome annotation and the biochemical literature, not from kinetics experiments.

Real models are the same object, bigger. Notebook 02 builds it with `create_stoichiometric_matrix(model)` and plots its non-zero entries with `plt.spy`:

- *i*JO1366 has 1805 metabolites and 2583 reactions, so $S$ is 1805 × 2583. The smaller `e_coli_core` model, used in the exercises, has 72 metabolites and 95 reactions.
- It is **sparse**: a typical reaction touches a handful of metabolites. The dense horizontal lines in the plot are the metabolites that nearly everything touches, such as H⁺, H₂O, ATP and NAD(H).
- A chemical in two compartments is two rows (`glc__D_c` and `glc__D_p`), joined by a transport reaction.

---

# Part 2 — The steady-state assumption

## From $\frac{d\mathbf{x}}{dt} = S\mathbf{v}$ to $S\mathbf{v} = 0$

Suppose the internal metabolites do not accumulate or deplete: $\frac{d\mathbf{x}}{dt} = 0$. Then

$$S\,\mathbf{v} = 0$$

Row by row for the toy cell:

$$\begin{aligned}
A:&\quad v_1 - v_2 - v_{3a} - v_{3b} = 0\\
B:&\quad v_2 - v_4 - v_5 = 0\\
C:&\quad v_{3a} + v_{3b} - v_4 = 0\\
E:&\quad v_2 - v_6 = 0
\end{aligned}$$

Each row says: **production equals consumption**. Nothing is left over to pile up. Ingalls arrives at the same equation as the balance condition $0 = N\mathbf{v}$ in §5.4.2.

## What it assumes

Metabolism is fast. Over the minutes a cell takes to grow and divide, metabolite pools settle to whatever level makes production match consumption. This is the idea of L05 (the quasi-steady-state assumption) applied to **every** metabolite at once instead of one complex. Like the QSSA, it is an approximation that holds when the time-scales separate.

## What it throws away

Look at what is *not* in $S\mathbf{v} = 0$:

- **time**: there is no $t$ and no $[A](t)$;
- **concentrations**: the equation never mentions $[A]$, so saturation, inhibition and cooperativity (L05, L06) have nowhere to appear;
- **rate laws**: a flux is just a number that must balance.

This is the trade from the hook. A kinetic model has a rate law $v_i(\mathbf{x}, \mathbf{p})$ for every reaction; here each $v_i$ is a free variable. Ingalls makes the correspondence explicit: the **upper bounds** that FBA needs "correspond to $V_{max}$ values in a kinetic model".

---

# Part 3 — Two null spaces

$S$ is a matrix, so it has two null spaces. You have already met one.

| | **Left null space** | **Right null space** |
|---|---|---|
| Vectors | $\mathbf{w}$ with $\mathbf{w}^TS = 0$ | $\mathbf{v}$ with $S\mathbf{v} = 0$ |
| Indexed by | metabolites | reactions |
| Meaning | a **conservation**: $\mathbf{w}\cdot\mathbf{x}$ never changes (L04) | a **steady-state flux pattern** |
| Question it answers | what is conserved? | what could the network do at steady state? |
| Depends on rate constants? | no | no |

## The left null space of the toy cell is empty

The code in Part 4 computes it: dimension **0**. There is no conservation, because R1, R5 and R6 let material in and out. L03 said that open networks generally have none; here it is as a number.

## The right null space is where the possibilities live

For the toy cell it has dimension **3**. Rank-nullity explains why: seven unknown fluxes ($S$ has seven columns) but only four independent equations (rank 4), leaving $7 - 4 = 3$ fluxes free. Choose $v_{3a}$, $v_{3b}$ and $v_5$ and the other four are determined:

$$v_4 = v_{3a} + v_{3b}, \qquad v_2 = v_4 + v_5, \qquad v_6 = v_2, \qquad v_1 = v_2 + v_{3a} + v_{3b}.$$

Now scale up. A metabolic network almost always has **more reactions than metabolites**, so $S$ is wide. The number of free fluxes is at least the number of columns minus the number of rows. For *i*JO1366 that is at least $2583 - 1805 = 778$; the matrix has rank 1766, so the exact number is $2583 - 1766 = 817$ (`np.linalg.matrix_rank(S)`). Ingalls calls this case **under-determined** (§5.4.2, Case III): the steady-state condition alone can never give one answer. In Ingalls' words, a unique prediction "can only be reached by imposing additional constraints".

---

# Part 4 — Bounds, an objective, and a linear program

Two kinds of extra constraint select one flux vector from the space.

**Bounds.** Each flux gets limits, $l_i \le v_i \le u_i$. An irreversible reaction has $l_i = 0$. Uptake is capped: *i*JO1366's glucose uptake is capped at 10 mmol gDW⁻¹ h⁻¹. Maintenance gets a floor: notebook 02 shows that the reaction `ATPM` has a lower bound, so every solution must burn at least that much ATP. A negative flux means the reaction runs against the direction it is written; an uptake appears as a negative flux through a BiGG exchange reaction, which is written as metabolite → outside.

**An objective.** Pick a combination of fluxes to maximise, $\mathbf{c}\cdot\mathbf{v}$. For growth, $\mathbf{c}$ selects the biomass reaction: the cell is assumed to be shaped by selection to make more cells. Ingalls: FBA "typically presumes that the 'goal' of a cell is to produce more cells". Together:

$$\max_{\mathbf{v}}\; \mathbf{c}\cdot\mathbf{v} \quad\text{subject to}\quad S\mathbf{v} = 0,\;\; \mathbf{l} \le \mathbf{v} \le \mathbf{u}$$

This is **flux balance analysis**. Everything is linear, so it is a **linear program**. In a linear program every local optimum is the global one, and solvers handle thousands of variables in seconds. That is what makes the genome-scale version practical. cobrapy builds exactly this problem when you call `model.optimize()`; notebook 02 prints its first lines.

Without an upper bound on uptake the optimum would be unbounded (Ingalls makes the same point). Notebook 02's "the math (scary!)" cell shows the problem as the solver sees it.

## The toy cell as a linear program

Uptake ≤ 10, maintenance ≥ 1, maximise growth ($v_4$). The code below needs only numpy and scipy:

```python
# /// script
# dependencies = ["numpy", "scipy"]
# ///
"""A toy cell: write down S, find its two null spaces, then run FBA as a linear program."""
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import linprog

# Columns: R1 uptake -> A | R2 A -> B + E | R3a A -> C | R3b A -> C (second route)
#          R4 B + C -> biomass | R5 B -> by-product (leaves) | R6 E -> drain (maintenance)
#                R1    R2    R3a   R3b   R4    R5    R6
S = np.array([[ 1., -1., -1., -1.,  0.,  0.,  0.],    # A
              [ 0.,  1.,  0.,  0., -1., -1.,  0.],    # B
              [ 0.,  0.,  1.,  1., -1.,  0.,  0.],    # C
              [ 0.,  1.,  0.,  0.,  0.,  0., -1.]])   # E

print("S is", S.shape[0], "metabolites x", S.shape[1], "reactions; rank", np.linalg.matrix_rank(S))
print("left null space dimension: ", null_space(S.T).shape[1], "(conservations)")
print("right null space dimension:", null_space(S).shape[1], "(free steady-state fluxes)")

def fba(uptake_max=10.0, maintenance_min=1.0):
    bounds = [(0, uptake_max), (0, None), (0, None), (0, None), (0, None), (0, None),
              (maintenance_min, None)]            # irreversible; R1 capped; R6 has a floor
    c = np.zeros(7)
    c[4] = -1.0                                   # linprog minimises, so maximise v4 as -v4
    return linprog(c, A_eq=S, b_eq=np.zeros(4), bounds=bounds, method="highs")

res = fba()
v = res.x
assert np.allclose(S @ v, 0)                      # the steady-state constraint holds
print("v =", v.round(3), " growth =", -res.fun)

for u in (5, 10, 20):
    print(f"uptake bound {u:2d}  ->  growth {-fba(uptake_max=u).fun:g}")
print("maintenance floor 20 -> status", fba(maintenance_min=20.0).status, "(2 = infeasible)")

# Alternative optima: fix growth at its optimum, then ask how far R3a can move.
A_eq = np.vstack([S, [0, 0, 0, 0, 1, 0, 0]])
b_eq = np.r_[np.zeros(4), -res.fun]
lo, hi = (linprog(s * np.eye(7)[2], A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, 10), (0, None), (0, None), (0, None), (0, None), (0, None), (1, None)],
                  method="highs").x[2] for s in (1, -1))
print(f"at the same optimal growth, R3a can be anywhere from {lo:g} to {hi:g}")
```

Output:

```text
S is 4 metabolites x 7 reactions; rank 4
left null space dimension:  0 (conservations)
right null space dimension: 3 (free steady-state fluxes)
v = [10.  5.  5.  0.  5.  0.  5.]  growth = 5.0
uptake bound  5  ->  growth 2.5
uptake bound 10  ->  growth 5
uptake bound 20  ->  growth 10
maintenance floor 20 -> status 2 (2 = infeasible)
at the same optimal growth, R3a can be anywhere from 0 to 5
```

Read it:

- **The optimum is a vertex.** All 10 units of uptake go to growth, which consumes $B$ and $C$ one for one: $v_4 = 5$, and $v_5 = 0$ because making by-product wastes carbon. The check `S @ v ≈ 0` is in the code: never trust a solver's answer you have not checked against the constraints.
- **The bound sets the answer.** Halve the uptake and growth halves. The "growth rate" is a consequence of the bound, not a property of the network alone.
- **Infeasibility is an answer too.** Demanding 20 units of maintenance energy cannot be met from 10 units of uptake. The solver reports status 2, and any numbers it returns then are meaningless. Check `solution.status` first.
- **The optimum need not be unique.** At the same growth, R3a can carry anything from 0 to 5, because R3b can make up the difference. The solver returned one of them ($v_{3a} = 5$, $v_{3b} = 0$), and another solver might return another.

---

# Part 5 — What FBA cannot tell you

A growth rate of 0.98 h⁻¹ looks like a measurement. It is a prediction under four assumptions. Hold on to all four.

1. **Fluxes, not concentrations or dynamics.** There is no $[A](t)$, no lag phase, no saturation. L04–L06 are the lectures to reach for when the question is *how fast* or *when*.
2. **The objective is an assumption.** "Maximise growth" is a modelling choice, the same kind of choice as "state variable or parameter" in L02. For a metabolic engineer it may be wrong: Ingalls notes that maximising a target product "is unlikely to ever be realized in the cell, but it provides an upper bound on achievable production rates".
3. **No regulation, and many optima.** FBA has no gene regulation and no allosteric control. Where the optimum is not unique it returns one point. Notebook 04 of the same course, which we do not cover, asks for the whole range at the optimum.
4. **The answer depends on the bounds.** The 0.98 h⁻¹ is conditional on 10 mmol gDW⁻¹ h⁻¹ of glucose. The smaller `e_coli_core` model gives about 0.87 h⁻¹ on the same bound, because its biomass reaction and maintenance requirement differ (the core model's `ATPM` lower bound is 8.39, *i*JO1366's is 3.15). Two models, two answers, and neither is "the" growth rate of *E. coli*.

## Hinge question

> Notebook 01 reports growth of 0.98 h⁻¹ for *i*JO1366. You halve the glucose uptake bound, and
> predicted growth falls to 0.48 h⁻¹, almost exactly half. What does that tell you?
>
> **A.** The cell's kinetics are linear in glucose.
> **B.** Nothing about kinetics: FBA has no kinetics. The linear response comes from the bound and
> the constraints, as in the toy cell.
> **C.** The model has been mis-built, because real growth saturates with substrate.
> **D.** The solver is not converging.

<details>
<summary>Answer</summary>

**B.** FBA contains no rate law, so it cannot say anything about saturation. Growth follows the uptake bound while uptake is the limiting constraint, exactly as growth doubled when the toy cell's uptake bound doubled. (It is not exactly proportional in a real model, 0.48 rather than 0.49, because maintenance is a fixed cost.) A is the tempting error, since it reads a modelling consequence as a biological fact. C blames the model for something it never claimed. D has no basis if `solution.status` is `optimal`.

</details>

---

# Part 6 — The practical: three notebooks

The practical is hosted in another repository, [`cell-factory-design-course`](https://github.com/lab-biotek-bio-ugm/cell-factory-design-course), which was written for genome-scale models and strain design. Use the **student** versions (exercise solutions are replaced by empty cells). On Colab, run the first (setup) cell: it clones the repository and installs the dependencies, which takes about 1–2 minutes. Save a copy to your Drive to keep your work.

| # | Notebook | Time | In one line |
|---|---|---|---|
| 01 | `01-Getting-started` | 30 min | Load *i*JO1366, run FBA, read growth and fluxes. |
| 02 | `02-Genome-scale-metabolic-models` | 45 min | Metabolites, reactions, genes, GPR rules, the $S$ matrix, an infeasible model. |
| 03 | `03-Pathway-visualization` | 30 min | Draw FBA fluxes on Escher maps (needs internet). |

Do them in order. Each has an *Overview* with its learning objectives. Then answer these before you leave:

**Notebook 01**
- What is the default objective, and what are the units and meaning of the number `model.optimize()` returns? How do you turn it into a doubling time?
- Count how many reactions carry non-zero flux in the optimum. What does a zero flux mean here?
- What is the *reduced cost* of a reaction, and why is it zero for the reactions in use?
- For the exercise model (`e_coli_core` or another from BiGG): what is the objective value, and why does it differ from *i*JO1366's?

**Notebook 02**
- How many metabolites and reactions does *i*JO1366 have? What is the *smallest* dimension its right null space can have?
- In the `plt.spy` plot of $S$, what are the horizontal lines?
- Find `ATPM`. What is its lower bound, and which reaction in the toy cell played the same role?
- Reproduce the infeasible model. What does `status` say, and why must you check it before using `fluxes`?
- Read the GPR rules of `PFK` and `ATPS4rpp`. What does `or` mean, what does `and` mean?

**Notebook 03**
- What decides the direction of an arrow on a map, and what does a negative flux look like?
- You run the core-model fluxes on the *i*JO1366 map. Why are most of its arrows grey?

<details>
<summary>Answers (checked by running the instructor notebooks in cobrapy 0.32)</summary>

**01.** The default objective is the biomass reaction, in h⁻¹; the doubling time is $\ln 2/\mu$, here about 42 min. About 440 of the 2583 reactions carry non-zero flux (438 in the run checked); a zero flux means the reaction is not needed for optimal growth on glucose. The reduced cost says how much the objective would change per unit of flux forced through a reaction; it is zero for reactions already in use. `e_coli_core` gives 0.87 h⁻¹ because its biomass reaction and maintenance requirement differ.

**02.** 1805 metabolites and 2583 reactions, so the right null space has at least 778 dimensions (817 exactly). The horizontal lines are the metabolites nearly everything touches: H⁺, H₂O, ATP, NAD(H). `ATPM` has a lower bound of 3.15, the counterpart of the toy cell's R6. The infeasible model has `status == 'infeasible'`, and the numbers it returns mean nothing. `or` means isozymes, either gene is enough (`PFK`); `and` means subunits of one complex, all are needed (`ATPS4rpp`).

**03.** Arrowheads follow the sign of the flux, so a negative flux points against the direction the reaction is written. The core model has no flux for reactions that exist only in *i*JO1366, so those arrows stay grey.

</details>

For more practice on the paper-and-pencil side, do Ingalls' Exercise 5.4.11 (maximal fluxes under uptake bounds, then with a knock-out) on the network of Figure 5.18.

## Where the course goes next

The same repository continues past these three notebooks: flux variability analysis (04), changing the medium and adding pathways (05), gene knock-outs (06), yields (07), pathway prediction and strain-design algorithms (08–10), dynamic FBA that brings time back (11), and an enzyme-constrained model with proteomics (12). They are not part of this lecture.

---

# Part 7 — Two ways to model one cell

| | Kinetic models (L03–L06) | Constraint-based (L07) |
|---|---|---|
| Input | rate laws and constants | $S$, bounds, an objective |
| Constants needed | $k$, $K_M$, $K_i$, $n$ for every reaction | none; bounds play the role of $V_{max}$ |
| Equation | $\frac{d\mathbf{x}}{dt} = S\mathbf{v}(\mathbf{x})$ | $S\mathbf{v} = 0$ |
| Answer | concentrations over time | one steady-state flux vector |
| Typical size | a pathway: a handful of reactions | a genome: thousands of reactions |
| Cost | needs data you rarely have | no dynamics, no regulation |

It is the same matrix $S$ in both columns. The first lets $\mathbf{v}$ be a function of $\mathbf{x}$ and follows $\mathbf{x}$ through time. The second sets $\frac{d\mathbf{x}}{dt} = 0$ and asks what $\mathbf{v}$ can be.
