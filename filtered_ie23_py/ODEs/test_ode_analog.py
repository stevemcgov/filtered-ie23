"""Nonautonomous Model Problem  Analog ODE."""
import numpy as np


def test_ode_analog(t, y):
    dydx =  (6-2*t)*y
    return dydx


def test_ode_analog_sol(t):
    y = np.exp(6*t-t**2)
    return y
