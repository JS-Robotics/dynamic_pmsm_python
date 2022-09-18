def di_q_func(u_q, L_q, L_d, R_s, i_q, i_d, p_p, w_rotor, lambda_m):
    di_q_r = u_q / L_q - (R_s * i_q) / L_q - (L_d * p_p * w_rotor * i_d) / L_q - (lambda_m * p_p * w_rotor) / L_q
    return di_q_r


def di_d_func(u_d, L_q, L_d, R_s, i_q, i_d, p_p, w_rotor, lambda_m):
    di_d_r = u_d / L_d - (R_s * i_d) / L_d + (L_q * p_p * w_rotor * i_q) / L_d
    return di_d_r
