#While working for ONGC, I recieved three wavelets of 40 millisecond signal length. 
#Plotting these wavelets and finding the correlation between them is the purpose of the code.
#The input of these time-series is taken as a list of Amplitudes inside the code itself. 

import matplotlib.pyplot as plt
import numpy as np

Time_stamps1 = list(range(1530, 1571, 2))
Amplitudes1 = [-0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835, 2.7966, 1.96388, 1.23775,0.51741]
plt.subplot(1,3,1)
plt.plot(Time_stamps1, Amplitudes1)
plt.xlabel('Time-stamps')
plt.ylabel('Amplitudes')
plt.title('Wave 1530-1570')

Time_stamps2 = list(range(1990, 2031, 2))
Amplitudes2 = [0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215,-2.22282]
plt.subplot(1,3,2)
plt.plot(Time_stamps2, Amplitudes2)
plt.xlabel('Time-stamps')
plt.ylabel('Amplitudes')
plt.title('Wave 1990-2030')

Time_comp = list(range(42, 81, 2))
Amplitudes_comp = [-0.285072, -0.247312, -0.188979, -0.114313, -0.0290429, 0.0600894, 0.145894, 0.221354, 0.28024, 0.317659, 0.33049, 0.317659, 0.28024, 0.221354, 0.145894, 0.0600894, -0.0290429, -0.114313, -0.188979, -0.247312]
plt.subplot(1,3,3)
plt.plot(Time_comp, Amplitudes_comp)
plt.xlabel('Time-stamps')
plt.ylabel('Amplitudes')
plt.title('Default Wave')
plt.tight_layout()


cross_corr1 = np.correlate(Amplitudes1, Amplitudes_comp, mode= 'valid')
percentage1 = (cross_corr1.max() / (np.linalg.norm(Amplitudes1) * np.linalg.norm(Amplitudes_comp))) * 100


print("Cross-Correlation Percentage with 1530-1571: {:.2f}%".format(percentage1))

cross_corr2 = np.correlate(Amplitudes2, Amplitudes_comp, mode='valid')
percentage2 = (cross_corr2.max() / (np.linalg.norm(Amplitudes2) * np.linalg.norm(Amplitudes_comp))) * 100


print("Cross-Correlation Percentage with 1990-2031: {:.2f}%".format(percentage2))
plt.show()