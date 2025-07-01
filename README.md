[![pipeline status](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/badges/main/pipeline.svg)](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/commits/main)

[[_TOC_]]

[How to run]

usage: main.py [-h] [--modest MODEST]
               (--modest-model MODEST_MODEL | --python-model PYTHON_MODEL)
               {explore,check} ...

explore does a random walk, check is the one we are interested in:

usage: main.py check [-h] [--algorithm {vi,pi,ii,svi,smt}]
                     [--json-output]
                     [--max-iterations MAX_ITERATIONS]
                     [--smt-timeout SMT_TIMEOUT]
                     [--precision PRECISION]

options:
  -h, --help            show this help message and exit
  --algorithm {vi,pi,ii,svi,smt}
                        Verification algorithm to use
  --json-output         Output results in JSON format
  --precision PRECISION
                        Numerical convergence threshold

Value Iteration Options:
  --max-iterations MAX_ITERATIONS
                        Maximum number of iterations for
                        value iteration

SMT Options:
  --smt-timeout SMT_TIMEOUT
                        Timeout for SMT solver

example usage:
```
> pip install -r requirements.txt
> python src/model
_checker/main.py --python-model test-files/beb.py check --algorithm pi
Load Modest model
--------------------
--------------------
Check Modest model: pi
LineSeized=0.9166259765625 (time: 0.20s)
GaveUp=0.0833740234375 (time: 0.22s)
--------------------
--------------------
Clean up
--------------------
```

## Latest

![ vi results ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/time_results_vi.png?job=graph_results)

![ pi results ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/time_results_pi.png?job=graph_results)

![ smt results ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/time_results_smt.png?job=graph_results)

![ svi results ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/time_results_svi.png?job=graph_results)

![ ovi results ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/time_results_ovi.png?job=graph_results)

![ ii results ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/time_results_ii.png?job=graph_results)

![ all results ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/time_results_all.png?job=graph_results)

![ all results table ](https://gitlab.utwente.nl/pmc-course/projects-2025/project-4/-/jobs/artifacts/main/raw/results/good_results_table.png?job=graph_results)