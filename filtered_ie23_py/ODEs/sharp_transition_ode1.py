"""Sharp Transition ODE."""

import numpy as np


def set_lambda_sharp_transition_ode1(lambda_input=None):
    """Set lambda for stiffness."""
    if not hasattr(set_lambda_sharp_transition_ode1, "lambda_default"):
        set_lambda_sharp_transition_ode1.lambda_default = 1.0

    if lambda_input is not None:
        set_lambda_sharp_transition_ode1.lambda_default = lambda_input

    lambda_output = set_lambda_sharp_transition_ode1.lambda_default

    return lambda_output


def sharp_transition_ode1(x, y):
    """Sharp Transition ODE."""
    LAMBDA = set_lambda_sharp_transition_ode1()
    dydx = LAMBDA + y * (-50.0) * np.cos(5 * x) * (np.sin(5 * x) - 1) ** 9
    return dydx


def sharp_transition_ode1_sol(x):
    """Sharp Transition ODE Solution."""
    LAMBDA = set_lambda_sharp_transition_ode1()
    y = LAMBDA * x + np.exp(-1 * (np.sin(5 * x) - 1) ** 10)
    return y
