import matplotlib.pyplot as plt
import numpy as np
from pyres.funcs.apodImRect import apodImRect
from pyres.funcs.getDcorr import getDcorr
#from funcs.getDcorrSect import getDcorrSect
from pyres.funcs.loadData import load_data
#from funcs.getLocalDcorr import getLocalDcorr
from pyres.funcs.resolution import calculate_resolution

# # Load the image
# def loadData(image_path):
#     return imageio.imread(image_path)

image = load_data('img_gt_0.tif').astype(np.float64)
print(f"Image shape is : {image.shape}")
pps = 5  # projected pixel size of 15nm
pixel_size = 0.0323  # in microns
# typical parameters for resolution estimate
Nr = 50
Ng = 10
r = np.linspace(0, 1, Nr)
GPU = False  # Using Python's boolean type here

# Apodize image edges with a cosine function over 20 pixels
image,mask = apodImRect(image, 20)
print(f"Apodized image shape is : {image.shape}")
plt.imshow(image, cmap='gray')  # You can adjust the colormap as needed
plt.title('Apodized image')
plt.colorbar()
plt.show()

# Compute resolution
figID = 100
if GPU:
    pass
else:
    kcMax, A0, d0, d= getDcorr(image, r, Ng, figID)
#print(f'kcMax : {kcMax:.3f}, A0 : {A0:.3f}, d0 : {d0:.3f}, d : {d:.3f}')

print(f'kcMax : {kcMax:.3f}, A0 : {A0:.3f}')
resolution = calculate_resolution(kcMax, pixel_size)
# # sectorial resolution
# Na = 8  # number of sectors
# figID = 101
# if GPU:
#     # Implement GPU functionality if required
#     pass
# else:
#     kcMax, A0 = getDcorrSect(image, r, Ng, Na, figID)

# # Local resolution map
# tileSize = 200  # in pixels
# tileOverlap = 0  # in pixels
# figID = 103
# if GPU:
#     # Implement GPU functionality if required
#     pass
# else:
#     kcMap, A0Map = getLocalDcorr(image, tileSize, tileOverlap, r, Ng, figID)
