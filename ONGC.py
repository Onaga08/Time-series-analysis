import math

def calculate_phase_angle(time_stamp, amplitude):
    time_radians = (time_stamp / 24) * 2 * math.pi
    phase_angle = math.atan(amplitude)
    phase_angle_deg = math.degrees(phase_angle)

    return phase_angle_deg
time_stamps = [0, 2, 4, 6, 8]  
amplitudes = [10, 20, -20, -30, 30]  


for i in range(len(time_stamps)):
    time_stamp = time_stamps[i]
    amplitude = amplitudes[i]
    phase_angle = calculate_phase_angle(time_stamp, amplitude)
    print(f"Phase angle at time stamp {time_stamp} millisecond: {round(phase_angle,3)} degrees")
