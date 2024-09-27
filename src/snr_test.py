from snr import get_snr
from skimage import io

imageSignal = io.imread('images_reference/image_reference1.png')
#imageBruit = io.imread('images_reference/image1_bruitee_snr_41.8939.png')
imageBruit = io.imread('images_reference/image1_bruitee_snr_16.4138.png')
print("SNR : ", get_snr(imageSignal, imageBruit))