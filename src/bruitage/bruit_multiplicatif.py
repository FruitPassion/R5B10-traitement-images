import numpy as np

from src.gaussian_noise import get_gaussian_noise


def bruit_multiplicatif(pixel_value: float, mean: float, std_dev: float) -> float:
    gaussian_noise = get_gaussian_noise(mean, std_dev)

    # Multiplier le bruit gaussien à la valeur du pixel
    noisy_pixel_value = pixel_value * (1 + gaussian_noise)

    # Limiter la valeur du pixel bruité entre 0 et 1
    noisy_pixel_value = np.clip(noisy_pixel_value, 0, 1)

    return noisy_pixel_value
