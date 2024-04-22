"""Standard BDF3 implementations."""

def bdf3(f, tspan, y0, n):
    """BDF3 with IE and BDF2 buildup steps."""
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

        elif i == 2:

            y1 = y[i - 2, :]
            y2 = y[i - 1, :]
            t3 = t[i]
            y3 = y[i - 1, :] + dt * f(t[i - 1], y[i - 1, :])

            y3 = fsolve(_bdf2_residual, y3, args=(f, dt, t3, y1, y2))

            y[i, :] = y3

        else:
            y1 = y[i - 3, :]
            y2 = y[i - 2, :]
            y3 = y[i - 1, :]
            t4 = t[i]
            y4 = y[i - 1, :] + dt * f(t[i - 1], y[i - 1, :])

            y4 = fsolve(_bdf3_residual, y4, args=(f, dt, t4, y1, y2, y3))

            y[i, :] = y4

    return t, y


def bdf3_v2(f, tspan, y0, n):
    """BDF3 with RK3 buildup steps."""
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

        elif i < 3:
            # two intermediate points
            xa = t[i - 1] + dt / 2
            ya = y[i - 1] + dt / 2 * f(t[i - 1], y[i - 1])

            xb = t[i - 1] + dt
            yb = y[i - 1] + dt * (2 * f(xa, ya) - f(t[i - 1], y[i - 1]))

            # estimate solution / true step
            y[i, :] = (
                y[i - 1, :]
                + dt * (f(t[i - 1], y[i - 1]) + 4.0 * f(xa, ya) + f(xb, yb)) / 6.0
            )

        else:
            y1 = y[i - 3, :]
            y2 = y[i - 2, :]
            y3 = y[i - 1, :]
            t4 = t[i]
            y4 = y[i - 1, :] + dt * f(t[i - 1], y[i - 1, :])

            y4 = fsolve(_bdf3_residual, y4, args=(f, dt, t4, y1, y2, y3))

            y[i, :] = y4

    return t, y


def _implicit_euler_residual(yp, f, to, yo, tp):
    """
    Compute residual for implicit euler.

    YP = YO + ( TP - TO ) * F ( TP, YP )
    """
    value = yp - yo - (tp - to) * f(tp, yp)

    return value


def _bdf2_residual(y3, f, dt, t3, y1, y2):
    """
    Compute residual for bdf2.

    3 Y3 - 4 Y2 + Y1 = 2 * DT * F ( T3, Y3 )
    """
    value = 3.0 * y3 - 4.0 * y2 + y1 - 2.0 * dt * f(t3, y3)

    return value


def _bdf3_residual(y4, f, dt, t4, y1, y2, y3):
    """
    Compute residual for bdf3.

    11 Y4 - 18 Y3 + 9 Y2 - 2 Y1 = 6 * H * F ( T4 , Y4 )
    """
    value = 11.0 * y4 - 18.0 * y3 + 9.0 * y2 - 2.0 * y1 - 6.0 * dt * f(t4, y4)

    return value
