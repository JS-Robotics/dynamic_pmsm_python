**Motor Introduction**
* https://www.ti.com/download/trng/docs/c2000/TI_MotorControlCompendium_2010.pdf - Reaction and Reluctance torque and saliency

**BLDC/PMSM**
* Odrive reference: https://docs.odriverobotics.com/v/devel/fibre_types/com_odriverobotics_ODrive.html
* k_t from k_V: https://things-in-motion.blogspot.com/2018/12/how-to-estimate-torque-of-bldc-pmsm.html
* Hobby BLDCs are actually PMSMs: https://things-in-motion.blogspot.com/2018/12/why-most-hobby-grade-bldc-out-runners.html
* Permanent Magnet Synchronous and Brushless DC Motor Drives: https://eee.sairam.edu.in/wp-content/uploads/sites/6/2019/07/R.-Krishnan_Permanent_Magnet_Synchronous_and_Brushless_DC_Motor_Drives__Mechanical_Engineering__Marcel_Dekker__.pdf

**Inductance, phase, and line-to-line**
* Understaning PM motorst: https://www.controleng.com/articles/understanding-permanent-magnet-motors/

* L_q approx L_q for SPMs: https://faculty.kashanu.ac.ir/file/download/page/1523859384-freescale-an-4680-pmsm-electrical-parameters-measurement.pdf

* phase is half of line-to-line: https://community.infineon.com/t5/MOTIX-MCU/SOLVED-Questions-about-phase-inductance-and-phase-resistance-in-FOC-Code/td-p/297904

**Control**
* FOC: https://imperix.com/doc/implementation/field-oriented-control-of-pmsm
* FOC made ultra simple: https://www.roboteq.com/applications/all-blogs/13-field-oriented-control-foc-made-ultra-simple

**Misc**
* Table convert: https://tableconvert.com/latex-to-markdown
* Motor Params Odrive: https://discourse.odriverobotics.com/t/odrive-d5065-motor-parameters/1869
* Goat leg and motor dissertation: https://www.ri.cmu.edu/pub_files/2016/8/kaloucheThesis.pdf
* Odrive resources thread: https://discourse.odriverobotics.com/t/recommended-books-resources/382/8
* L = L_q = L_d for SPM (approx zero saliency): https://discourse.odriverobotics.com/t/information-on-the-current-control-loop-structure/6778/14

**NUMERICAL SOLVERS FOR STIFF SYSTEMS**
* http://www.scholarpedia.org/article/Backward_differentiation_formulas
* https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.BDF.html
* https://github.com/scipy/scipy/blob/v1.9.2/scipy/integrate/_ivp/bdf.py#L72-L445
* https://dl.acm.org/doi/pdf/10.1145/355626.355636
* https://iopscience.iop.org/article/10.1088/1742-6596/48/1/026/pdf
* https://www.osaka-kyoiku.ac.jp/~ashino/pdf/2651.pdf
