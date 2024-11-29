from random import random

import numpy as np


def get_gaussian_noise(mean: float, std_dev: float) -> float:
    """Retourne un bruit gaussien.

    Args:
        mean (float): Moyenne de la distribution.
        std_dev (float): Écart-type de la distribution.
    """
    seed = int(random() * 100)
    rng = np.random.default_rng(seed)
    return rng.normal(mean, std_dev)
