import numpy as np

Amplitudes1 = [-0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835, 2.7966, 1.96388, 1.23775,0.51741]
Amplitudes2 = [0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215,-2.22282]
Amplitudes_comp = [-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -0.00260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228, 0.0744249]

sample_rate = 2

maxima1_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes1))) < 0)[0] + 1
maxima2_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes_comp))) < 0)[0] + 1

minima1_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes1))) > 0)[0] + 1
minima2_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes_comp))) > 0)[0] + 1

phase_lag_crest_to_crest1 = (maxima2_indices1[0] - maxima1_indices1[0]) * sample_rate

phase_lag_trough_to_trough1 = (minima2_indices1[0] - minima1_indices1[0]) * sample_rate

print("Phase Lag (Crest to Crest)1-3:", phase_lag_crest_to_crest1, "seconds")
print("Phase Lag (Trough to Trough)1-3:", phase_lag_trough_to_trough1, "seconds")


maxima1_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes2))) < 0)[0] + 1
maxima2_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes_comp))) < 0)[0] + 1

minima1_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes2))) > 0)[0] + 1
minima2_indices1 = np.where(np.diff(np.sign(np.diff(Amplitudes_comp))) > 0)[0] + 1

phase_lag_crest_to_crest1 = (maxima2_indices1[0] - maxima1_indices1[0]) * sample_rate

phase_lag_trough_to_trough1 = (minima2_indices1[0] - minima1_indices1[0]) * sample_rate

print("Phase Lag (Crest to Crest)2-3:", phase_lag_crest_to_crest1, "seconds")
print("Phase Lag (Trough to Trough)2-3:", phase_lag_trough_to_trough1, "seconds")