from time import time

import matplotlib.pyplot as plt
import numpy as np
from simple_term_menu import TerminalMenu
from skimage import img_as_float, img_as_ubyte, io

from src.bruit_additif import bruit_additif
from src.bruit_multiplicatif import bruit_multiplicatif
from src.saltPepperGrain import pepperSaltGrainEachPixel


def get_noise_settings(arg):
    if arg == "a":
        mean = 0
        std_dev = 0.1
        return {"mean": mean, "std_dev": std_dev}
    elif arg == "m":
        mean = -0.7
        std_dev = 0.1
        return {"mean": mean, "std_dev": std_dev}
    elif arg == "p":
        rate = 10
        return {"rate": rate}


def generate_noisy_image(arg, titre):
    image = io.imread("images_reference/image_reference1.png")
    image = img_as_float(image)
    noisy_image = np.zeros_like(image)

    settings = get_noise_settings(arg)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if arg == "p":
                noisy_image[i, j] = pepperSaltGrainEachPixel(image[i, j], settings["rate"])
            elif arg == "a":
                noisy_image[i, j] = bruit_additif(image[i, j], settings["mean"], settings["std_dev"])
            elif arg == "m":
                noisy_image[i, j] = bruit_multiplicatif(image[i, j], settings["mean"], settings["std_dev"])
    noisy_image = np.clip(noisy_image, 0, 1)
    noisy_image_uint8 = img_as_ubyte(noisy_image)

    name = f"out/image_bruitee_{arg}_{time()}.png"
    io.imsave(name, noisy_image_uint8)
    _, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(image, cmap="gray")
    ax[0].set_title("Image Originale")
    ax[0].axis("off")

    ax[1].imshow(noisy_image, cmap="gray")
    ax[1].set_title(f"Image avec bruit {titre}")
    ax[1].axis("off")

    plt.show()


def main():
    while True:
        options = ["[a] Additif", "[m] Multiplicatif", "[p] Poivre et Sel", "[q] Quitter"]
        terminal_menu = TerminalMenu(options, title="Choix du bruitage")
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 3:
            break
        arg = options[menu_entry_index][1]
        titre = options[menu_entry_index][4:]
        print(f"Generation du bruit {titre}")
        generate_noisy_image(arg, titre)


if __name__ == "__main__":
    main()
