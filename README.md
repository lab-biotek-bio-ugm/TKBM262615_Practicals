# TKBM262615_Practicals

Hands-on practicals companion for [TKBM262615](https://github.com/lab-biotek-bio-ugm/TKBM262615) (TBM263214 Komputasi Biologi / Computational Biology).

## Notebooks

Each exercise script in [`scripts/`](scripts/) has a matching Colab-ready notebook in [`notebooks/`](notebooks/), built from the course's lecture notes (Learning Objectives, Key Concepts/Equations, the runnable simulation, Python Exercises, Discussion Questions, and Reading).

| Script | Notebook | Topic | Colab |
|---|---|---|---|
| [`scripts/01_ode_intro.py`](scripts/01_ode_intro.py) | [`notebooks/01_ode_intro.ipynb`](notebooks/01_ode_intro.ipynb) | Introduction to Dynamic Models | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/TKBM262615_Practicals/blob/main/notebooks/01_ode_intro.ipynb) |
| [`scripts/02_mass_action.py`](scripts/02_mass_action.py) | [`notebooks/02_mass_action.ipynb`](notebooks/02_mass_action.ipynb) | Chemical Reaction Networks I | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/TKBM262615_Practicals/blob/main/notebooks/02_mass_action.ipynb) |
| [`scripts/03_enzyme_kinetics_I.py`](scripts/03_enzyme_kinetics_I.py) | [`notebooks/03_enzyme_kinetics_I.ipynb`](notebooks/03_enzyme_kinetics_I.ipynb) | Enzyme Kinetics I | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/TKBM262615_Practicals/blob/main/notebooks/03_enzyme_kinetics_I.ipynb) |
| [`scripts/04_enzyme_kinetics_II.py`](scripts/04_enzyme_kinetics_II.py) | [`notebooks/04_enzyme_kinetics_II.ipynb`](notebooks/04_enzyme_kinetics_II.ipynb) | Enzyme Kinetics II | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/TKBM262615_Practicals/blob/main/notebooks/04_enzyme_kinetics_II.ipynb) |

Click a badge to open that notebook directly in Colab, or run locally with `pip install numpy scipy matplotlib jupyter` and `jupyter notebook notebooks/`.

As more scripts are added to `scripts/` following the course's `NN_topic.py` numbering, add a matching `notebooks/NN_topic.ipynb` using the same cell structure (title + Colab badge → objectives → setup → concepts/equations → simulation → exercises → discussion → reading).

## Instructor materials

[`instructor/`](instructor/) holds the answer key for each notebook's exercises: full derivations, completed code, and teaching notes (expected results, common student mistakes, extension talking points, and a grading rubric). Excluded from the published Quarto site (`_quarto.yml`'s `!instructor/` render rule) so it isn't surfaced next to the student notebooks — don't share these links with students before the exercise deadline.

| Notebook | Instructor solutions |
|---|---|
| [`notebooks/01_ode_intro.ipynb`](notebooks/01_ode_intro.ipynb) | [`instructor/01_ode_intro_solutions.ipynb`](instructor/01_ode_intro_solutions.ipynb) |
| [`notebooks/02_mass_action.ipynb`](notebooks/02_mass_action.ipynb) | [`instructor/02_mass_action_solutions.ipynb`](instructor/02_mass_action_solutions.ipynb) |
| [`notebooks/02_simple_networks.ipynb`](notebooks/02_simple_networks.ipynb) | [`instructor/02_simple_networks_solutions.ipynb`](instructor/02_simple_networks_solutions.ipynb) |
| [`notebooks/03_enzyme_kinetics_I.ipynb`](notebooks/03_enzyme_kinetics_I.ipynb) | [`instructor/03_enzyme_kinetics_I_solutions.ipynb`](instructor/03_enzyme_kinetics_I_solutions.ipynb) |
| [`notebooks/04_enzyme_kinetics_II.ipynb`](notebooks/04_enzyme_kinetics_II.ipynb) | [`instructor/04_enzyme_kinetics_II_solutions.ipynb`](instructor/04_enzyme_kinetics_II_solutions.ipynb) |

When adding solutions for a future topic notebook, follow the same pattern: a matching `instructor/NN_topic_solutions.ipynb`, with the theory/code/checks fully worked plus the reasoning, common mistakes, and a grading rubric — not just the answers.