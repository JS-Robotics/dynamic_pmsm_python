import csv
import matplotlib.pyplot as plt
import numpy as np

with open('PMSM_simlnk_block.csv') as csv_file:
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

print(len(time), len(tau), len(omega))
# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
time = np.array(time)
tau = np.array(tau)
omega = np.array(omega)
t = np.arange(0.0, 2.0, 0.0004)
s = 1 + np.sin(2 * np.pi * t)
print(f'len t: {len(t)}')
print(time[-1])
ax.plot(time, tau, color='k')

# set the limits
ax.set_xlim([0, 0.5])
ax.set_ylim([-900, 900])

ax.set_title('plot')

# display the plot
plt.show()
