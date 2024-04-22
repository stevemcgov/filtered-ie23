import numpy as np
import matplotlib.pyplot as plt

from filtered_ie23_py import (
    test_ode_analog_sol,
    test_ode_sol,
    sharp_transition_ode1_sol,
    set_lambda_sharp_transition_ode1
)


def _plot_sol(ranges, ode_sol, names):
    for r, sol, name in zip(ranges, ode_sol, names):
        t = np.linspace(r[0], r[1], 1001)
        y = sol(t)
        plt.plot(t, y, "b-")
        plt.grid(True)
        plt.ylabel('y axis')
        plt.xlabel('t axis')
        plt.title(f"y = {name}")
        plt.savefig(f"{name}.jpg")
        plt.show()
        plt.close()


if __name__ == "__main__":
    ranges = [[0.0, 20.0], [0.0, 2.0], [0.0, 1.0]]
    set_lambda_sharp_transition_ode1(1.0)
    ode_sol = [test_ode_analog_sol, test_ode_sol, sharp_transition_ode1_sol]
    names = ["test_ode_analog_sol", "test_ode_sol", "sharp_transition_ode1_sol"]
    _plot_sol(ranges, ode_sol, names)
