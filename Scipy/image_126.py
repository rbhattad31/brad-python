import numpy as np
from scipy import misc
from matplotlib import pyplot as plt

# get face image of panda from misc package
panda = misc.face()
# plot or show image of face
plt.imshow( panda )
plt.show()

# Flip Down using scipy misc.face image
flip_down = np.flipud(misc.face())
plt.imshow(flip_down)
plt.show()

from scipy import ndimage, misc
from matplotlib import pyplot as plt
panda = misc.face()
# rotatation function of scipy for image – image rotated 135 degree
panda_rotate = ndimage.rotate(panda, 135)
plt.imshow(panda_rotate)
plt.show()