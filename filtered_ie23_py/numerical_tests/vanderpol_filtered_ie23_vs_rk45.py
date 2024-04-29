"""Filtered-IE23 vs RK45 on van der Pol."""
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp

from filtered_ie23_py import (
    # bdf2,
    filtered_ie23,
    vanderpol_deriv,
    set_mu,
)

t_ranges = [
    [0.0, 50.0],
    [0.0, 50.0],
    [0.0, 100.0],
    [0.0, 200.0],
    [0.0, 500.0],
    [0.0, 1500.0],
]
y_init = np.array([1.0, 0.0])
num_steps = 1000000

dt = 0.001
tol = 0.0075
max_steps = 1000000
mus = [1.0, 2.0, 5.0, 10.0, 100.0, 200.0]
# num_step = 10000

print(
    "Parameter mu & Final t value &"
    + "Final x value IE23 & Final x value RK45  & Method Difference"
)
for mu, t_range in zip(mus, t_ranges):
    set_mu(mu)
    t = np.linspace(t_range[0], t_range[1], 10000)
    sol = solve_ivp(vanderpol_deriv, t_range, y_init, t_eval=t)
    plt.plot(t, sol.y[0], "r-")
    # t_bdf2, y_bdf2 = bdf2(vanderpol_deriv, t_range, y_init, num_step)
    # plt.plot(t_bdf2, y_bdf2[:, 0], "r-")
    t_filtered_ie23, y_filtered_ie23, e = filtered_ie23(
        vanderpol_deriv, t_range, y_init, dt, tol, max_steps
    )
    print(
        "Filtered-IE23 diff from RK45 at final step: "
        + f"{abs(y_filtered_ie23[-1, :][0] - sol.y[0][-1]):.5E}"
    )
    # print(f"Given t range: {t_range[1]}")
    # print(f"Final t value returned from Filtered-IE23: {t_filtered_ie23[-1]}")
    # print(f"Final t value from np.linspace: {t[-1]}")
    print(
        f"{mu} & {t_range[1]} & {y_filtered_ie23[-1, :][0]:.5E} &"
        + f"{sol.y[0][-1]:.5E} & {abs(y_filtered_ie23[-1, :][0] - sol.y[0][-1]):.5E}"
    )
    plt.plot(t_filtered_ie23, y_filtered_ie23[:, 0], "b-", linewidth=1.5)
    plt.grid(True)
    plt.ylabel("x axis")
    plt.xlabel("t axis")
    plt.savefig(f"plots/vanderpol_filtered_ie23_vs_rk45_mu_{mu}.jpg")
    # plt.show()
    plt.close()
