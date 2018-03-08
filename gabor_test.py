import numpy as np

b = np.load('/Users/charlieholtz/Desktop/hermann/Gabor Filters/gabor_dictionary.npy').item()
f,x = b['gabors']
print(len(f))
