# FFT Vibration Analysis

# Overview 
This project demonstrates the use of Fast Fourier Tranform(FFT) for identifying dominant frequencies in machine vibration data.

# Tools Used
1. Python
2. Numpy
3. Matplotlib

# Method
1. Generate a vibration signal containing 20 Hz and 60 Hz freqency components.
2. Apply FFT using Numpy.
3. Plot the vibration signal and FFT spectrum.
4. Identify the dominant vibration frequencies and their peak values.

# Results
The FFT spectrum successfully identified peaks at 20 Hz and 60 Hz. The 60 Hz component exhibited the highest magnitude by having the highest peak in the FFT spectrum plot, indicating that it is the dominant source of vibration in the generated signal.

# Future Improvements
1. Add noise to the signal
2. Automatic peak detection
3. Real sensor data analysis
4. Machine health monitoring applications using the vibration signals and finding out that dominant frequency
