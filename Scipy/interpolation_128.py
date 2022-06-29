# Import the required Python libraries
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

# Initialize input values x and y
x = np.arange(0, 10)
y = x**2

# Interpolation
temp = interpolate.interp1d(x, y)
xnew = np.arange(0, 9, 0.2)
ynew = temp(xnew)

plt.title("1-D Interpolation")
plt.plot(x, y, '*', xnew, ynew, '-', color="green")
plt.show()
