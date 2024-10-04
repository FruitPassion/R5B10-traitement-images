import numpy as np


def debruitage_convolution(image: np.ndarray, i: int, j: int, taille_voisinage: int = 1) -> float:
    """Applique un filtre par convultion sur une fenêtre de l'image."""
    voisins = []
    for x in range(i - taille_voisinage, i + taille_voisinage + 1):
        for y in range(j - taille_voisinage, j + taille_voisinage + 1):
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[0]:
                voisins.append(image[x, y])
    return np.mean(voisins)
