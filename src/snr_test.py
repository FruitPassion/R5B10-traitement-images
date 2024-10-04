from skimage import io

from snr import get_snr

imageSignal = io.imread("images_reference/image_reference1.png")
# imageBruit = io.imread('images_reference/image1_bruitee_snr_41.8939.png')
imageBruit = io.imread("images_reference/image1_bruitee_snr_16.4138.png")
print("SNR : ", get_snr(imageSignal, imageBruit))
