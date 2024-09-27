from random import random

import numpy as np


def get_gaussian_noise(mean: float, std_dev: float) -> float:
    """Retourne un bruit gaussien."""
    seed = int(random() * 100)
    rng = np.random.default_rng(seed=seed)
    return rng.normal(mean, std_dev)
