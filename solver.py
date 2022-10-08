
def rk4_single_step(func, dt, t_k, y_k):
    """
    This function performs a single 4th order Runge-Kutta integration.
    :param func: The ODE that will be used for the integration step
    :param dt: The step time
    :param t_k: The current time of the ODE
    :param y_k: The current state of the ODE
    :return: y_(k+1) The system integrated one time step
    """
    f1 = func(t_k, y_k)
    f2 = func(t_k+dt/2, y_k+(dt/2)*f1)
    f3 = func(t_k+dt/2, y_k+(dt/2)*f2)
    f4 = func(t_k+dt, y_k+dt*f3)
    y_k1 = y_k + (dt/6) * (f1 + 2*f2 + 2*f3 + f4)
    return y_k1
