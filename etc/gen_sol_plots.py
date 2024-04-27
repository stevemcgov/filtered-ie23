import numpy as np
import matplotlib.pyplot as plt

from filtered_ie23_py import (
    test_ode_analog_sol,
    test_ode_sol,
    test_ode_analog_sol,
    set_lambda_test_ode_analog,
    sharp_transition_ode1_sol,
    set_lambda_sharp_transition_ode1,
)


def _plot_sol(ranges, ode_sol, names):
    for r, sol, name in zip(ranges, ode_sol, names):
        t = np.linspace(r[0], r[1], 10001)
        y = sol(t)
        plt.plot(t, y, "b-")
        plt.grid(True)
        plt.ylabel('y axis')
        plt.xlabel('t axis')
        plt.title(f"y = {name}")
        plt.savefig(f"{name}.jpg")
        plt.show()
        plt.close()

def _plot_sol_lam(r, ode_sol, set_lambda, lams, name):
    for lam in lams:
        set_lambda(lam)
        t = np.linspace(r[0], r[1], 10001)
        y = ode_sol(t)
        plt.plot(t, y, "b-")
        plt.grid(True)
        plt.ylabel('y axis')
        plt.xlabel('t axis')
        plt.title(f"y = {name}; Lambda = {lam}")
        plt.savefig(f"{name}_lambda_{lam}.jpg")
        plt.show()
        plt.close()



if __name__ == "__main__":
    ranges = [[0.0, 20.0], [0.0, 2.0], [0.0, 1.0]]
    set_lambda_sharp_transition_ode1(1.0)
    ode_sol = [test_ode_analog_sol, test_ode_sol, sharp_transition_ode1_sol]
    names = ["Model ODE Analog", "Model ODE", "Sharp Transition"]
    _plot_sol(ranges, ode_sol, names)
    _plot_sol_lam([0.0, 10.0], test_ode_analog_sol, set_lambda_test_ode_analog, [1, 3, 5, 5.7, 6], "Model ODE Analog")
