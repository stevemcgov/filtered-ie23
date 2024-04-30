"""Run Filtered-IE23 on Model ODE."""

from filtered_ie23_py import (
    filtered_ie23,
    ie_pre_post_3,
    test_ode,
    test_ode_sol,
)

t_range = [0.0, 2.0]
y_init = 1.0
num_steps = [200, 400, 2000]
max_steps = 1000000

dts = [0.01, 0.001, 0.005, 0.0005]
tols = [0.001, 0.0001, 0.00025, 0.00025]

for dt, tol in zip(dts, tols):
    t_filtered_ie23, y_filtered_ie23, e = filtered_ie23(
        test_ode, t_range, y_init, dt, tol, max_steps
    )
    print(f"\nNumber of steps taken: {len(t_filtered_ie23) - 1}")
    print(
        "Error at final step:"
        + f"{abs(y_filtered_ie23[-1, :][0] - test_ode_sol(t_range[1])):.5E}"
    )

for num_step in num_steps:
    t_prepost3, y_prepost3 = ie_pre_post_3(test_ode, t_range, y_init, num_step)
    print(f"\nNumber of steps taken: {num_step}")
    print(
        "Error at final step:"
        + f"{abs(y_prepost3[-1, :][0] - test_ode_sol(t_range[1])):.5E}"
    )
