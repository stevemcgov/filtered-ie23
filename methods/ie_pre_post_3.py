"""IE-Pre-Post-3 constant step method."""


def IE_pre_post_3(f_ode, t_range, y_init, num_steps):
    """3rd Order Filtered Implicit method using RK3 to start.

    Args:
        f_ode: target ODE function passed in
        t_range: [ t1 , t2 ] , beginning and final values for t
        y_init: column vector for initial y value
        num_steps = number of evenly-spaced steps to divide t_range
    Returns:
        t: num_steps + 1 t values as a List
        y: num_steps + 1 rows and k columns , with k-th row containing solution at t[k]
    """
    import numpy as np
    from scipy.optimize import fsolve

    t = np.zeros(num_steps + 1)
    y = np.zeros((num_steps + 1, np.size(y_init)))
    h = (t_range[1] - t_range[0]) / num_steps

    for k in range(0, num_steps + 1):
        if k == 0:
            t[0] = t_range[0]
            y[0, :] = y_init
        else:
            t[k] = t[k - 1] + h
            dt = h
            if k < 3:
                # two intermediate points
                ta = t[k - 1] + dt / 2
                ya = y[k - 1] + dt / 2 * f_ode(t[k - 1], y[k - 1])

                tb = t[k - 1] + dt
                yb = y[k - 1] + dt * (2 * f_ode(ta, ya) - f_ode(t[k - 1], y[k - 1]))

                # estimate solution / true step
                t[k] = t[k - 1] + dt
                y[k, :] = (
                    y[k - 1, :]
                    + dt
                    * (f_ode(t[k - 1], y[k - 1]) + 4.0 * f_ode(ta, ya) + f_ode(tb, yb))
                    / 6.0
                )

            else:
                temp_ykm1 = _IE_pre_filter_2(y[k - 1, :], y[k - 2, :], y[k - 3, :])
                y[k, :] = fsolve(ier, y[k, :], args=(f_ode, t[k - 1], temp_ykm1, t[k]))
                y[k, :] = _IE_post_filter_3(
                    y[k, :], y[k - 1, :], y[k - 2, :], y[k - 3, :]
                )

    return t, y


def _IE_pre_filter_2(y_n, y_nm1, y_nm2):
    """Constant step method pre-filter."""
    y_ntilde = (1.0 / 2.0) * y_n + y_nm1 - (1.0 / 2.0) * y_nm2
    return y_ntilde


def _IE_post_filter_3(y_np1, y_n, y_nm1, y_nm2):
    """Constant step method post-filter."""
    ynp1_third = (
        (6.0 / 11.0) * y_np1
        + (15.0 / 11.0) * y_n
        - (15.0 / 11.0) * y_nm1
        + (5.0 / 11.0) * y_nm2
    )
    return ynp1_third


def ier(yp, f, to, yo, tp):
    """Implicit Euler Residual."""
    value = yp - yo - (tp - to) * f(tp, yp)

    return value
