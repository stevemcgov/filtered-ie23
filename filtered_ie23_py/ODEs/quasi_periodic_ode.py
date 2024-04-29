"""Implementation of Quasi-periodic ODE."""

import numpy as np


def quasi_periodic_ode(t, y):
    y1 = y[1]
    y2 = y[2]
    y3 = y[3]
    y4 = -(np.pi**2 + 1) * y2 - np.pi**2 * y[0]
    yprime = np.array([y1, y2, y3, y4])
    return yprime


def quasi_periodic_ode_sol(t):
    return np.cos(t) + np.cos(np.pi * t)
