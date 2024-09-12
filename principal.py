import numpy as np
from skimage import io, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt
from src.bruit_additif import bruit_additif
from src.bruit_multiplicatif import bruit_multiplicatif
from src.saltPepperGrain import pepperSaltGrainEachPixel
from time import time
import sys

arg = sys.argv[1]
if arg not in ['additif', 'multiplicatif', 'poivre_et_sel']:
    print("Argument invalide")
    sys.exit()
print(arg)

image = io.imread('images_reference/image_reference1.png')
image = img_as_float(image)

mean = None
std_dev = None
if arg == 'additif':
    mean = 0
    std_dev = 10
elif arg == 'mutiplicatif':
    mean = 1
    std_dev = 0.1

noisy_image = np.zeros_like(image)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if arg == 'poivre_et_sel':
            noisy_image[i, j] = pepperSaltGrainEachPixel(image[i, j])
        elif arg == 'additif':
            noisy_image[i, j] = bruit_additif(image[i, j], mean, std_dev)
        elif arg == 'multiplicatif':
            noisy_image[i, j] = bruit_multiplicatif(image[i, j], mean, std_dev)

noisy_image = np.clip(noisy_image, 0, 1)
noisy_image_uint8 = img_as_ubyte(noisy_image)

name = f"out/image_bruitee_multiplicatif_{time()}.png"
io.imsave(name, noisy_image_uint8)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title("Image Originale")
ax[0].axis('off')

ax[1].imshow(noisy_image, cmap='gray')
ax[1].set_title(f"Image avec bruit {arg}")
ax[1].axis('off')

plt.show()
