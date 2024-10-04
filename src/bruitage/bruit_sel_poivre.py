import random as rd


def salt_pepper_noise(pixel: int, rate: int) -> int:
    # default rate value 1000 ->> 0.1% of the pixels will be affected
    if rd.randint(0, rate) <= 2:
        if rd.randint(0, 1) == 0:
            pixel = 0  # salt
        else:
            pixel = 255  # pepper
    return pixel
