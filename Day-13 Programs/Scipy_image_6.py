from scipy import misc, ndimage
import imageio
import matplotlib.pyplot as plt
import numpy as np

# Saving image using scipy
face = misc.face()
imageio.imsave('Animal.png', face)
plt.imshow(face)
plt.show()

# Image to Array
print(face.shape)
print(face.dtype)
plt.imshow(face)
plt.show()

# Read raw file with encoding
img_1 = np.fromfile('Animal.raw', dtype=np.uint8)
print(img_1.shape)

# Get min max mean
print(face.max())
print(face.min())
print(face.mean())

# Crop image
x, y = face.shape
crop = face[x // 5: - x // 6, y // 3: - y // 8]
plt.imshow(crop)
plt.show()

# Rotate image
rotate = ndimage.rotate(face, 90)
plt.imshow(rotate)
plt.show()

# Sharpening image
# Blur image
img = misc.face(gray=True).astype(float)
blur = ndimage.gaussian_filter(img, 5)
plt.imshow(blur)
plt.show()
# Sharp image
blur_G = ndimage.gaussian_filter(blur, 1)
alpha = 30
sharp = blur + alpha * (blur - blur_G)
plt.imshow(sharp)
plt.show()

# Edge Detection
img = np.zeros((300, 300))
img[64:-64, 64:-64] = 1
img = ndimage.rotate(img, 30, mode='constant')
img = ndimage.gaussian_filter(img, 7)
plt.imshow(img)
plt.show()
x = ndimage.sobel(img, axis=0, mode='constant')
y = ndimage.sobel(img, axis=1, mode='constant')
border = np.hypot(x, y)
plt.imshow(border)
plt.show()
