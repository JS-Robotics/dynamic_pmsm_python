from math import pi, sin
from solver import rk4_single_step
from transforms import clarke_transform, park_transform, inverse_clarke_transform, inverse_parke_transform


class PMSynchronousMotor:
    def __init__(self, enable_foc: False, moto_params: dict):
        self.enable_foc = enable_foc

        # Motor Parameters
        self.b_viscous = 0.001  # Viscous damping
        self.b_coulomb = 0.001
        self.p = 14  # poles
        KV = 270
        kt = 8.27 / KV
        self.t_load = 0.5
        self.motor_inertia = 1e-4  # kg.m^2
        self.R_s = 0.039  # Ohm
        phase_inductance = 0.0000157  # H
        self.L_q = phase_inductance
        self.L_d = phase_inductance
        self.lambda_m = 2 * kt / (3 * self.p / 2)
        self.dt = moto_params['dt']

        # FOC parameters
        self.i_q_ref = 0 * 4 / (3 * self.p * self.lambda_m)
        self.i_d_ref = 0

        # Initial conditions
        self.u_d = 0
        self.u_q = 0
        self.i_q = 0
        self.i_d = 0
        self.theta_e = 0
        self.w_rotor = 0
        self.theta_rotor = 0
        self.torque_em = 0

        # Power Supply Unit (PSU) parameters
        self.w_psu = 60 * 2 * pi
        self.a_psu = 230
        self.phase_a = 0
        self.phase_b = -120 * pi / 180
        self.phase_c = -240 * pi / 180

    def step(self, time):
        if not self.enable_foc:
            u_a = self.a_psu * sin(self.w_psu * time + self.phase_a)
            u_b = self.a_psu * sin(self.w_psu * time + self.phase_b)
            u_c = self.a_psu * sin(self.w_psu * time + self.phase_c)
            u_alpha, u_beta = clarke_transform(u_a, u_b, u_c)
        else:
            if time > 0.25:
                self.i_q_ref = 1 * 4/(3*self.p*self.lambda_m)
            else:
                self.i_q_ref = 0
            i_q_error = self.i_q_ref - self.i_q
            i_d_error = self.i_d_ref - self.i_d
            u_q = i_q_error * 12000
            u_d = i_d_error * 12000
            u_alpha, u_beta = inverse_parke_transform(u_d, u_q, self.theta_e)
            u_a, u_b, u_c = inverse_clarke_transform(u_alpha, u_beta)
            u_alpha, u_beta = clarke_transform(u_a, u_b, u_c)

        self.u_d, self.u_q = park_transform(u_alpha, u_beta, self.theta_e)

        self.i_q = rk4_single_step(self.di_q_func, self.dt, time, self.i_q)
        self.i_d = rk4_single_step(self.di_d_func, self.dt, time, self.i_d)

        self.torque_em = 1.5 * self.p / 2 * (self.lambda_m * self.i_q + (self.L_d - self.L_q) * self.i_d * self.i_q)

        alpha_motor = 1 / self.motor_inertia * (self.torque_em - self.t_load - self.w_rotor * self.b_viscous)
        self.w_rotor = rk4_single_step(self.mot_func, self.dt, time, self.w_rotor)
        self.theta_rotor = self.theta_rotor + self.w_rotor * self.dt + 0.5 * alpha_motor * self.dt ** 2
        self.theta_e = self.theta_rotor * self.p / 2
        return self.torque_em

    def di_q_func(self, t, y):
        # y = self.i_q
        di_q = (self.u_q - (self.R_s * y) - (self.L_d * self.p / 2 * self.w_rotor * self.i_d) -
                (self.lambda_m * self.p / 2 * self.w_rotor)) / self.L_q
        return di_q

    def di_d_func(self, t, y):
        # y = self.i_d
        di_d = (self.u_d - (self.R_s * y) + (self.L_q * self.p / 2 * self.w_rotor * self.i_q)) / self.L_d
        return di_d

    def mot_func(self, t, y):
        # y = self.w_rotor
        torque_em = 1 / self.motor_inertia * (self.torque_em - self.t_load - y * self.b_viscous)
        return torque_em

    def validate_dict(self, motor_dict: dict):
        if "L" not in motor_dict:
            print(f"Motor param 'L' is missing")
            return False
        if "R" not in motor_dict:
            print(f"Motor param 'R' is missing")
            return False
        if "poles" not in motor_dict:
            print(f"Motor param 'poles' is missing")
            return False
        if "b_viscous" not in motor_dict:
            print(f"Motor param 'b_viscous' missing, defaulting to 0")
        else:
            self.b_viscous = motor_dict['b_viscous']
        return True


if __name__ == "__main__":
    motor = PMSynchronousMotor({})
    motor.step(0)
    motor.step(0)
    motor.step(0)
