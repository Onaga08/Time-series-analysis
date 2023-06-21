import math
import matplotlib.pyplot as plt


def calculate_phase_angle(time_stamp, amplitude):
    time_radians = (time_stamp / 24) * 2 * math.pi
    phase_angle = math.atan(amplitude)
    phase_angle_deg = math.degrees(phase_angle)
    return round(phase_angle_deg,2)

time_stamps = [0, 2, 4, 6, 8]  
amplitudes = [10, 20, -20, -30, 30]  
phase_angles = []

for i in range(len(time_stamps)):
    time_stamp = time_stamps[i]
    amplitude = amplitudes[i]
    phase_angle = calculate_phase_angle(time_stamp, amplitude)
    phase_angles.append(phase_angle)
   # print(f"Phase angle at time stamp {time_stamp} millisecond: {phase_angle} degrees")
print(phase_angles)
plt.plot(time_stamps, phase_angles, 'o')
plt.xlabel('Time-stamps')
plt.ylabel('Phase_angles')
plt.show()