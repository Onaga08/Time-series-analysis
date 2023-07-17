import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

def execute(file1):
    #File open for trace
    file_path1 = file1
    
    if not os.path.exists(file_path1):
        print(f"File '{file_path1}' does not exist.")
    else:
        with open(file_path1, "r") as file1:
            lines1 = file1.readlines()
            num_lines1 = len(lines1)
            
            t_actual = []

            for line1 in lines1:
                columns1 = line1.strip().split()
                if len(columns1) >= 2:
                    t_actual.append(float(columns1[1]))  

        t_actual = np.array(t_actual)
        return t_actual
def execute1(file2):
    #File open for Comp_wavelet
    file_path2 = file2
    if not os.path.exists(file_path2):
        print(f"File '{file_path2}' does not exist.")
    else:
        with open(file_path2, "r") as file2:
            lines2 = file2.readlines()
            num_lines2 = len(lines2)
            t1 = []
            
            for line2 in lines2:
                columns2 = line2.strip().split()
                if len(columns2) >= 2:
                    t1.append(float(columns2[1]))  
        t1 = np.array(t1)
        return t1
    
#Function which calculates corr & phase angle
def calculate_cross_correlation(t1, t_actual):
    cross_correlation_percentages = []
    phase_differences=[]
    t1_length = len(t1)
    t_actual_length = len(t_actual)
    part_length = 20
    length = []
    length_value = []

    for i in range(0, t_actual_length, part_length):
        t1_part = t_actual[i:i+part_length]
        t_actual_part = t_actual[i:i+part_length]
        t1_part = np.array(t1_part)
        phase = np.angle(t1_part)
        new_phase = phase + np.pi/2
        rotated_wave = np.abs(t1_part) * np.exp(1j * new_phase)
        t1_part = np.real(rotated_wave)

        j = 1400 + 2*i
        length.append(j)
        length_value.append(t_actual[i])
        
      #Normalisation is not required in this data  
        #t1_norm = (t1_part - np.mean(t1_part)) / np.std(t1_part)
        #t_actual_norm = (t_actual_part - np.mean(t_actual_part)) / np.std(t_actual_part)
      #autocorrelation
        #t1_auto = np.corrcoef(t1_part,rowvar=True)
        #t_actual_auto = np.corrcoef(t_actual_part,rowvar=True)
        
      #Corr
        cross_correlation = np.correlate(t1_part, t_actual_part, "full")
        max_cross_correlation = np.max(cross_correlation)
        
        peak_index = np.argmax(cross_correlation)
    
    #Convert peak position to time lag
        lag = peak_index - len(t1_part) + 1
        sampling_rate = 20  
    
    #Convert lag to phase difference
        frequency = 1 / sampling_rate
        phase_difference = 360 * frequency * lag
        condition_met = False
        #if(phase_difference != 90 or phase_difference != -90 and not condition_met):
         #  condition_met = True
          # part_length = 40
           #continue
        
    #%age
        cross_correlation_percentage = (max_cross_correlation / (np.linalg.norm(t1_part) * np.linalg.norm(t_actual_part))) * 100
        cross_correlation_percentages.append(cross_correlation_percentage)
        phase_differences.append(phase_difference)

    return cross_correlation_percentages,phase_differences, length, length_value

#t1 = np.array([-0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835, 2.7966, 1.96388, 1.23775])
#t1 = np.array([0.865257, 2.09646, 3.55949, 5.0869, 6.39701, 7.34355, 7.71642, 7.22113, 5.87831, 3.78083, 1.15362, -1.68, -4.35489, -6.53074, -7.95374, -8.48222, -8.08787, -7.15307, -5.63978, -3.91215])
#t1 = np.array([-0.0413589, -0.0744249, -0.108228, -0.161074, -0.224722, -0.291076, -0.334128, -0.333282, -0.271283, -0.153474, -0.00260863, 0.153474, 0.271283, 0.333282, 0.334128, 0.291076, 0.224722, 0.161074, 0.108228,0.0744249])

#cross_correlation_percentages,phase_differences,length,length_value = calculate_cross_correlation(t1, t_actual)
    
   # for i, percentage in enumerate(cross_correlation_percentages):
       # print(f"Cross-correlation percentage for part {i+1}: {percentage}")
   # for i, phase in enumerate(phase_differences):
       # print(f"Phase for part {i+1}: {phase}")
    
#print(length)
#print(length_value)
#print(phase_differences)
#plotting

def plot(length, length_value, phase_difference):
    filename = 'data.txt'
    delimiter = ' , '
    new_list = [num for num in range(length[0], length[-1]+1, 2)]
    patterns = [[var]*20 for var in phase_difference]
    phase_list = [item for pattern in patterns for item in pattern]
    
    with open(filename, 'w') as file:
        for item1, item2, item3 in zip(new_list, length_value, phase_list):
            line = f"{item1}{delimiter}{item2}{delimiter}{item3}\n"
            file.write(line)
        
    data = np.loadtxt(filename, delimiter=',')

    time = data[:, 0]
    amplitude = data[:, 1]
    phase = data[:, 2]
    
    #phase = [-x for x in phase]
    

    scaling_factor = 5 #scaling factor changed as needed
    amplitude_scaled = amplitude.copy()
    amplitude_scaled[phase == -90] *= scaling_factor
    amplitude_scaled[phase == 90] *= scaling_factor
    amplitude_scaled[phase == 90] *= scaling_factor
    #amplitude_scaled[phase == 0] *= scaling_factor
    #amplitude_scaled[phase == 180] *= scaling_factor
    #amplitude_scaled[phase == -180] *= scaling_factor

    fig, ax = plt.subplots(figsize=(10, 6))

    time = time[::-1]
    phase = phase[::-1]
    amplitude_scaled = amplitude_scaled[::-1]

    line_offsets = np.arange(len(time))

    plt.fill_betweenx(line_offsets, phase - amplitude_scaled, phase + amplitude_scaled,
                      where=(amplitude_scaled > 0), facecolor='red', interpolate=True, alpha=0.5)
    plt.fill_betweenx(line_offsets, phase - amplitude_scaled, phase + amplitude_scaled,
                      where=(amplitude_scaled < 0), facecolor='blue', interpolate=True, alpha=0.5)

    cmap = plt.cm.bwr
    norm = plt.Normalize(vmin=np.min(amplitude_scaled), vmax=np.max(amplitude_scaled))
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    cbar = plt.colorbar(sm, ax=ax, label='Amplitude')
    cbar.ax.invert_yaxis()

    plt.xlabel('Phase (Degrees)')
    plt.ylabel('Time (ms)')
    plt.title('Variable Density Wiggle Plot')

    tick_interval = max(1, int(len(time) / 2))
    ax.set_yticks(np.arange(0, len(time), tick_interval))
    ax.set_yticklabels(time[::tick_interval])
    ax.set_xticks(np.arange(-180, 181, 60))
    ax.set_xticklabels(np.arange(-180, 181, 60))
    plt.axvline(x=2, color='red', linestyle='dotted')

    # Show the plot
    plt.show()