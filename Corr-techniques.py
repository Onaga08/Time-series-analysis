#This code takes two np.array inputs of signal amplitudes and returns the cross-correlation between them using
#three different methods. A 100% correlation suggests identical time-series graphs. A negative Correlation 
#points towards similarity between the wavelets, but with a different phase angle between them.

import numpy as np
from scipy.signal import correlate

def calculate_correlation_percentage(signal1, signal3):
    # Method 1: Using numpy.correlate
    correlation_np = np.correlate(signal1, signal3, mode='valid')
    print(correlation_np)
    correlation_percentage_np = (correlation_np.max() / np.sqrt(np.sum(np.square(signal1)) * np.sum(np.square(signal2)))) * 100

    # Method 2: Using scipy.signal.correlate
    correlation_scipy = correlate(signal1, signal3, mode='full')
    print(correlation_scipy)
    correlation_percentage_scipy = (correlation_scipy.max() / np.sqrt(np.sum(np.square(signal1)) * np.sum(np.square(signal2)))) * 100

    # Method 3: Manual cross-correlation calculation
    padded_signal1 = np.pad(signal1, (0, len(signal1) - 1))
    padded_signal2 = np.pad(signal3[::-1], (0, len(signal3) - 1))
    correlation_manual = np.zeros(len(signal1) + len(signal3) - 1)
    for i in range(len(correlation_manual)):
        correlation_manual[i] = np.sum(padded_signal1 * padded_signal2)
        padded_signal2 = np.roll(padded_signal2, 1)
    correlation_percentage_manual = (correlation_manual.max() / np.sqrt(np.sum(np.square(signal1)) * np.sum(np.square(signal3)))) * 100

    return correlation_percentage_np, correlation_percentage_scipy, correlation_percentage_manual

signal1 = np.array([-0.393105, -0.822565, -1.32783, -1.84869, -2.30533, -2.52846, -2.40997, -1.97941, -1.24355, -0.517542, 0.0990675, 1.13414, 2.17622, 3.01957, 3.55358, 3.72256, 3.47835, 2.7966, 1.96388, 1.23775])
signal2 = np.array([-0.013995, -0.0186956, -0.0275364, -0.0311656, -0.0149192, 0.0346624, 0.12169, 0.23547, 0.351297, 0.438163, 0.470425, 0.438163, 0.351297, 0.23547, 0.12169, 0.0346624, -0.0149192, -0.0311656, -0.0275364, -0.0186956])
signal3 = np.array([-0.013995, -0.0186956, -0.0275364, -0.0311656, -0.0149192, 0.0346624, 0.12169, 0.23547, 0.351297, 0.438163, 0.470425, 0.438163, 0.351297, 0.23547, 0.12169, 0.0346624, -0.0149192, -0.0311656, -0.0275364, -0.0186956])
correlation_percentage_np, correlation_percentage_scipy, correlation_percentage_manual = calculate_correlation_percentage(signal1, signal3)

print("Correlation Percentage using numpy.correlate:", correlation_percentage_np)
print("Correlation Percentage using scipy.signal.correlate:", correlation_percentage_scipy)
print("Correlation Percentage using manual calculation:", correlation_percentage_manual)
