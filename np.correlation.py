#This code snippet finds correlation %age between two time-series graphs taken as list of amplitudes with equal 
#signal length. The correlation technique used here is np.correlate from the numpy module in python.

import numpy as np
import math



Amplitude1 = np.array([-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -0.00260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228,0.0744249])
Amplitude_comp2 = np.array([0.0426437, -0.0684449, -0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835,2.7966,1.96388])
cross_corr1 = np.correlate(Amplitude1, Amplitude_comp2, mode= "full")
percentage1 = (cross_corr1.max() / (np.linalg.norm(Amplitude1) * np.linalg.norm(Amplitude_comp2))) * 100

print(f"Correlation Percentage: {percentage1}%")
