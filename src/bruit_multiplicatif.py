import numpy as np
from time import time

# mean = 1 # Bruit multiplicatif autour de 1 (pas de changement moyen)
# std_dev = 0.1 # Écart type (contrôle l'intensité du bruit)


def bruit_multiplicatif(pixel_value, mean, std_dev) -> int:
    # Générer un bruit gaussien
    seed = int(time())
    rng = np.random.default_rng(seed)
    gaussian_noise = rng.normal(mean, std_dev)

    # Ajouter le bruit gaussien à la valeur du pixel
    noisy_pixel_value = pixel_value + gaussian_noise

    # Limiter la valeur du pixel bruité entre 0 et 255
    noisy_pixel_value = np.clip(noisy_pixel_value, 0, 255)

    return int(noisy_pixel_value)
