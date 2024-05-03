"""van der Pol DE."""
import numpy as np


def set_mu(mu_input=None):
    """Set damping."""
    if not hasattr(set_mu, "mu_default"):
        set_mu.mu_default = 1.0

    if mu_input is not None:
        set_mu.mu_default = mu_input

    mu_output = set_mu.mu_default

    return mu_output


def vanderpol_deriv(t, y):
    """Return van der Pol derivative."""
    MU = set_mu()
    u = y[0]
    v = y[1]

    uprime = v
    vprime = MU * (1.0 - u**2) * v - u

    return np.array([uprime, vprime])
