# Dynamic Permanent Magnet Synchronous Motor
Notes: 
* **FOC is working**, however a solver similar to Matlab's ODE15s. 
ode15s is a variable-step, variable-order (VSVO) solver based on the numerical differentiation formulas (NDFs) of 
orders 1 to 5. Optionally, it can use the backward differentiation formulas (BDFs, also known as Gear's method) 
that are usually less efficient. Like ode113, ode15s is a multistep solver. Use ode15s if ode45 fails or is very 
inefficient, and you suspect that the problem is stiff, or when solving a differential-algebraic equation (DAE) 


* It has been verified that a similar behaviour occurs in matlab with ode4 (4th Order Runge-Kutta) solver in Matlab/Simulink

### Dynamic driving equations ###

$$ \frac{d}{dt}i_q = \frac{u_q}{L_q} - i_q\frac{R_s}{L_q} - \frac{\omega_e L_d i_d}{L_q} - \frac{\omega_e
\lambda_m}{L_q} $$

$$ \frac{d}{dt}i_d = \frac{u_d}{L_d} - i_d\frac{R_s}{L_d} + \frac{\omega_e L_q i_q}{L_d} $$

$$ T_{em} = \frac{3}{2}\cdot\frac{p}{2}\left[\lambda_mi_q + (L_d - L_q)i_qi_d\right] $$

$$ \alpha_m = \frac{1}{J}(T_{em} - T_{load} - \omega_m b_v) $$

Where:

| Symbol:     |     | Description:                    | Value: | Unit:     |
|-------------|-----|---------------------------------|--------|-----------|
| $\lambda_m$ | -   | Flux linkage                    | $\sim$ | $Wb$      |
| $\omega_e$  | -   | Electrical angular velocity     | $\sim$ | $rad/s$   |
| $\omega_m$  | -   | Mechanical angular velocity     | $\sim$ | $rad/s$   |
| $\alpha_m$  | -   | Mechanical angular acceleration | $\sim$ | $rad/s^2$ |
| $i_q$       | -   | q-axis current                  | $\sim$ | $A$       |
| $i_d$       | -   | d-axis current                  | $\sim$ | $A$       |
| $u_q$       | -   | q-axis voltage                  | $\sim$ | $V$       |
| $u_d$       | -   | d-axis voltage                  | $\sim$ | $V$       |
| $T_{em}$    | -   | Electromagnetic torque          | $\sim$ | $Nm$      |
| $T_{load}$  | -   | External load torque            | $\sim$ | $Nm$      |
| $L_q$       | -   | Quadrature inductance           | $\sim$ | $H$       |
| $L_d$       | -   | Direct inductance               | $\sim$ | $H$       |
| $R_s$       | -   | Phase resistance                | $\sim$ | $\Omega$  |
| $b_v$       | -   | Viscous damping                 | $\sim$ | $Nms/rad$ |
| $J$         | -   | Motor inertia                   | $\sim$ | $kg/m^2$  |

#### Aux equations ####

$$ \omega_e = \frac{p}{2}\omega_m $$

$$ k_t = \frac{15\sqrt{3}}{\pi K_V}$$

$$ \lambda_m = \frac{2k_t}{3p_p} = \frac{2\cdot15\sqrt{3}}{3\pi} \frac{1}{p_pK_V} $$

| Symbol:     |     | Description:                | Value: | Unit:      |
|-------------|-----|-----------------------------|--------|------------|
| $\lambda_m$ | -   | Flux linkage                | $\sim$ | $Wb$       |
| $\omega_e$  | -   | Electrical angular velocity | $\sim$ | $rad/s$    |
| $\omega_m$  | -   | Mechanical angular velocity | $\sim$ | $rad/s$    |
| $p_p$       | -   | Motor pole pairs            | $\sim$ | $-$        |
| $k_t$       | -   | Torque constant             | $\sim$ | $Nm/A$     |
| $K_V$       | -   | Speed Constant              | $\sim$ | $rad/(sV)$ |