"""Model Problem ODE."""
import numpy as np


def test_ode(t, y, c=1):
    dydx = c * y
    return dydx


def test_ode_sol(t, c=1):
    y = np.exp(c * t)
    return y
