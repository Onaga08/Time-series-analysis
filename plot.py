import matplotlib.pyplot as plt
import numpy as np


Time_stamps1 = list(range(0, 41, 2))
Amplitudes1 = [0, 0, 0, 0, 0.0301017, 0.0358239, 0.0377665, 0.0357909, 0.0167538, -0.0272439, -0.109748, -0.229813, -0.384661, -0.556583, -0.695369, -0.785221, -0.815269, -0.829323, -0.687622, -0.366953, 0.12407]
plt.subplot(1, 2, 1)
plt.plot(Time_stamps1, Amplitudes1)
plt.xlabel('Time-stamps')
plt.ylabel('Amplitudes')
plt.title('Wave 1')

Time_stamps2 = list(range(42, 81, 2))
Amplitudes2 = [ 0.729113, 1.34556, 1.92608, 2.3567, 2.51551, 2.55658, 2.37535, 1.91666, 1.31234, 0.648053, 0.011749, -0.52202, -0.903566, -1.18526, -1.21687, -1.18767, -1.00122, -0.687064, -0.468549, -0.275822]
plt.subplot(1, 2, 2)
plt.plot(Time_stamps2, Amplitudes2)
plt.xlabel('Time-stamps')
plt.ylabel('Amplitudes')
plt.title('Wave 2')
plt.show()


snippet1 = [0, 0, 0, 0, 0.0301017, 0.0358239, 0.0377665, 0.0357909, 0.0167538, -0.0272439, -0.109748, -0.229813, -0.384661, -0.556583, -0.695369, -0.785221, -0.815269, -0.829323, -0.687622, -0.366953, 0.12407]  # Wave snippet 1
snippet2 = [0.729113, 1.34556, 1.92608, 2.3567, 2.51551, 2.55658, 2.37535, 1.91666, 1.31234, 0.648053, 0.011749, -0.52202, -0.903566, -1.18526, -1.21687, -1.18767, -1.00122, -0.687064, -0.468549, -0.275822]  # Wave snippet 2


cross_corr = np.correlate(snippet1, snippet2)
percentage = (cross_corr.max() / (np.linalg.norm(snippet1) * np.linalg.norm(snippet2))) * 100


print("Cross-Correlation Percentage: {:.2f}%".format(percentage))
