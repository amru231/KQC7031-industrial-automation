import pandas as pd
import matplotlib.pyplot as plt

# Read data exported from AMPL
c1 = pd.read_csv('case1_results.csv')
c2 = pd.read_csv('case2_results.csv')

fig, axes = plt.subplots(3, 2, figsize=(14, 10), sharex=True)

# ----------------- CASE I (Unconstrained) -----------------

# 1. Status
axes[0, 0].plot(c1['time'], c1['s'], label='Susceptible (s)', color='blue')
axes[0, 0].plot(c1['time'], c1['i'], label='Infected (i)', color='red')
axes[0, 0].axhline(y=0.04, color='gray', linestyle='--', label='ICU Threshold (i_M)')
axes[0, 0].set_title('Case I: States (No Constraint)')
axes[0, 0].legend()
axes[0, 0].grid(True)

# 2. Co-states
axes[1, 0].plot(c1['time'], c1['p_s'], label='p_s', color='darkblue')
axes[1, 0].plot(c1['time'], c1['p_i'], label='p_i', color='darkred')
axes[1, 0].set_title('Case I: Co-states')
axes[1, 0].legend()
axes[1, 0].grid(True)

# 3. Switching conditions and control
axes[2, 0].plot(c1['time'], c1['phi'], label='Switching Function ($\phi$)', color='purple')
axes[2, 0].axhline(y=0, color='black', linestyle=':')
ax_v1 = axes[2, 0].twinx()
ax_v1.fill_between(c1['time'], c1['v'], alpha=0.2, color='green', label='Vaccination (v)')
ax_v1.set_ylabel('Control v')
axes[2, 0].set_title('Case I: Switching Condition & Control')
axes[2, 0].set_xlabel('Time')
axes[2, 0].grid(True)

# ------------------ CASE II (with constraints) ------------------
# 1. Status
axes[0, 1].plot(c2['time'], c2['s'], color='blue')
axes[0, 1].plot(c2['time'], c2['i'], color='red')
axes[0, 1].axhline(y=0.04, color='gray', linestyle='--')
axes[0, 1].set_title('Case II: States (With ICU Constraint)')
axes[0, 1].grid(True)

# 2. Collaboration state
axes[1, 1].plot(c2['time'], c2['p_s'], color='darkblue')
axes[1, 1].plot(c2['time'], c2['p_i'], color='darkred')
axes[1, 1].set_title('Case II: Co-states')
axes[1, 1].grid(True)

# 3. Switching conditions and control
axes[2, 1].plot(c2['time'], c2['phi'], color='purple')
axes[2, 1].axhline(y=0, color='black', linestyle=':')
ax_v2 = axes[2, 1].twinx()
ax_v2.fill_between(c2['time'], c2['v'], alpha=0.2, color='green')
ax_v2.set_ylabel('Control v')
axes[2, 1].set_title('Case II: Switching Condition & Control')
axes[2, 1].set_xlabel('Time')
axes[2, 1].grid(True)

plt.tight_layout()
plt.savefig('optimal_control_comparison.png', dpi=300)
plt.show()