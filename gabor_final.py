import scipy as sp
from scipy import arange, sqrt, array, amax, ceil, io, fliplr, flipud
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import ipdb
import time
from tqdm import tqdm

"""
The following code creates a series of 
'gabor' filters at specified sizes. Gabor filters
are used as a proxy for simple V1 cell receptive 
fields (https://en.wikipedia.org/wiki/Gabor_filter). 
This code was adapted from David Mely, Serre Lab by 
Charlie Holtz '18 and used in his thesis.
"""


# initialize degrees of rotation (mely et. al)
rot = np.array([90,-67.5,-45,-22.5,0,22.5,45,67.5])

# initialize receptive field size 
RF_siz = sp.arange(33,67,2)
Div = sp.arange(4,3.15,-.05)

def create_gabor(rot,RF_siz,Div,plot,num=10):
    """
    this function creates a series of gabor filters
    
    @param rot: number rotations
    @param RF_siz: receptive field size
    @param Div: receptive field degree
    @param num: interval of pixel size to plot
    """
    count = 0
    numFilterSizes   = len(RF_siz)
    numSimpleFilters = len(rot)
    lamb = (RF_siz * 2.)/Div
    sigma  = lamb * 0.8
    G      = 0.3
    phases = [0, np.pi/2]

    # initialize filterbank
    alt_fb = np.zeros((65,65,1,272),dtype=np.float32)

    # loop through number of filter sizes
    for k in tqdm(range(1,numFilterSizes+1)):
        for r in tqdm(range(1,numSimpleFilters+1)):

            f = np.zeros([RF_siz[numFilterSizes-1],RF_siz[numFilterSizes-1]])
            fx = np.zeros([RF_siz[numFilterSizes-1],RF_siz[numFilterSizes-1]])

            ## Parameters
            theta     = rot[r-1]*(np.pi/180)
            filtSize  = RF_siz[k-1]

            img_center = ceil(33.0) ## New center for padding with zeros

            center    = ceil(filtSize/2.0) ## Old and possibly more accurate center

            filtSizeL = center-1
            filtSizeR = filtSize-filtSizeL-1
            sigmaq    = (sigma[k-1]) * (sigma[k-1])


            # Compute filter values
            for iPhi in range(1,3):
                for i in range(int(-1 * filtSizeL),int(filtSizeR+1)):
                    for j in range(int(-1 * filtSizeL),int(filtSizeR+1)):

                        if (sqrt((i**2)+(j**2))>(filtSize/2 )) :
                            E = 0
                        else :
                            x = i*np.cos(theta) - j*np.sin(theta)
                            y = i*np.sin(theta) + j*np.cos(theta)

                            E = np.exp((-1*((x**2)+ (G**2) * (y**2)))/(2*sigmaq))*np.cos(2*np.pi*x/lamb[k-1] + phases[iPhi-1])

                        f[int(j+img_center-1),int(i+img_center-1)] = E


                ## Append to fb (filterbank)
                f = f - np.mean(np.mean(f))
                f = f / sqrt(np.sum(np.sum(f**2)))

                # Reshaped image
                alt_fb[:,:,0,count] = f
                count += 1

                if (plot):
                    if count % num == 0:
                        plt.imshow(f,cmap='Greys')
                        plt.show()

    return (np.array(alt_fb))






## Create Dictionary ---------------
gabor_array = create_gabor(rot,RF_siz,Div,False)
bias = np.zeros([272])
gabor_dictionary = {}
gabor_dictionary['gabors'] = gabor_array,bias

f,x = gabor_dictionary['gabors']


## Save Dictionary ----------------------
np.save('/Users/charlieholtz/Desktop/gabors/gabor_dictionary.npy', gabor_dictionary)
