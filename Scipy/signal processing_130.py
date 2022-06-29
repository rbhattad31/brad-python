from numpy import *
from scipy import signal, misc
import matplotlib.pyplot as plt

# Spline Edge Filter
image = misc.lena().astype(float32)
der_filter = array([1.0, -2, 1.0], float32)
ck = signal.cspline2d(image, 8.0)
der_iv = signal.sepfir2d(ck, der_filter, [1]) + signal.sepfir2d(ck, [1], der_filter)
plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()

plt.figure()
plt.imshow(der_iv)
plt.gray()
plt.title('spline edge filter')
plt.show()

# FIR Filter
b1 = signal.firwin(40, 0.5)
b2 = signal.firwin(41, [0.3, 0.8])
w1, h1 = signal.freqz(b1)
w2, h2 = signal.freqz(b2)
plt.title('Digital filter frequency response')
plt.plot(w1, 20*np.log10(np.abs(h1)), 'b')
plt.plot(w2, 20*np.log10(np.abs(h2)), 'r')
plt.ylabel('Amplitude Response (dB)')
plt.xlabel('Frequency (rad/sample)')
plt.grid()
plt.show()

# IIR Filter
b, a = signal.iirfilter(4, Wn=0.2, rp=5, rs=60, btype='lowpass', ftype='ellip')
w, h = signal.freqz(b, a)
plt.title('Digital filter frequency response')
plt.plot(w, 20*np.log10(np.abs(h)))
plt.title('Digital filter frequency response')
plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Frequency (rad/sample)')
plt.grid()
plt.show()