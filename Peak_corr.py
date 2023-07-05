#To Calculate and plot the time lag between peaks of Cross-correlation of two time-series.
#Also finding the phase angle lag between the datasets.

import numpy as np
import matplotlib.pyplot as plt

#input as list of Amplitudes.
Amplitude1 = [-0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835, 2.7966, 1.96388, 1.23775]
Amplitude2 = [0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215]
Amplitude_comp1 = [-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -0.00260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228,0.0744249]
Amplitude_comp2 = [-0.013995, -0.0186956, -0.0275364, -0.0311656, -0.0149192, 0.0346624, 0.12169, 0.23547, 0.351297, 0.438163, 0.470425, 0.438163, 0.351297, 0.23547, 0.12169, 0.0346624, -0.0149192, -0.0311656, -0.0275364, -0.0186956]

#Find Correlation & Corr %age
cross_corr = np.correlate(Amplitude1, Amplitude_comp2, mode='full')
percentage1 = (cross_corr.max() / (np.linalg.norm(Amplitude1) * np.linalg.norm(Amplitude_comp2))) * 100

print("Cross-corr:{:.2f}%".format(percentage1))
print(cross_corr)
print(np.argmax(cross_corr))

#Find peak lag
peak_lag = np.argmax(cross_corr) - (len(Amplitude1) - 1)
time_lag = peak_lag  

plt.figure(figsize=(8, 4))
plt.plot(cross_corr)
plt.xlabel('Lag')
plt.ylabel('Cross-Correlation')
plt.title('Cross-Correlation between Time Series')
plt.axvline(x=peak_lag + (len(Amplitude2) - 1), color='r', linestyle='--', label='Peak Lag')
plt.legend()

print("Time Lag between Peaks of Cross-Correlations:", time_lag, "units")

period = 40 

phase_angle_lag = (time_lag / period) * 360

print("Phase Angle Lag between Time Series:", phase_angle_lag, "degrees")
plt.show()
