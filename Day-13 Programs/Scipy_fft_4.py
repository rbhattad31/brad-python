from scipy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# Method-1[Discrete Fourier]
print("Method-1")
n = 1000
f = 1.0 / 800.0
x_axis = np.linspace(0.0, n*f, n)
y_axis = np.sin(70.0 * 2.0*np.pi*x_axis) + 0.5*np.sin(100.0 * 2.0*np.pi*x_axis)
x_fft = np.linspace(0.0, 1.0/(2.0*f), n//2)
y_fft = fft.fft(y_axis)
plt.plot(x_fft, 2.0 / n * np.abs(y_fft[:n // 2]))
plt.show(block=True)

# Method-2[Discrete Fourier]
print("Method-2")
my_freq = 6
freq_sample = 70
time_val = np.linspace(0, 3, 3 * freq_sample, endpoint=False)
amp_val = np.sin(my_freq * 3 * np.pi * time_val)
figure, axis = plt.subplots()
for i in range(2):
    if i is 0:
        axis.plot(time_val, amp_val)
        axis.set_xlabel('Time (in seconds)')
        axis.set_ylabel('Amplitude of signal')
        plt.show()
    elif i is 1:
        A = fftpack.fft(amp_val)
        frequency = fftpack.fftfreq(len(amp_val)) * freq_sample
        figure, axis = plt.subplots()
        axis.stem(frequency, np.abs(A))
        axis.set_xlabel('Frequency in Hz')
        axis.set_ylabel('Frequency Spectrum Magnitude')
        axis.set_xlim(-freq_sample / 2, freq_sample / 2)
        axis.set_ylim(-7, 125)
        plt.show()
