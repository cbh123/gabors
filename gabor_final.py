import scipy as sp
from scipy import arange, sqrt, array, amax, ceil, io, fliplr, flipud
import numpy as np
import matplotlib.pyplot as plt



# rot = np.array([0, 90])
# # RF_siz = np.array([11,13])
#
# # the_range = arange(33,65,2)
# # RF_siz = np.array([the_range])
# RF_siz = np.array([33,35])
# div2 =arange(4, 3.2, -0.05)
# Div = div2[2],div2[3]
# # general_rot = np.array([90,-67.5,-45, -22.5,0,22.5,45, 67.5])

rot = np.array([90])
RF_siz = sp.arange(7,40,2)
Div = sp.arange(4,3.15,-.05)

def create_gabor(rot,RF_siz,Div):
    count = 0
    numFilterSizes   = len(RF_siz)
    numSimpleFilters = len(rot)
    lamb = (RF_siz * 2)/Div
    sigma  = lamb * 0.8
    G      = 0.3
    phases = [0, np.pi/2]

    # Initialize Filerbank

    #fb = []

    fb = np.empty((2*numSimpleFilters,numFilterSizes),dtype=object)
    #x = np.zeros([2*numSimpleFilters, numFilterSizes])
    #fb = np.array([x])
    #print(fb)
    for k in range(0,numFilterSizes):
        for r in range(0,numSimpleFilters):


            #f = np.zeros([RF_siz[k],RF_siz[k]])
            f = np.zeros([RF_siz[numFilterSizes-1],RF_siz[numFilterSizes-1]])


            ## Parameters
            theta     = rot[r]*(np.pi/180)
            filtSize  = RF_siz[k]


            img_center = ceil(21.0) ## New center for padding with zeros

            center    = ceil(filtSize/2)+1 ## Old and possibly more accurate center

            print(center)
            filtSizeL = center-1
            filtSizeR = filtSize-filtSizeL-1
            sigmaq    = (sigma[k]) * (sigma[k])

            #print(center)

            # Compute filter values

            for iPhi in range(0,2):
                for i in range( int((-1 * filtSizeL)),int(filtSizeR+1)):
                    for j in range( int((-1 * filtSizeL)),int(filtSizeR+1)):

                        if (sqrt((i**2)+(j**2))>(filtSize/2 )) :
                            E = 0
                        else :
                            x = i*np.cos(theta) - j*np.sin(theta)
                            y = i*np.sin(theta) + j*np.cos(theta)

                            E = np.exp((-1*((x**2)+ (G**2) * (y**2)))/(2*sigmaq))*np.cos(2*np.pi*x/lamb[k] + phases[iPhi])


                        f[int(j+img_center-1),int(i+img_center-1)] = E

                ## Append to fb (filterbank)
                f = f - np.mean(np.mean(f))
                f = f / sqrt(np.sum(np.sum(f**2)))


                plt.imshow(f,cmap='Greys')
                #plt.savefig('images/gabor' + str(count) + '.png')
                 ## Plotting
                #plt.imshow(f,cmap='Greys')
                plt.show()

                count += 1

                (fb[2*r - iPhi+1][k]) = (f)
                #fb.append(f)



    return (np.array(fb))




## Test Plotting
#create_gabor(rot,RF_siz,Div)

#For creating dictionary
gabor_array = create_gabor(rot,RF_siz,Div)

weights = np.zeros([34])
gabor_dictionary = {}
gabor_dictionary['gabors'] = gabor_array,weights
f,x = gabor_dictionary['gabors']
print(len(f))

np.save('gabor_dictionary.npy', gabor_dictionary)

b = np.load('/Users/charlieholtz/Desktop/hermann/Gabor Filters/gabor_dictionary.npy').item()
f,x = b['gabors']

print(f.shape)





## Tensorflow shit - not needed
# print(create_gabor(rot,RF_siz,Div).shape)

# init = tf.constant(create_gabor(rot,RF_siz,Div))
# tf.get_variable('gabors', initializer=init)
