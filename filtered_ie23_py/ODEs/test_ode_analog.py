"""Nonautonomous Model Problem  Analog ODE."""

import numpy as np


def set_lambda_test_ode_analog(lambda_input=None):
    if not hasattr(set_lambda_test_ode_analog, "lambda_default"):
        set_lambda_test_ode_analog.lambda_default = 1.0

    if lambda_input is not None:
        set_lambda_test_ode_analog.lambda_default = lambda_input

    lambda_output = set_lambda_test_ode_analog.lambda_default

    return lambda_output


def test_ode_analog(t, y):
    LAMBDA = set_lambda_test_ode_analog()
    dydx = (LAMBDA - 2 * t) * y
    return dydx


def test_ode_analog_sol(t):
    LAMBDA = set_lambda_test_ode_analog()
    y = np.exp(LAMBDA * t - t**2)
    return y
