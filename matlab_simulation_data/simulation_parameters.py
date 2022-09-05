"""
This file contains the parameters utilized in the MatLab Simulink simulations.
The power source in the simulations has the following parameters
    f = 60Hz
    a = 230V
    phase_a = 0
    phase_b = -120deg
    phase_c = -240deg

PMSM_dq_model.csv - Uses the dq-frame dynamic equation to drive the simulation, which are
                    from "DYNAMIC MODEL OF PM SYNCHRONOUS MOTORS", by D. Y. Ohm - Published 2000.
                    This is the same model used by ODrive

PMSM_flux_model.csv - A model driven by flux dynamic equations presented in "Control of Voltage-Source Converters
                      and Variable-Speed Drives", by Lennart Harnefors,
                                                    Marko Hinkkanen,
                                                    Oskar Wallmark,
                                                    and Alejandro Gomez Yepes

PMSM_simlnk_model.csv - Is a simulation of a PMSM utilizing Matlab's Simulink, Simscape (Simscape Electrical) block.

Note: The simulation of the simulink and the dq-frame model are equivalent in values.
      (The small difference is due to the voltage source amplitude is not 230A, but ~230A).
      However, the flux dynamic model has a large deviation, it still has to be determined why.
"""

# Electrical parameters of PMSM motor
p = 4  # poles
n_p = p / 2  # pole pairs
T_rated = 0.8  # Nm
n_rated = 4500  # rpm
I_rated = 1.4  # A, rms
J = 0.0027  # kg.m^2
R_s = 0.0485  # Ohm
L_s = 0.000395  # H
b = 0.0004924  # Viscous damping
# Calculated parameters:
# psi_R= 3*T_rated/sqrt(2)/p/I_rated;
psi_R = 0.2194

# Transformation matrices:
# T32 = [1 -1/2 -1/2; 0 sqrt(3)/2 -sqrt(3)/2 ];
# T23 = [2/3 0; -1/3 1/sqrt(3); -1/3 -1/sqrt(3)];

# dq model
# L_s = 1/2(L_d + L_q) here it is assumed that L_q = L_d
L_q = 0.5 * L_s
L_d = L_q
lambda_m = 4 / 9 * psi_R
