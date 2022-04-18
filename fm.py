import numpy as np
import matplotlib.pyplot as plt

sample_rate = 44100.0
nsamples = 320
V_main = 440.0
V_carry = 5000.0
t = np.arange(nsamples) / sample_rate

v_main = np.sin(2 * np.pi * V_main * t)
v_carry = np.sin(2 * np.pi * V_carry * t)
vfm = np.sin(2 * np.pi * V_carry * t + 6.0 * -np.cos(2 * np.pi * V_main * t))

fig = plt.figure(1)
ax = fig.add_subplot(311)
ax.plot(v_carry[1: 300])
ax = fig.add_subplot(312)
ax.plot(v_main[1: 300])
ax = fig.add_subplot(313)
ax.plot(vfm[1: 300])
fig.set_tight_layout(True)
plt.show()
