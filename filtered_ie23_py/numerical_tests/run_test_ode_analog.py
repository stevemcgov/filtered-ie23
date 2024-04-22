import numpy as np
import matplotlib.pyplot as plt

from filtered_ie23_py import (
    filtered_ie23,
    ie_pre_post_3,
    bdf2,
    test_ode_analog,
    test_ode_analog_sol,
)

t_range = [0.0, 20.0]
y_init = 1.0
num_steps = [200, 400, 2000]
max_steps = 100000000

# dts = [0.01, 0.001, 0.005, 0.0005]
# tols = [0.001, 0.0001, 0.00025, 0.00025]
dts = [0.001,  0.0001, 0.00005]  # good for lambda = 5
tols = [0.001, 0.0001, 0.000005] # good for lambda = 5
dts = [0.0001,  0.00001, 0.000005]  # good for lambda = 5
tols = [0.0001, 0.000001, 0.0000005] # good for lambda = 5

print("\n\nBegin Adaptive Step method...\n\n")
for dt, tol in zip(dts, tols):
    t_filtered_ie23, y_filtered_ie23, e = filtered_ie23(
        test_ode_analog, t_range, y_init, dt, tol, max_steps
    )
    print(f"\nNumber of steps taken: {len(t_filtered_ie23) - 1}")
    print(
        f"Error at final step:{abs( y_filtered_ie23[-1,:][0] - test_ode_analog_sol(t_range[1] ) ):.5E}"
    )
    plt.plot(t_filtered_ie23, y_filtered_ie23, "b-")
    plt.grid(True)
    plt.ylabel("y axis")
    plt.xlabel("t axis")
    plt.show()
    plt.close()

# print("\n\nBegin Constant Step method...\n\n")
# for num_step in num_steps:
#     t_prepost3, y_prepost3 = ie_pre_post_3(test_ode_analog, t_range, y_init, num_step)
#     print(f"\nNumber of steps taken: {num_step}")
#     print(
#         f"Error at final step:{abs( y_prepost3[-1,:][0] - test_ode_analog_sol(t_range[1] ) ):.5E}"
#     )
#     plt.plot(t_prepost3, y_prepost3, "b-")
#     plt.grid(True)
#     plt.ylabel("y axis")
#     plt.xlabel("t axis")
#     plt.show()
#     plt.close()

# for num_step in num_steps:
#     t_bdf2, y_bdf2 = bdf2(test_ode_analog, t_range, y_init, num_step)
#     print(f"\nNumber of steps taken: {num_step}")
#     print(
#         f"Error at final step:{abs( y_bdf2[-1,:][0] - test_ode_analog_sol(t_range[1] ) ):.5E}"
#     )
#     plt.plot(t_bdf2, y_bdf2, "b-")
#     plt.grid(True)
#     plt.ylabel("y axis")
#     plt.xlabel("t axis")
#     plt.show()
#     plt.close()
