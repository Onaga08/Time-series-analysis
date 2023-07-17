import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

#This is code which generates the wiggle plot. If you have three columns, un-comment the necessary lines.
# Load the data from the text file
data = np.loadtxt('data.txt',delimiter=',')

# Extract the columns for time, amplitude, and phase
time = data[:, 0]
amplitude = data[:, 1]
#phase = data[:, 2]


scaling_factor = 10  # Adjust the scaling factor as needed

# Scale up the amplitude for -90 phase
amplitude_scaled = amplitude.copy()
#amplitude_scaled[phase == -90] *= scaling_factor
#amplitude_scaled[phase == 90] *= scaling_factor
#amplitude_scaled[phase == 0] *= scaling_factor
#amplitude_scaled[phase == 180] *= scaling_factor
#amplitude_scaled[phase == -180] *= scaling_factor

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Reverse the time axis
time = time[::-1]
#phase = phase[::-1]
amplitude_scaled = amplitude_scaled[::-1]

# Calculate the line offsets for variable density wiggle plot
line_offsets = np.arange(len(time))

# Plot the variable density wiggle
plt.fill_betweenx(line_offsets, amplitude_scaled,
                  where=(amplitude_scaled > 0), facecolor='red', interpolate=True, alpha=0.5)
plt.fill_betweenx(line_offsets,amplitude_scaled,
                  where=(amplitude_scaled < 0), facecolor='blue', interpolate=True, alpha=0.5)

# Create a ScalarMappable for the colorbar
cmap = plt.cm.bwr
norm = plt.Normalize(vmin=np.min(amplitude_scaled), vmax=np.max(amplitude_scaled))
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # Set an empty array to the ScalarMappable

# Add colorbar
cbar = plt.colorbar(sm, ax=ax, label='Amplitude')
cbar.ax.invert_yaxis()

plt.xlabel('Phase (Degrees)')
plt.ylabel('Time (ms)')
plt.title('Variable Density Wiggle Plot')

# Set the correct time axis ticks and labels
tick_interval = max(1, int(len(time) /2))  # Adjust the tick interval as needed
ax.set_yticks(np.arange(0, len(time), tick_interval))
ax.set_yticklabels(time[::tick_interval])
ax.set_xticks(np.arange(-180, 181, 60))  # Set the phase ticks from -180 to 180 degrees with a step of 60 degrees
ax.set_xticklabels(np.arange(-180, 181, 60))  # Set the phase tick labels from -180 to 180 degrees with a step of 60 degrees

#Show the plot
plt.show()