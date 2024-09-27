import time

import matplotlib.pyplot as plt
import numpy as np
from skimage import img_as_float, img_as_ubyte, io


def load_image(path: str) -> np.ndarray:
    """Load an image from a file path and convert it to floating point."""
    image = io.imread(path)
    return img_as_float(image)


def save_image(image: np.ndarray, arg: str) -> None:
    """Sauvegarde l'image bruitée dans un fichier."""
    timestamp = int(time.time())
    filename = f"out/image_bruitee_{arg}_{timestamp}.png"
    io.imsave(filename, img_as_ubyte(image))
    print(f"Image sauvegardée dans {filename}")


def display_images(original: np.ndarray, noisy: np.ndarray, noise_type: str) -> None:
    """Affiche les images originale et bruitée."""
    _, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(original, cmap="gray")
    ax[0].set_title("Image Originale")
    ax[0].axis("off")

    ax[1].imshow(noisy, cmap="gray")
    ax[1].set_title(f"Image avec bruit {noise_type}")
    ax[1].axis("off")

    plt.show()
