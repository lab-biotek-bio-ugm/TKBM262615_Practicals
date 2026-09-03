# TKBM262615 Practicals — Computational Biology Hands-On Notebooks

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lab-biotek-bio-ugm/TKBM262615_Practicals/blob/main/notebooks/02_simple_networks.ipynb)
[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://lab-biotek-bio-ugm.github.io/TKBM262615_Practicals/)
[![Use this template](https://img.shields.io/badge/use%20this-template-2ea44f)](https://github.com/lab-biotek-bio-ugm/TKBM262615_Practicals/generate)

## About

Companion hands-on notebook repository for **TBM263214 Komputasi Biologi** (Computational Biology), Biomedical Engineering, Universitas Gadjah Mada — instructor Matin Nuhamunada. It pairs with the course's lecture-notes/slides repo, [`lab-biotek-bio-ugm/TKBM262615`](https://github.com/lab-biotek-bio-ugm/TKBM262615).

Notebooks are Jupyter `.ipynb` files that run directly in Google Colab, and can optionally be published as a static site via [Quarto](https://quarto.org/) → GitHub Pages.

## Contents

| Notebook | Topic |
|---|---|
| [`notebooks/02_simple_networks.ipynb`](notebooks/02_simple_networks.ipynb) | MMSB §2.1.3 "Simple Networks" — decay, production and decay, irreversible conversion, reversible conversion |

## Run it

**Google Colab (no setup required):** click the "Open in Colab" badge above, then *Runtime → Run all*.

**Local, pip:**
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

**Local, conda:**
```bash
conda env create -f environment.yml
conda activate tkbm262615-practicals
jupyter lab
```

## Publish/preview with Quarto

```bash
quarto preview   # live local preview
quarto render    # build the static site into _site/
```

A GitHub Actions workflow (`.github/workflows/publish.yml`) renders the site with Quarto and deploys it to GitHub Pages on every push to `main`.

## Notebook hygiene: outputs are always stripped before commit

This repo uses a shared git hook (`.githooks/pre-commit`) that clears cell outputs and
execution counts from any staged `.ipynb` file — via `jupyter nbconvert --clear-output`
— before every commit, so diffs stay readable and committed notebooks never carry stale
run state. It needs no extra dependency (`jupyter` is already in `requirements.txt` /
`environment.yml`).

**One-time setup per clone** (git hooks aren't copied automatically):
```bash
git config core.hooksPath .githooks
```

## Instructor materials

[`instructor/02_simple_networks_solutions.ipynb`](instructor/02_simple_networks_solutions.ipynb)
is the answer key for the exercises in `notebooks/02_simple_networks.ipynb`: full
derivations, completed code, and grading notes (expected results, common student
mistakes, and extension talking points) for each exercise. It's committed to the repo
like any other file, but excluded from the published Quarto site (`_quarto.yml`'s
`project.render` list) so it isn't surfaced next to the student notebook — don't share
its link with students before the exercise deadline.

When adding solutions for a future topic notebook, follow the same pattern: a matching
file under `instructor/`, with the theory/code/checks fully worked plus the reasoning
and pitfalls, not just the answers.

## Using this as a template

This repo is set up as a GitHub **template repository**: use the "Use this template" button (or badge above) to create a fresh copy — with no shared git history — as a starting point for a new chapter or topic notebook. The pattern to follow when extending it:

1. Add a new notebook under `notebooks/` (e.g. `03_enzyme_kinetics.ipynb`), following the same structure: a Colab badge, a short theory markdown cell per example, a code cell with an editable parameters block, and a printed sanity check (analytical-vs-numeric or a conservation/steady-state check).
2. Add an entry for it to the `navbar` in `_quarto.yml`.

## Source material / citation

The textbook excerpt is **not** redistributed in this repository. Read/download the official PDF (with solutions) directly from the author:

> Ingalls, B. P. (2013). *Mathematical Modeling in Systems Biology: An Introduction*. MIT Press.
> <https://www.math.uwaterloo.ca/~bingalls/MMSB/MMSB_w_solutions.pdf>

## License

MIT — see [LICENSE](LICENSE).
