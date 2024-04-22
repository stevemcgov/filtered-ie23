
import numpy as np
import matplotlib.pyplot as plt

from filtered_ie23_py import (
    filtered_ie23,
    ie_pre_post_3,
    test_ode,
    test_ode_sol,
)

# update tol in constant step method
t_range = [ 0.0 , 2.0 ]
y_init = 1.0
num_steps = 200
tol = 0.000075
tol = 0.001
t_prepost3 , y_prepost3 = ie_pre_post_3 ( test_ode , t_range , y_init , num_steps )

# plot true
x = np.linspace ( 0.0, 1.0, 1001 )
y = test_ode_sol ( x )
plt.plot ( x, y, 'b-' )
plt.plot ( t_prepost3 , y_prepost3 , 'r-' )
plt.grid ( True )
plt.title ( 'y = test_ode_sol IE-Pre-Post-3' )
plt.savefig ( f'new_test_ode_prepost3.jpg' )
plt.show ( )
plt.close ( )

print (f'\nNumber of steps taken: {len(t_prepost3) - 1}')
print (f'Error at final step:{abs( y_prepost3[-1,:][0] - test_ode_sol(t_range[1] ) ):.5E}')

# print( y_prepost3[-1,:][0] )




dt = 0.01
tol = 0.001
dt = 0.004
tol = 0.0001
max_steps = 10000000
t_prepost_adapt , y_prepost_adapt , e = filtered_ie23 ( test_ode , t_range , y_init , dt , tol , max_steps )
plt.plot ( x, y, 'b-' )
plt.plot ( t_prepost_adapt , y_prepost_adapt , 'r-' )
plt.grid ( True )
plt.title ( 'y = test_ode_sol IE-Pre-Post-Adaptive' )
plt.savefig ( f'test_ode_prepost_adapt.jpg' )
plt.show ( )
plt.close ( )

print (f'\nNumber of steps taken: {len(t_prepost_adapt) - 1}')
print (f'Error at final step:{abs( y_prepost_adapt[-1,:][0] - test_ode_sol(t_range[1] ) ):.5E}')

# print( y_prepost_adapt[-1,:][0] )

