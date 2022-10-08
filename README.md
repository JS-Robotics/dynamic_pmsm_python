# Dynamic Permanent Magnet Synchronous Motor

$$ \frac{d}{dt}i_q = \frac{V_q}{L_q} - i_q\frac{R_s}{L_q} - \frac{\omega_e L_d i_d}{L_q} - \frac{\omega_e
\lambda_m}{L_q} $$

$$ \frac{d}{dt}i_d = \frac{V_d}{L_d} - i_d\frac{R_s}{L_d} + \frac{\omega_e L_q i_q}{L_d} $$

$$ T_m = \frac{3}{2}\cdot\frac{p}{2}\left[\lambda_mi_q + (L_d - L_q)i_qi_d\right] $$

$$ \omega_e = \frac{p}{2}\omega_m $$

$$ k_t = \frac{15\sqrt{3}}{\pi K_V}$$

$$ \lambda_m = \frac{2k_t}{3p_p} = \frac{2\cdot15\sqrt{3}}{3\pi} \frac{1}{p_pK_V} $$ 

Where:

| Symbol:     |     | Description:                | Value: | Unit:    |
|-------------|-----|-----------------------------|--------|----------|
| $\lambda_m$ | -   | Flux linkage                | $\sim$ | $Wb$     |
| $\omega_e$  | -   | Electrical angular velocity | $\sim$ | $rad/s$  |
| $\omega_m$  | -   | Mechanical angular velocity | $\sim$ | $rad/s$  |
| $p_p$       | -   | Motor pole pairs            | $\sim$ | $-$      |