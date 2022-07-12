#write a program to demonstrate Discrete Fourier Transform – scipy.fftpack functions with SciPy
import numpy as np
from scipy import fftpack

time_step = 0.05
time_vec = np.arange(0,10,time_step)
sig = (np.sin(2*np.pi*time_vec))
print(sig)