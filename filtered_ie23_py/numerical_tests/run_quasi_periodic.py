"""Run Filtered-IE23 on van der pol."""

import numpy as np
import matplotlib.pyplot as plt

from filtered_ie23_py import (
    ie_pre_post_3,
    ie_pre_2,
    filtered_ie23,
    quasi_periodic_ode,
    quasi_periodic_ode_sol,
)

t_range = [0, 20.0]
y_init = np.array([2.0, 0.0, -(1 + np.pi**2), 0.0])

dt = 0.1
tol = 0.0075
max_steps = 1000000
num_steps = [200, 400, 800]

for num_step in num_steps:
    x = np.linspace(0.0, 20.0, 1001)
    y = quasi_periodic_ode_sol(x)
    plt.plot(x, y, "b-")
    plt.grid(True)

    t_ie_pre_post_3, y_ie_pre_post_3 = ie_pre_post_3(
        quasi_periodic_ode, t_range, y_init, num_step
    )
    plt.plot(t_ie_pre_post_3, y_ie_pre_post_3[:, 0], "r-", label="constant, 3rd order")
    t_ie_pre_2, y_ie_pre_2 = ie_pre_2(quasi_periodic_ode, t_range, y_init, num_step)
    plt.plot(t_ie_pre_2, y_ie_pre_2[:, 0], "g-", label="constant, 2nd order")
    
    t_filtered_ie23, y_filtered_ie23, e = filtered_ie23(
        quasi_periodic_ode, t_range, y_init, dt, tol, max_steps
    )
    plt.plot(t_filtered_ie23, y_filtered_ie23[:, 0], "b-", label="adaptive")
    plt.legend(mode='expand')
    plt.ylabel("x axis")
    plt.xlabel("t axis")
    plt.legend(loc="lower right")
    plt.savefig(f"quasi_periodic_k_{t_range[1]/num_step}.jpg")
    plt.show()
    plt.close()
