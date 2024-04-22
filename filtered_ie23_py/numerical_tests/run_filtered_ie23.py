import numpy as np
import matplotlib.pyplot as plt

from filtered_ie23_py import (
    filtered_ie23,
    bdf2,
    ie_pre_post_3,
    test_ode,
    test_ode_sol,
    sharp_transition_ode1,
    sharp_transition_ode1_sol,
)

t_range = [ 0.0 , 1.0 ]
y_init = np.exp( -1.0 )
num_steps = 100000
t_prepost3 , y_prepost3 = ie_pre_post_3 ( sharp_transition_ode1 , t_range , y_init , num_steps )

# plot true
x = np.linspace ( 0.0, 1.0, 1001 )
y = sharp_transition_ode1_sol ( x )
plt.plot ( x, y, 'b-' )
plt.grid ( True )
plt.title( 'True Solution Sharp Transition ODE 1' )
plt.savefig( f'sharp_transition_ode1_sol.jpg')
plt.show( )
plt.plot ( t_prepost3 , y_prepost3 , 'r-' )
plt.grid ( True )
plt.title ( 'y = sharp_transition_ode1_sol IE-Pre-Post-3 (Constant Step)' )
plt.savefig ( f'sharp_transition_ode1_prepost3.jpg' )
plt.show ( )
plt.close ( )

print (f'\nNumber of steps taken: {len(t_prepost3) - 1}')
print (f'Error at final step: {abs( y_prepost3[-1,:][0] - sharp_transition_ode1_sol(t_range[1] ) )}')

print( y_prepost3[-1,:][0] )

t_bdf2 , y_bdf2 = bdf2 ( sharp_transition_ode1 , t_range , y_init , num_steps )

# plot true
x = np.linspace ( 0.0, 1.0, 1001 )
y = sharp_transition_ode1_sol ( x )
plt.plot ( t_bdf2 , y_bdf2 , 'r-' )
plt.grid ( True )
plt.title ( 'y = sharp_transition_ode1_sol BDF2 (Constant Step)' )
plt.savefig ( f'sharp_transition_ode1_bdf2.jpg' )
plt.show ( )
plt.close ( )

print (f'\nNumber of steps taken: {len(t_bdf2) - 1}')
print (f'Error at final step: {abs( y_bdf2[-1,:][0] - sharp_transition_ode1_sol(t_range[1] ) )}')

print( y_bdf2[-1,:][0] )



dt = 0.01
#tol = 0.000075
tol = 0.001
max_steps = 300000
t_prepost_adapt , y_prepost_adapt , e = filtered_ie23 ( sharp_transition_ode1 , t_range , y_init , dt , tol , max_steps )
plt.plot ( x, y, 'b-' )
plt.plot ( t_prepost_adapt , y_prepost_adapt , 'r-' )
plt.grid ( True )
plt.title ( 'y = sharp_transition_ode1_sol Filtered-IE23' )
plt.savefig ( f'sharp_transition_ode1_prepost_adapt.jpg' )
plt.show ( )
plt.close ( )

print (f'\nNumber of steps taken: {len(t_prepost_adapt) - 1}')
print (f'Error at final step: {abs( y_prepost_adapt[-1,:][0] - sharp_transition_ode1_sol(t_range[1] ) )}')

print( y_prepost_adapt[-1,:][0] )