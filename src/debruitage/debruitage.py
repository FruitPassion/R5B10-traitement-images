import numpy as np
from tqdm import tqdm

from src.debruitage.debruitage_median import debruitage_median
from src.image_management import display_images, load_image, save_image


def apply_denoising(image: np.ndarray, denoise_function: callable, **kwargs) -> np.ndarray:
    """Applique la fonction de débruitage sélectionnée à chaque pixel de l'image."""
    denoised_image = np.zeros_like(image)
    total_pixels = image.shape[0] * image.shape[0]

    with tqdm(total=total_pixels, desc="Application du debruitage", unit=" pixels") as pbar:
        for i in range(image.shape[0]):
            for j in range(image.shape[0]):
                denoised_image[i, j] = denoise_function(image, i, j)
                pbar.update(1)

    return np.clip(denoised_image, 0, 1)


def denoising_img():
    """Débruite une image."""
    image = load_image("images_reference/image1_bruitee_snr_13.0913.png")
    denoised_image = apply_denoising(image, debruitage_median)

    save_image(denoised_image, "debruitee")
    display_images(image, denoised_image, "débruitage", "median")
