import numpy as np
from time import time

# mean = 0  # Centré sur 0 (pas de biais)
# std_dev = 10  # Déviation standard de 10


def bruit_additif(pixel_value, mean, std_dev):
    gaussian_noise = np.random.normal(mean, std_dev)

    # Ajouter le bruit gaussien à la valeur du pixel
    noisy_pixel_value = pixel_value + gaussian_noise

    # Limiter la valeur du pixel bruité entre 0 et 1
    noisy_pixel_value = np.clip(noisy_pixel_value, 0, 1)

    return noisy_pixel_value
