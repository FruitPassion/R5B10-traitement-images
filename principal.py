import numpy as np
from skimage import io, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt
from src.bruit_additif import bruit_additif
from src.bruit_multiplicatif import bruit_multiplicatif


image = io.imread('images_reference/image_reference1.png')
image = img_as_float(image)

mean = 0
std_dev = 10

# Créer une image bruitée avec du bruit multiplicatif
noisy_image = np.zeros_like(image)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        noisy_image[i, j] = bruit_additif(image[i, j], mean, std_dev)


noisy_image = np.clip(noisy_image, 0, 1)
noisy_image_uint8 = img_as_ubyte(noisy_image)

io.imsave('out/image_bruitee_multiplicatif.jpg', noisy_image_uint8)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title("Image Originale")
ax[0].axis('off')

ax[1].imshow(noisy_image, cmap='gray')
ax[1].set_title("Image avec Bruit Multiplicatif")
ax[1].axis('off')

plt.show()
