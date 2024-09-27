from math import log10
from skimage import img_as_float

def get_snr(imageSignal, imageBruit):
    
    imageSignal = img_as_float(imageSignal)
    imageBruit = img_as_float(imageBruit)
    signal, bruit = 0, 0
    if imageSignal.shape != imageBruit.shape:
        raise ValueError("Les deux images doivent avoir la même taille")
   
    for i in range(imageSignal.shape[0]):
        for j in range(imageSignal.shape[1]):
            signal += imageSignal[i, j]**2
            bruit += imageBruit[i, j]**2
          
    print("signal : ", signal, "\n", "bruit : ", bruit)
    return 10 * log10(signal/bruit)
