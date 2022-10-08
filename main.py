import matplotlib.pyplot as plt
from misc_functions import read_file, create_time_span

from pmsm import PMSynchronousMotor


if __name__ == '__main__':
    dt = 0.00001
    time = create_time_span(0, 0.5, dt)
    T_sim = []
    motor = PMSynchronousMotor({"dt": dt})

    for t in time:
        torque_em = motor.step(t)
        T_sim.append(torque_em)

    time_m, tau, omega = read_file('matlab_simulation_data/PMSM_dq_model.csv')

    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(time_m, tau, color='r')
    ax.plot(time, T_sim, color='b')
    ax.set_xlim([0, 0.5])
    ax.set_ylim([-900, 900])
    ax.set_title('plot')
    plt.show()
