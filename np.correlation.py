#This code snippet finds correlation %age between two time-series graphs taken as list of amplitudes with equal 
#signal length. The correlation technique used here is np.correlate from the numpy module in python.

import numpy as np
import math



Amplitude1 = [-0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835, 2.7966, 1.96388, 1.23775]
Amplitude_comp2 = [-0.013995, -0.0186956, -0.0275364, -0.0311656, -0.0149192, 0.0346624, 0.12169, 0.23547, 0.351297, 0.438163, 0.470425, 0.438163, 0.351297, 0.23547, 0.12169, 0.0346624, -0.0149192, -0.0311656, -0.0275364, -0.0186956]

cross_corr1 = np.correlate(Amplitude1, Amplitude_comp2, mode= 'full')
percentage1 = (cross_corr1.max() / (np.linalg.norm(Amplitude1) * np.linalg.norm(Amplitude_comp2))) * 100

print(f"Correlation Percentage: {percentage1}%")
