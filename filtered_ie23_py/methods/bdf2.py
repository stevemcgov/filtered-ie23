"""Standard BDF2 implementation."""


def bdf2(f, tspan, y0, n):
    """BDF2 with implicit Euler as first step."""
    from scipy.optimize import fsolve
    import numpy as np

    if np.ndim(y0) == 0:
        m = 1
    else:
        m = len(y0)

    t = np.linspace(tspan[0], tspan[1], n + 1)
    y = np.zeros([n + 1, m])

    dt = (tspan[1] - tspan[0]) / float(n)

    for i in range(0, n + 1):

        if i == 0:

            y[i, :] = y0

        elif i == 1:

            to = t[i - 1]
            yo = y[i - 1, :]
            th = t[i - 1] + 0.5 * dt
            yh = y[i - 1, :] + 0.5 * dt * f(t[i - 1], y[i - 1, :])

            yh = fsolve(_implicit_euler_residual, yh, args=(f, to, yo, th))

            y[i, :] = 2.0 * yh - y[i - 1, :]

        else:

            y1 = y[i - 2, :]
            y2 = y[i - 1, :]
            t3 = t[i]
            y3 = y[i - 1, :] + dt * f(t[i - 1], y[i - 1, :])

            y3 = fsolve(_bdf2_residual, y3, args=(f, dt, t3, y1, y2))

            y[i, :] = y3

    return t, y


def _bdf2_residual(y3, f, dt, t3, y1, y2):
    """
    Compute residual for bdf2.

    3 Y3 - 4 Y2 + Y1 = 2 * DT * F ( T3, Y3 )
    """
    value = 3.0 * y3 - 4.0 * y2 + y1 - 2.0 * dt * f(t3, y3)

    return value


def _implicit_euler_residual(yp, f, to, yo, tp):
    """
    Compute residual for implicit euler.

    YP = YO + ( TP - TO ) * F ( TP, YP )
    """
    value = yp - yo - (tp - to) * f(tp, yp)

    return value
