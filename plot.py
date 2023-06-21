import matplotlib.pyplot as plt
import numpy as np


Time_stamps1 = list(range(1990, 2031, 2))
Amplitudes1 = [0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215,-2.22282]
plt.subplot(1, 2, 1)
plt.plot(Time_stamps1, Amplitudes1)
plt.xlabel('Time-stamps')
plt.ylabel('Amplitudes')
plt.title('Wave 1')

Time_stamps2 = list(range(42, 81, 2))
Amplitudes2 = [-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -0.00260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228, 0.0744249]
plt.subplot(1, 2, 2)
plt.plot(Time_stamps2, Amplitudes2)
plt.xlabel('Time-stamps')
plt.ylabel('Amplitudes')
plt.title('Wave 2')
plt.show()


snippet1 = [0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215,-2.22282]  # Wave snippet 1
snippet2 = [-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -0.00260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228, 0.0744249]  # Wave snippet 2


cross_corr = np.correlate(snippet1, snippet2)
percentage = (cross_corr.max() / (np.linalg.norm(snippet1) * np.linalg.norm(snippet2))) * 100


print("Cross-Correlation Percentage: {:.2f}%".format(percentage))
