"""Run Filtered-IE23 on Model ODE Analog."""

import numpy as np
import matplotlib.pyplot as plt

from filtered_ie23_py import (
    filtered_ie23,
    test_ode_analog,
    test_ode_analog_sol,
    set_lambda_test_ode_analog,
)

t_range = [0.0, 10.0]
y_init = 1.0
max_steps = 100000

lams = [1, 3, 5, 5.7, 6]
dts = [0.00001, 0.00001, 0.0001, 0.0001, 0.0001]
tols = [0.000025, 0.000025, 0.00025, 0.00025, 0.0005]

print("\n\nBegin Adaptive Step method...\n\n")

for lam, dt, tol in zip(lams, dts, tols):
    set_lambda_test_ode_analog(lam)
    t_filtered_ie23, y_filtered_ie23, e = filtered_ie23(
        test_ode_analog, t_range, y_init, dt, tol, max_steps
    )
    print(f"\nSettings: lambda = {lam}, dt = {dt}, tol = {tol}")
    print(f"Number of steps taken: {len(t_filtered_ie23) - 1}")
    print(
        "Filtered-IE23 Error at final step: "
        + f"{abs(y_filtered_ie23[-1, :][0] - test_ode_analog_sol(t_range[1])):.5E}"
    )
    x = np.linspace(0.0, 10.0, 1001)
    y = test_ode_analog_sol(x)
    plt.plot(x, y, "r-")
    plt.plot(t_filtered_ie23, y_filtered_ie23, "b-")
    plt.grid(True)
    plt.ylabel("y axis")
    plt.xlabel("t axis")
    plt.savefig(f"plots/filtered_ie23_lambda{lam}_dt{dt}_tol{tol}.jpg")
    plt.close()
