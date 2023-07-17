#This code accepts wavelet input as list of amplitudes and plots the phase angle for the same with respect to time.

import math
import matplotlib.pyplot as plt


def calculate_phase_angle(time_stamp, amplitude):
    time_radians = (time_stamp / 24) * 2 * math.pi
    phase_angle = math.atan(amplitude)
    phase_angle_deg = math.degrees(phase_angle)
    return round(phase_angle_deg,2)

time_stamps = list(range(1530, 1570, 2))
amplitudes = [-0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835, 2.7966, 1.96388, 1.23775]
phase_angles = []

for i in range(len(time_stamps)):
    time_stamp = time_stamps[i]
    amplitude = amplitudes[i]
    phase_angle = calculate_phase_angle(time_stamp, amplitude)
    phase_angles.append(phase_angle)
    print(f"Phase angle at time stamp {time_stamp} millisecond: {phase_angle} degrees")
print(phase_angles)
plt.plot(time_stamps, phase_angles)
plt.xlabel('Time-stamps')
plt.ylabel('Phase_angles')
plt.show()
