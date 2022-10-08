import csv


def di_q_func(u_q, L_q, L_d, R_s, i_q, i_d, p_p, w_rotor, lambda_m):
    di_q_r = u_q / L_q - (R_s * i_q) / L_q - (L_d * p_p * w_rotor * i_d) / L_q - (lambda_m * p_p * w_rotor) / L_q
    return di_q_r


def di_d_func(u_d, L_q, L_d, R_s, i_q, i_d, p_p, w_rotor):
    di_d_r = u_d / L_d - (R_s * i_d) / L_d + (L_q * p_p * w_rotor * i_q) / L_d
    return di_d_r


def read_file(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        time_s = []
        tau = []
        omega = []
        for row in csv_reader:
            if line_count == 0:
                pass  # Skipping row with headers
            else:
                time_s.append(float(row[0]))
                tau.append(float(row[1]))
                omega.append(float(row[2]))
            line_count += 1
        return time_s, tau, omega


def create_time_span(t_start, t_end, step_size):
    """
    Create a timespan from t_start to t_end with step_size increments.
    :param t_start: start time
    :param t_end: end time
    :param step_size: step size (delta time)
    :return: A list of the timespan
    """
    time_span = []
    time_c = t_start
    while time_c <= t_end:
        time_span.append(time_c)
        time_c += step_size
    time_span.append(time_c)
    return time_span
