import math
import matplotlib.pyplot as plt

# Input for graph 1
graph1 = [0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215]

# Input for graph 2
graph2 = [-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -0.00260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228, 0.0744249]

# Calculate cross-correlation
cross_corr = [sum(graph1[j] * graph2[j-i] for j in range(min(len(graph1), len(graph2)) - i)) for i in range(abs(len(graph1) - len(graph2)) + 1)]

# Find index of maximum cross-correlation
max_index = cross_corr.index(max(cross_corr, key=abs))

# Calculate phase lag in radians
phase_lag_rad = max_index * (2 * math.pi / len(graph1))

# Convert phase lag to degrees
phase_lag_deg = math.degrees(phase_lag_rad)

print("Phase Lag (radians):", phase_lag_rad)
print("Phase Lag (degrees):", phase_lag_deg)

# Plot the cross-correlation
shifts = range(len(graph1) - len(graph2) + 1, len(graph1) - len(graph2) + len(cross_corr) + 1)
plt.plot(shifts, cross_corr)
plt.xlabel('Shifts')
plt.ylabel('Cross-correlation')
plt.title('Cross-correlation between Graph 1 and Graph 2')
plt.grid(True)
plt.show()
