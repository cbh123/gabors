import scipy as sp
from scipy import arange, sqrt, array, amax, ceil, io, fliplr, flipud
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

x = [None,100]

img = np.zeros([10,10])
img[3] = 1

print(img.shape)


fb = np.empty((10,10,1,4),dtype=np.float32)
#
# fb = []
#
for i in range(0,3):
    for k in range(0,9):

        fb[k][k][0][i] = img[k]

# fb = np.array(fb)
#
# fb = np.reshape(fb,[-1,28,28,1])
# print(fb.shape)
#
# plt.imshow(fb[:])
# plt.show()
