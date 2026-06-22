# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Create a time vector
t = np.linspace(0, 1, 1000)

# Generate a vibration signal
signal = np.sin(2 * np.pi * 20 * t) + 3*np.sin(2 * np.pi * 60 * t)

# Plotting the vibration signal using matplotlib
plt.figure(figsize = (10, 4))
plt.plot(t, signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Raw Vibration Signal")

plt.grid()
plt.savefig("raw_signal.png")
plt.show()


# Using fft to generate the dominant frequencies from the vibration signal
fft_result = np.fft.fft(signal)
freq = np.fft.fftfreq(len(t), t[1] - t[0])
magnitude = np.abs(fft_result)

# Plotting the required fft curve
plt.figure(figsize = (10, 4))
plt.plot(freq[:500], magnitude[:500])
plt.xlim(0, 100)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Spectrum")

plt.grid()
plt.savefig("fft_spectrum.png")
plt.show()



