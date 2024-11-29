import random as rd


def salt_pepper_noise(pixel: int, rate: int) -> int:
    """ Ajoute du bruit sel et poivre à un pixel
    
    Args:
        pixel (int): Pixel à bruité.
        rate (int): Taux de bruitage.
    """
    if rd.randint(0, 100 - rate) <= 2:
        if rd.randint(0, 1) == 0:
            pixel = 0  # salt
        else:
            pixel = 255  # pepper
    return pixel
