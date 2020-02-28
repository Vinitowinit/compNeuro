from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pickle
from compute_sta import compute_sta



FILENAME = 'c1p8.pickle'


with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']


# Values of interval sampling and adjacent samples
sampling_period = 2
num_timesteps = 150

sta = compute_sta(stim, rho, num_timesteps)
print(sta)
time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()