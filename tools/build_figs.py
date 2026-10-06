"""Quarto pre-render: run every lecture-note figure script; images land in course/build/.
A failing script is reported but does not stop the book build (its figure is just missing)."""
import os
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent.parent
env = {**os.environ, "MPLBACKEND": "Agg"}
for script in sorted(root.glob("lecture_notes/*/figs/*.py")):
    r = subprocess.run([sys.executable, str(script)], env=env, capture_output=True, text=True)
    if r.returncode:
        print(f"WARNING: {script.relative_to(root)} failed: {r.stderr.strip().splitlines()[-1]}", file=sys.stderr)
