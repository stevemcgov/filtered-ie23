"""Filtered-IE23."""

def filtered_ie23 ( f_ode , t_range , y_init , dt , TOL , max_steps ):
    """
        RK3 until there are enough steps for adaptive filter.
    """
    import numpy as np
    from scipy.optimize import fsolve

    m = np.size ( y_init )
    t = np.zeros ( 1 )
    y = np.zeros ( ( 1 , m ) )
    e = np.zeros( 1 )
    
    k = 0
    t[k] = t_range[0]
    y[k,:] = y_init

    ### BEGIN RK3 for 0 < k < 3 ============================================================== ###
    while ( k < 3 ):

        # add new t , y , e values
        t = np.append ( t , 0.0 )
        y = np.vstack( ( y , np.zeros( m ) ) )
        e = np.append ( e , 0.0 )

        ta = t[k] + dt / 2
        ya = y[k] + dt / 2 * f_ode( t[k] , y[k] )

        tb = t[k] + dt
        yb = y[k] + dt * ( 2 * f_ode( ta , ya ) - f_ode( t[k] , y[k] ) )

        # estimate solution / true step
        y[k+1] = y[k,:] + \
        dt * ( f_ode ( t[k] , y[k] ) + 4.0 * f_ode ( ta , ya ) + f_ode( tb , yb ) ) / 6.0
        
        t[k+1] = t[k] + dt
        k = k + 1
    ### END RK3 ============================================================================== ###

    # initial the first three timesteps
    knm1 = t[k] - t[k-1]
    knm2 = t[k-1] - t[k-2]
    knm3 = t[k-2] - t[k-3]

    # to be updated in loop
    kn = dt 
    
    while ( t[k] < t_range[1] ):

        # add new t , y , e values in outer loop
        # will be updated until inner loop is satisfied
        t = np.append ( t , 0.0 )
        y = np.vstack ( ( y ,np.zeros ( m ) ) )
        e = np.append ( e , 0.0 )
        
        while ( True ):
            t[k+1] = t[k] + kn

            if( t[k+1] > t_range[1] ):
                t[k+1] = t_range[1]
                kn = t[k+1] - t[k]

            temp_yk , kappa_nm1 = _IE_adaptive_pre_filter( y[k,:] , y[k-1,:] , y[k-2,:] , kn , knm1 , knm2 )
            # y[k+1,:] = fsolve ( _ier_updated , y[k+1, :] , args = ( f_ode , kn , temp_yk , t[k+1] ), xtol=10e-5 )
            # y[k+1,:] = fsolve ( _ier_updated , y[k+1, :] , args = ( f_ode , kn , temp_yk , t[k+1] ), xtol=TOL )
            y[k+1,:] = fsolve ( _ier_updated , y[k+1, :] , args = ( f_ode , kn , temp_yk , t[k+1] ) )
            ynp1_order2 = y[k+1,0]
            y[k+1,:] = _IE_adaptive_post_filter ( y[k+1,:] , y[k,:] , y[k-1,:] , kappa_nm1 , kn , knm1 , knm2 , knm3 )
            ynp1_order3 = y[k+1,0]


            e[k+1] = np.linalg.norm( ynp1_order2 - ynp1_order3 )

            if ( TOL * kn < e[k+1] ):
                kn = kn / 2.0
            elif ( e[k+1] < TOL * kn  / 32.0 ): # original 32
                kn = kn * 2.0
                break
            else:
                break

        k = k + 1
        # add this line to reset steps
        # kn = dt
        knm1 = t[k] - t[k-1]
        knm2 = t[k-1] - t[k-2]
        knm3 = t[k-2] - t[k-3]

        # test
        if ( k > max_steps ):
            print('Reached maximum number of allowable steps.')
            break

    return t , y , e


def _IE_adaptive_pre_filter( y_n , y_nm1 , y_nm2 , kn , knm1 , knm2 ):
    kappa_nm1 = (2*knm2/(knm1+knm2)) * y_n - 2 * y_nm1 + (2*knm1/(knm1+knm2)) * y_nm2
    y_ntilde = y_n - (kn**2/(2*knm1*knm2)) * kappa_nm1
    
    return y_ntilde , kappa_nm1

def _IE_adaptive_post_filter( y_np1 , y_n , y_nm1 , kappa_nm1 , kn , knm1 , knm2 , knm3 ):
    kappa_n = (2*knm1/(kn+knm1)) * y_np1 - 2 * y_n + (2*kn/(kn+knm1)) * y_nm1
    post_filter = -( kn**2 * (knm1 + kn) * (knm2 + 2 * ( knm1 + kn ) ) ) / \
        ( 2*knm1*(2*knm2**2*(knm1+kn) + 3*knm3*(knm2-kn)*(knm1+kn) - 2*knm1*kn*(knm1+kn) + knm2*(knm1**2 - 5*knm1*kn - 7*kn**2)) )
    ynp1_first = y_np1 - post_filter * ( kappa_n - kappa_nm1 )
    
    return ynp1_first

def _ier_updated ( yp, f, kn, yo, tp ):

  value = yp - yo - kn * f ( tp, yp )

  return value

