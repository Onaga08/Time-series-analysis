import tkinter as tk
from tkinter import filedialog
import subprocess
import pprint
import numpy as np
from Functions import execute, calculate_cross_correlation, plot, execute1
#Functions are imported from Functions.py
#For slices with overlaps, import functions from Functions_overlap.py


def browse_file1():
    filename = filedialog.askopenfilename()
    file1_path.set(filename)

def browse_file2():
    filename = filedialog.askopenfilename()
    file2_path.set(filename)

def execute_code():
    file1 = file1_path.get()
    file2 = file2_path.get()
    t1 = execute1(file2)
    t_actual = execute(file1)
    cross_correlation_percentages, phase_differences, length, length_value = calculate_cross_correlation(t1, t_actual)
    plot(length, t_actual, phase_differences)
    return phase_differences
    
def print():
    cross = execute_code()
    cross = [-x for x in cross] #reversing the sign of phase angle
    cross = np.round(cross, decimals=2)
    pretty_result = pprint.pformat(cross)  
    label.config(text=f"The phase differences are:{cross}")
         
window = tk.Tk()
window.title("Phase-filtering")
window.configure(background='#00008B')  

file1_label = tk.Label(window, text="Trace:", fg='black')  
file1_label.grid(row=0, column=0, padx=10, pady=10)

file1_path = tk.StringVar()
file1_entry = tk.Entry(window, textvariable=file1_path)
file1_entry.grid(row=0, column=1, padx=10)

file1_button = tk.Button(window, text="Browse", command=browse_file1)
file1_button.grid(row=0, column=2, padx=10)

file2_label = tk.Label(window, text="Comparison Wavelet:", fg='black') 
file2_label.grid(row=1, column=0, padx=10, pady=10)

file2_path = tk.StringVar()
file2_entry = tk.Entry(window, textvariable=file2_path)
file2_entry.grid(row=1, column=1, padx=10)

file2_button = tk.Button(window, text="Browse", command=browse_file2)
file2_button.grid(row=1, column=2, padx=10)

execute_button = tk.Button(window, text="Execute Code", command=execute_code)
execute_button.grid(row=2, column=0, pady=10)

#output_text = tk.Text(window, state=tk.NORMAL)
#output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

label = tk.Label(window, text="OUTPUT WILL BE SHOWN HERE", height=20, width=100)
label.grid(row = 3, column=1)

button = tk.Button(window, text="Print", command=print)
button.grid(row = 4, column = 1)
    
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.grid(row=2, column=2, pady= 20, padx=10)
window.mainloop()