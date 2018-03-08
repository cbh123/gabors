import scipy.io
import matplotlib.pyplot as plt
import png

mat = scipy.io.loadmat('/Users/charlieholtz/Desktop/hermann/Rosemary_Work/HermannHMAX_2/Functions_Data/OriginalImagesCG.mat');


image_files = (mat['OriginalImagesCG'])

images = image_files[0]

count = 1

for i in images:
	png.from_array(i,'L').save('pngs/parsed_' + str(count) +  '.png')
	count = count + 1
