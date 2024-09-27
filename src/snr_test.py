from snr import get_snr
from skimage import io

imageSignal = io.imread('images_reference/image_reference1.png')
imageBruit = io.imread('images_reference/image1_bruitee_snr_9.2885.png')


print(get_snr(imageSignal, imageBruit))