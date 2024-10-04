import numpy as np


def debruitage_median(image: np.ndarray, i: int, j: int, taille_voisinage: int = 2) -> float:
    """Applique un filtre médian sur une fenêtre de l'image."""
    if int(image[i, j]) == 1 or str(image[i, j]) == "0.0":
        return image[i, j]
    voisins = []
    for x in range(i - taille_voisinage, i + taille_voisinage + 1):
        for y in range(j - taille_voisinage, j + taille_voisinage + 1):
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[0]:
                voisins.append(image[x, y])
    return np.median(voisins)
