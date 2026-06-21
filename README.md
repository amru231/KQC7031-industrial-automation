# Optimal Control of an SIR Epidemic with an ICU Capacity Constraint

Supplementary code and results for the **KQC7031 Industrial Automation and
Robotics** assignment — *Session 2025/2026, Semester 2*.

This repository accompanies the submitted report. The report PDF is the primary
deliverable; the material here provides the full source code, raw numerical
results, and reproduction steps that do not fit inside a single PDF.

> Department of Electrical Engineering, Universiti Malaya 

## Group members

| Name | Matric No. |
|------|------------|
| Muhammad Amru bin Mohamad Sharis | S2116804 |
| Avienash A/L Shankar | U2103136/2 |
| Chuah Wei Yang | 25066431 |
| Guo Xuanzhuo | 24215841 |
| Lau Sim Yee | 24220152 |

Further details (methodology, derivations, discussion) are in the report:
[`report/KQC7031_Assignment_Report.pdf`](report/KQC7031_Assignment_Report.pdf).

---

## Problem summary

We minimise the combined vaccination and health cost of an epidemic modelled by
a normalised SIR system, choosing the time-varying vaccination rate `v(t)` as the
control variable.

**Objective**

```
minimise  J = ∫₀ᵀ ( λ_v · v(t) + λ_i · i(t) ) dt
```

**State dynamics** (susceptible `s`, infected `i`)

```
ṡ = −β·s·i − v·s
i̇ =  β·s·i − γ·i
```

**Two scenarios are compared:**

| Case | Description |
|------|-------------|
| **Case I**  | Unconstrained — no limit on the infected fraction |
| **Case II** | ICU constraint `i(t) ≤ i_M` enforced (hospital bed safety capacity) |

The optimisation is discretised on a uniform time grid and solved as a nonlinear
program. Co-states (`p_s`, `p_i`) and the switching function `φ` are recovered
from the constraint duals to verify the Pontryagin optimality conditions.

## Parameters (`code/sir_optimal.dat`)

| Symbol | Value | Meaning |
|--------|-------|---------|
| `N`        | 500  | time steps |
| `T`        | 50   | time horizon |
| `β`        | 0.30 | transmission rate |
| `γ`        | 0.10 | recovery rate |
| `v_M`      | 0.05 | max vaccination rate |
| `λ_v`      | 2.0  | vaccination cost weight |
| `λ_i`      | 15.0 | infection (health) cost weight |
| `i_M`      | 0.04 | ICU capacity bound (Case II) |
| `s0`, `i0` | 0.95, 0.01 | initial susceptible / infected |

## Repository layout

```
.
├── code/
│   ├── sir_optimal.mod   # AMPL model: states, control, objective, constraints
│   ├── sir_optimal.dat   # parameter values
│   ├── sir_optimal.run   # solves Case I then Case II, exports CSV
│   ├── plot_results.py   # builds the 3×2 comparison figure
│   ├── case1_results.csv # exported solution — Case I (unconstrained)
│   ├── case2_results.csv # exported solution — Case II (ICU constraint)
│   └── optimal_control_comparison.png
└── report/
    ├── KQC7031_Assignment_Report.pdf   # full report (submitted version)
    └── Case1&Case2_Derivation.pdf      # analytical derivation, Case I & II
```

## How to reproduce

**Requirements:** [AMPL](https://ampl.com/) with the **IPOPT** solver, and Python 3
with `pandas` + `matplotlib`.

```bash
cd code

# 1. Solve both cases and export case1_results.csv / case2_results.csv
ampl sir_optimal.run

# 2. Regenerate the comparison figure
pip install pandas matplotlib
python plot_results.py
```

`sir_optimal.run` solves Case I (drops the ICU constraint), then Case II
(restores it), printing the optimal cost `J` for each and writing the CSVs.

## Output columns

Each results CSV contains: `time, s, i, v, p_s, p_i, phi`
(time, susceptible, infected, vaccination control, two co-states, switching function).

## Figure

`code/optimal_control_comparison.png` — 3×2 panel comparing the two cases:
states, co-states, and switching function / control, side by side.
