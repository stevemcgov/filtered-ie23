
import numpy as np
from filtered_ie23_pkg import test_ode, test_ode_sol
from filtered_ie23_pkg import ie_pre_post_3


def _test_print(method, method_name, ode, ode_sol, t_range, y_init, num_steps):

    print(f"\n\n{method_name}:\n")
    print("num_steps\t,\terror\t\t,\t\tratio\t\t,\tconv. rate")

    SIZE = len(num_steps)

    y_exact = ode_sol(t_range[1])
    final_y = np.zeros(SIZE)
    e = np.zeros(SIZE)
    r = np.zeros(SIZE)

    for k in range(0, SIZE):
        t, y = method(ode, t_range, y_init, num_steps[k])
        final_y[k] = y[num_steps[k]]
        e[k] = abs(final_y[k] - y_exact)

    for k in range(0, SIZE - 1):
        r[k] = e[k] / e[k + 1]

    for k in range(0, SIZE):
        if k < SIZE - 1:
            print(
                num_steps[k],
                "\t,\t",
                "%.15f" % e[k],
                "\t,\t",
                "%.15f" % r[k],
                "\t,\t",
                "%.15f" % np.log2(r[k]),
            )
            continue

        print(
            num_steps[k], "\t,\t", "%.15f" % e[k], "\t,\t", "%.15f" % r[k], "\t,\t", 0.0
        )

    print("\n\n")
    return


t_range = [0.0, 1.0]
y_init = 1.0
num_steps = np.array([40, 80, 160, 320, 640, 1280, 2560, 5120])
_test_print(
    ie_pre_post_3, "ie-Pre-Post-3", test_ode, test_ode_sol, t_range, y_init, num_steps
)