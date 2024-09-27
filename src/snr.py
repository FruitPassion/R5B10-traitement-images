from math import log10


def getSNR(imageSignal, imageBruit):
    signal, bruit = 0, 0

    if imageSignal.shape != imageBruit.shape:
        raise ValueError("Les deux images doivent avoir la même taille")

    for i in range(imageSignal.shape[0]):
        for j in range(imageSignal.shape[1]):
            signal += imageSignal[i, j]
            bruit += imageBruit[i, j]
    print("signal : ", signal, "\n", "bruit : ", bruit)
    return 10 * log10(signal**2 / bruit**2)
