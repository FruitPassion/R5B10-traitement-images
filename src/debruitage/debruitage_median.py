import numpy as np


def debruitage_median(image: np.ndarray, i: int, j: int, taille_voisinage: int = 2) -> float:
    """Applique un filtre médian sur une fenêtre de l'image.

    Args:
        image (np.ndarray): Image à débruiter.
        i (int): Position x du pixel à débruiter.
        j (int): Position y du pixel à débruiter.
        taille_voisinage (int): Taille du voisinage pour le filtre médian.<br>Un voisinage de taille 1 correspond à une fenêtre 3x3, un voisinage de taille 2 correspond à une fenêtre 5x5, etc.
    """
    voisins = []
    for x in range(i - taille_voisinage, i + taille_voisinage + 1):
        for y in range(j - taille_voisinage, j + taille_voisinage + 1):
            if 0 <= x < image.shape[0] and 0 <= y < image.shape[0]:
                voisins.append(image[x, y])
    return np.median(voisins)
