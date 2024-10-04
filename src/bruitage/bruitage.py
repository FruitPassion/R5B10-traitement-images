import numpy as np
from tqdm import tqdm

from src.bruitage.bruit_additif import bruit_additif
from src.bruitage.bruit_multiplicatif import bruit_multiplicatif
from src.image_management import display_images, load_image, save_image
from src.bruitage.bruit_sel_poivre import salt_pepper_noise


def get_noise_settings(arg: str) -> dict:
    """Retourne les paramètres de bruitage pour un type de bruit donné."""
    noise_settings = {"a": {"mean": 0, "std_dev": 0.1}, "m": {"mean": -0.7, "std_dev": 0.1}, "p": {"rate": 10}}
    return noise_settings.get(arg, {})


def apply_noise(image: np.ndarray, noise_function: callable, **kwargs) -> np.ndarray:
    """Applique la fonction de bruitage sélectionnée à chaque pixel de l'image avec une barre de progression."""
    noisy_image = np.zeros_like(image)
    total_pixels = image.shape[0] * image.shape[0]

    with tqdm(total=total_pixels, desc="Application du bruit", unit=" pixels") as pbar:
        for i in range(image.shape[0]):
            for j in range(image.shape[0]):
                noisy_image[i, j] = noise_function(image[i, j], **kwargs)
                pbar.update(1)

    return np.clip(noisy_image, 0, 1)


def generate_noisy_image(arg: str, noise_name: str) -> None:
    """Génerer une image bruitée en fonction du type de bruit sélectionné."""
    image = load_image("images_reference/image_reference1.png")
    settings = get_noise_settings(arg)

    noise_functions = {
        "a": lambda pixel, mean, std_dev: bruit_additif(pixel, mean, std_dev),
        "m": lambda pixel, mean, std_dev: bruit_multiplicatif(pixel, mean, std_dev),
        "p": lambda pixel, rate: salt_pepper_noise(pixel, rate),
    }

    noisy_image = apply_noise(image, noise_functions[arg], **settings)

    save_image(noisy_image, f"bruitage_{arg}")
    display_images(image, noisy_image, "bruitage", noise_name)
