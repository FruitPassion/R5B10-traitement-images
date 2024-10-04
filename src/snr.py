from math import log10

from skimage import img_as_float


def get_snr(image_bruit, image_signal):
    image_signal = img_as_float(image_signal)
    image_bruit = img_as_float(image_bruit)
    image_bruit = image_bruit - image_signal
    signal, bruit = 0, 0

    if image_signal.shape != image_bruit.shape:
        raise ValueError("Les deux images doivent avoir la même taille")

    for i in range(image_signal.shape[0]):
        for j in range(image_signal.shape[0]):
            signal += image_signal[i, j] ** 2
            bruit += image_bruit[i, j] ** 2

    # print("signal : ", signal, "\n", "bruit : ", bruit)
    return 10 * log10(signal / bruit)
