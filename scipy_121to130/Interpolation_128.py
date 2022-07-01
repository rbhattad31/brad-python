import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Initialize the input values
x = np.arange(0, 10)
y = np.cos(x ** 3)

# Interpolation
# To find the spline representation of a
# curve in a 2-D plane using the function
# spl rep
temp = interpolate.splrep(x, y, s=0)
xnew = np.arange(0, np.pi ** 2, np.pi / 100)
ynew = interpolate.splev(xnew, temp, der=0)

plt.figure()

plt.plot(x, y, '*', xnew, ynew, xnew, np.cos(xnew),
         x, y, 'b', color="green")

plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-0.1, 6.5, -1.1, 1.1])
plt.title('Cubic-spline Interpolation in Python')
plt.show()