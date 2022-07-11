# 1-D Interpolation
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

# Initialize input values x and y
x = np.arange(0, 10)
y = x ** 2

# Interpolation
temp = interpolate.interp1d(x, y)
x1 = np.arange(0, 9, 0.2)
y1 = temp(x1)

plt.title("1-D Interpolation")
plt.plot(x, y, '*', x1, y1, '-', color="green")
plt.show()

# Spline Interpolation
# Initialize the input values
x2 = np.arange(0, 10)
y2 = np.cos(x ** 3)

# Interpolation
# To find the spline representation of a
# curve in a 2-D plane using the function

temp = interpolate.splrep(x, y, s=0)
x3 = np.arange(0, np.pi ** 2, np.pi / 100)
y3 = interpolate.splev(x3, temp, der=0)

plt.figure()

plt.plot(x2, y2, '*', x3, y3, x3, np.cos(x3), x2, y2,  color="green")

plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-0.1, 6.5, -1.1, 1.1])
plt.title('Cubic-spline Interpolation in Python')
plt.show()

# Univariate Spline
x4 = np.linspace(-3, 3, 50)
y4 = np.exp(-x4 ** 2) + 0.1 * np.random.randn(50)
plt.title("Univariate Spline")
plt.plot(x4, y4, 'g.', ms=8)

# Using the default values for the
# smoothing parameter
spl = UnivariateSpline(x4, y4)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'green', lw=3)

# Manually change the amount of smoothing
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), color='black', lw=3)
plt.show()
