from math import sin, cos, pi, sqrt
import csv
import matplotlib.pyplot as plt


def read_file(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        time_s = []
        tau = []
        omega = []
        for row in csv_reader:
            if line_count == 0:
                print(row)
            else:
                time_s.append(float(row[0]))
                tau.append(float(row[1]))
                omega.append(float(row[2]))
            line_count += 1
        return time_s, tau, omega


def create_time_span(t_start, t_end, step_size):
    time_span = []
    time_c = t_start
    while time_c <= t_end:
        time_span.append(time_c)
        time_c += step_size
    time_span.append(time_c)
    return time_span


def clarke_transformation(a, b, c):
    """
    :param a:
    :param b:
    :param c:
    :return: alpha, beta
    """
    alpha = 2 / 3 * (a - 0.5 * b - 0.5 * c)
    beta = 2 / 3 * (sqrt(3) / 2 * b - sqrt(3) / 2 * c)
    return alpha, beta


def park_transformation(alpha, beta, angle):
    d = cos(angle) * alpha + sin(angle) * beta
    q = -sin(angle) * alpha + cos(angle) * beta
    return d, q


if __name__ == '__main__':
    p = 4  # poles
    p_p = p / 2  # pole pairs
    T_rated = 0.8  # Nm
    n_rated = 4500  # rpm
    I_rated = 1.4  # A, rms
    T_load = 15
    J = 0.0027  # kg.m^2
    R_s = 0.0485  # Ohm
    L_s = 0.000395  # H
    b_v = 0.0004924  # Viscous damping
    psi_R = 0.2194
    L_q = 0.5 * L_s
    L_d = L_q
    lambda_m = 4 / 9 * psi_R

    i_q = 0
    i_d = 0

    dt = 0.00001
    time = create_time_span(0, 0.5, dt)
    w_psu = 60 * 2 * pi
    a_psu = 230
    phase_a = 0
    phase_b = -120 * pi / 180
    phase_c = -240 * pi / 180
    theta_e = 0
    w_rotor = 0
    theta_rotor = 0
    T_sim = []

    for t in time:
        u_a = a_psu * sin(w_psu * t + phase_a)
        u_b = a_psu * sin(w_psu * t + phase_b)
        u_c = a_psu * sin(w_psu * t + phase_c)
        u_alpha, u_beta = clarke_transformation(u_a, u_b, u_c)
        u_d, u_q = park_transformation(u_alpha, u_beta, theta_e)

        di_q = u_q / L_q - (R_s*i_q) / L_q - (L_d * p_p * w_rotor * i_d) / L_q - (lambda_m * p_p * w_rotor) / L_q
        di_d = u_d / L_d - (R_s*i_d) / L_d + (L_q * p_p * w_rotor * i_q) / L_d

        i_q = i_q + di_q * dt
        i_d = i_d + di_d * dt

        T_em = 1.5 * p_p * (lambda_m * i_q + (L_d - L_q) * i_d * i_q)

        alpha_motor = 1 / J * (T_em - T_load - w_rotor * b_v)
        w_rotor = w_rotor + alpha_motor * dt
        theta_rotor = theta_rotor + w_rotor * dt
        theta_e = theta_rotor * p_p

        T_sim.append(T_em)
    time2, tau2, omega2 = read_file('matlab_simulation_data/PMSM_dq_model.csv')

    # plot the data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(time2, tau2, color='r')
    ax.plot(time, T_sim, color='b')
    ax.set_xlim([0, 0.5])
    ax.set_ylim([-900, 900])
    ax.set_title('plot')
    plt.show()
