import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100.0
nsamples = 320
F_main = 440.0
F_carry = 5000.0
t = np.arange(nsamples) / sample_rate

f_main = np.sin(2 * np.pi * F_main * t)
f_carry = np.sin(2 * np.pi * F_carry * t)
fam = np.sin(2 * np.pi * F_carry * t)*np.sin(2 * np.pi * F_main * t)

fig = plt.figure(1)
ax = fig.add_subplot(311)
ax.plot(f_carry[1: 300])
ax = fig.add_subplot(312)
ax.plot(f_main[1: 300])
ax = fig.add_subplot(313)
ax.plot(fam[1: 300])
fig.set_tight_layout(True)
plt.show()
