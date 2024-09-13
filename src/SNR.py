from math import log10

def getSNR(imageSignal, imageBruit):
    signal, bruit = 0, 0
    #si l'image difère en taille l'algo marche pas
    #sa marche pas
    for i in range(imageSignal.shape[0]):
        for j in range(imageSignal.shape[1]):
            signal += imageSignal[i, j] ** 2
            bruit += imageBruit[i, j] ** 2

    return 10 * log10(signal / bruit)