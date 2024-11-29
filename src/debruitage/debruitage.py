import numpy as np
from tqdm import tqdm

from src.debruitage.debruitage_convolution import debruitage_convolution
from src.debruitage.debruitage_median import debruitage_median
from src.image_management import display_images, load_image, save_image
from src.snr import get_snr


def _get_denoise_function(arg: str) -> dict:
    """Retourne la fonction de debruitage appropriée en fonction de l'argument."""
    denoise_functions = {"m": debruitage_median, "c": debruitage_convolution}
    return denoise_functions.get(arg, {})


def _apply_denoising(image: np.ndarray, denoise_function: callable, **kwargs) -> np.ndarray:
    """Applique la fonction de débruitage sélectionnée à chaque pixel de l'image."""
    denoised_image = np.zeros_like(image)
    total_pixels = image.shape[0] * image.shape[0]

    # **kwargs est utilisé pour passer des paramètres supplémentaires à la fonction de débruitage, il s'agit de la taille du voisinage
    taille_voisinage = kwargs.get("taille_voisinage", 1)

    with tqdm(total=total_pixels, desc="Application du debruitage", unit=" pixels") as pbar:
        for i in range(image.shape[0]):
            for j in range(image.shape[0]):
                denoised_image[i, j] = denoise_function(image, i, j, taille_voisinage)
                pbar.update(1)

    return np.clip(denoised_image, 0, 1)


def denoising_image(arg: str, denoise_name: str, image_path: str, display: bool = True, **kwargs) -> float:
    """Débruite une image en utilisant la méthode de débruitage sélectionnée.

    Args:
        arg (str): Argument pour sélectionner la méthode de débruitage.
        denoise_name (str): Nom de la méthode de débruitage.
        image_path (str): Chemin de l'image à débruiter.
        display (bool): Afficher les images avant et après débruitage. Si False, les images ne sont pas affichées ni sauvegardées.
        **kwargs: Paramètres supplémentaires pour la fonction de débruitage. Par exemple, la taille du voisinage (taille_voisinage).
    """
    image = load_image(image_path)
    denoise_function = _get_denoise_function(arg)
    denoised_image = _apply_denoising(image, denoise_function, **kwargs)

    if display:
        save_image(denoised_image, "debruitee")
        display_images(image, denoised_image, "débruitage", denoise_name)
    return get_snr(image, denoised_image)
