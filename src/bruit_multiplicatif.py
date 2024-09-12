import numpy as np
from time import time

# mean = 1 # Bruit multiplicatif autour de 1 (pas de changement moyen)
# std_dev = 0.1 # Écart type (contrôle l'intensité du bruit)


def bruit_multiplicatif(pixel_value, mean, std_dev) -> float:
    gaussian_noise = np.random.normal(mean, std_dev)

    # Multiplier le bruit gaussien à la valeur du pixel
    noisy_pixel_value = pixel_value * (1 + gaussian_noise)

    # Limiter la valeur du pixel bruité entre 0 et 1
    noisy_pixel_value = np.clip(noisy_pixel_value, 0, 1)

    return noisy_pixel_value
