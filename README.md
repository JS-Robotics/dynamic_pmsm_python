# Dynamic Permanent Magnet Synchronous Motor

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
| $R_s$       | -   | Phase resistance                | $\sim$ | $\Ohm$    |
| $b_v$       | -   | Viscous damping                 | $\sim$ | $Nms/rad$ |

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