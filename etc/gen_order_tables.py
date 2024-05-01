
import numpy as np
from filtered_ie23_py import test_ode, test_ode_sol
from filtered_ie23_py import ie_pre_post_3, ie_pre_2


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
                "%.5E" % e[k],
                "\t,\t",
                "%.5E" % r[k],
                "\t,\t",
                "%.5E" % np.log2(r[k]),
            )
            continue

        print(
            num_steps[k], "\t,\t", "%.5E" % e[k], "\t,\t", "%.5E" % r[k], "\t,\t", 0.0
        )

    print("\n\n")
    return


t_range = [0.0, 2.0]
y_init = 1.0
num_steps = np.array([40, 80, 160, 320, 640, 1280, 2560, 5120])
# num_steps = np.array([20, 200, 2000, 20000])
_test_print(
    ie_pre_post_3, "ie-pre-post-3", test_ode, test_ode_sol, t_range, y_init, num_steps
)

_test_print(
    ie_pre_2, "ie-pre-2", test_ode, test_ode_sol, t_range, y_init, num_steps
)