from math import pi, sin
from solver import rk4_single_step
from transforms import clarke_transform, park_transform
from driving_eq import *


class PMSynchronousMotor:
    def __init__(self, moto_params: dict):
        self.b_viscous = 0.0004924  # Viscous damping
        self.b_coulomb = 0.0
        self.p = 4  # poles
        self.t_load = 15
        self.motor_inertia = 0.0027  # kg.m^2
        self.R_s = 0.0485  # Ohm
        L_s = 0.000395  # H
        self.L_q = 0.5*L_s
        self.L_d = self.L_q
        psi_R = 0.2194
        self.lambda_m = 4 / 9 * psi_R
        self.dt = 0.000005
        # Initial conditions
        self.u_d = 0
        self.u_q = 0
        self.i_q = 0
        self.i_d = 0
        self.theta_e = 0
        self.w_rotor = 0
        self.theta_rotor = 0

        self.w_psu = 60 * 2 * pi
        self.a_psu = 230
        self.phase_a = 0
        self.phase_b = -120 * pi / 180
        self.phase_c = -240 * pi / 180

    def step(self, time):
        u_a = self.a_psu * sin(self.w_psu * time + self.phase_a)
        u_b = self.a_psu * sin(self.w_psu * time + self.phase_b)
        u_c = self.a_psu * sin(self.w_psu * time + self.phase_c)
        u_alpha, u_beta = clarke_transform(u_a, u_b, u_c)
        self.u_d, self.u_q = park_transform(u_alpha, u_beta, self.theta_e)

        self.i_q = rk4_single_step(self.di_q_func, self.dt, time, self.i_q)
        self.i_d = rk4_single_step(self.di_d_func, self.dt, time, self.i_d)

        torque_em = 1.5 * self.p/2 * (self.lambda_m * self.i_q + (self.L_d - self.L_q) * self.i_d * self.i_q)

        alpha_motor = 1 / self.motor_inertia * (torque_em - self.t_load - self.w_rotor * self.b_viscous)
        self.w_rotor = self.w_rotor + alpha_motor * self.dt
        self.theta_rotor = self.theta_rotor + self.w_rotor * self.dt + 0.5*alpha_motor*self.dt**2
        self.theta_e = self.theta_rotor * self.p/2
        return torque_em

    def di_q_func(self, t, y):
        # y = self.i_q
        di_q = self.u_q / self.L_q - (self.R_s * y) / self.L_q - \
               (self.L_d * self.p/2 * self.w_rotor * self.i_d) / self.L_q - \
               (self.lambda_m * self.p/2 * self.w_rotor) / self.L_q
        return di_q

    def di_d_func(self, t, y):
        # y = self.i_d
        di_d = self.u_d / self.L_d - (self.R_s * y) / self.L_d + \
               (self.L_q * self.p/2 * self.w_rotor * self.i_q) / self.L_d
        return di_d

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
