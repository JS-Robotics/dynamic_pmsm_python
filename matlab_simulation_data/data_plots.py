import csv
import matplotlib.pyplot as plt
import numpy as np


def read_file(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        time = []
        tau = []
        omega = []
        for row in csv_reader:
            if line_count == 0:
                print(row)
            else:
                time.append(float(row[0]))
                tau.append(float(row[1]))
                omega.append(float(row[2]))
            line_count += 1
        return time, tau, omega


time1, tau1, omega1 = read_file('PMSM_flux_model.csv')
time2, tau2, omega2 = read_file('PMSM_dq_model.csv')
time3, tau3, omega3 = read_file('PMSM_simlnk_block.csv')

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
time1 = np.array(time1)
tau1 = np.array(tau1)
omega1 = np.array(omega1)
print(time1[-1])
#ax.plot(time1, tau1, color='k')
ax.plot(time2, tau2, color='r')
ax.plot(time3, tau3, color='b')



# set the limits
ax.set_xlim([0, 0.5])
ax.set_ylim([-900, 900])

ax.set_title('plot')

# display the plot
plt.show()
