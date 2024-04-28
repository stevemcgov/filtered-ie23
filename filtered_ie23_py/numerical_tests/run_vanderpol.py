import numpy as np
import matplotlib.pyplot as plt
# from scipy.integrate import solve_ivp

from filtered_ie23_py import (
    filtered_ie23,
    vanderpol_deriv,
    set_mu,
)

t_ranges = [[0.0, 50.0], [0.0, 50.0], [0.0, 100.0], [0.0, 200.0], [0.0, 500.0]]
y_init = np.array([1.0, 0.0])
# num_steps = 10000

dt = 0.001
tol = 0.0075
max_steps = 1000000
mus = [1.0, 2.0, 5.0, 10.0, 100.0]


for mu, t_range in zip(mus, t_ranges):
    set_mu(mu)
    # t = np.linspace(t_range[0], t_range[1], 10000)
    # sol = solve_ivp(vanderpol_deriv, t_range, y_init, t_eval=t)
    # plt.plot(t, sol.y[0], "b-")
    t_filtered_ie23, y_filtered_ie23, e = filtered_ie23(
        vanderpol_deriv, t_range, y_init, dt, tol, max_steps
    )
    plt.plot(t_filtered_ie23, y_filtered_ie23[:, 0], "r-", linewidth=1.5)
    plt.grid(True)
    plt.title("y = vanderpol_sol Filtered-IE23")
    plt.savefig(f"plots/vanderpol_filtered_ie23_mu_{mu}.jpg")
    plt.show()
    plt.close()
