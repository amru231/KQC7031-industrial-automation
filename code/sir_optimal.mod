# ==========================================================

# AMPL Model for SIR Optimal Control with ICU Constraint

# =======================================================

param N; # Time steps

param T; # Total time horizon

param dt := T / N; # Step size

param beta; # Disease transmission rate

param gamma; # Recovery rate

param v_M; # Maximum vaccination rate

param lambda_v; # Cost weight of vaccination

param lambda_i; # Health cost weight of infected population

param i_M; # ICU Bed safety capacity constraint

param s0; # Initial proportion of susceptible individuals

param i0; # Initial proportion of infected individuals

set TIME := 0..N;

set TIME_CONTROL := 0..N-1;

# State variables and control variables

var s {TIME} >= 0, <= 1;

var i {TIME} >= 0, <= 1;

var v {TIME_CONTROL} >= 0, <= v_M;

# Objective function: Minimize total cost (using rectangular integral approximation)

minimize Total_Cost:

sum {t in TIME_CONTROL} (lambda_v * v[t] + lambda_i * i[t]) * dt;

# Dynamic state constraint (discretization of differential equations)

subject to eq_s {t in TIME_CONTROL}:

s[t+1] = s[t] + dt * (-beta * s[t] * i[t] - v[t] * s[t]);

subject to eq_i {t in TIME_CONTROL}:

i[t+1] = i[t] + dt * (beta * s[t] * i[t] - gamma * i[t]);

# Initial conditions
subject to init_s: s[0] = s0;
subject to init_i: i[0] = i0;

# ICU state constraints (dynamically controlled via drop/restore in the running script)
subject to icu_bound {t in TIME}:

i[t] <= i_M;