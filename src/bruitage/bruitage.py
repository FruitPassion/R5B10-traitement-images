import numpy as np
from tqdm import tqdm

from src.bruitage.bruit_additif import bruit_additif
from src.bruitage.bruit_multiplicatif import bruit_multiplicatif
from src.bruitage.bruit_sel_poivre import salt_pepper_noise
from src.image_management import display_images, load_image, save_image
from src.snr import get_snr


def _get_noise_settings(arg: str, **kwargs) -> dict:
    """Retourne les paramètres de bruitage pour un type de bruit donné, avec possibilité de personnalisation."""
    default_noise_settings = {
        "a": {"mean": 0, "std_dev": 0.1},
        "m": {"mean": -0.7, "std_dev": 0.1},
        "p": {"rate": 10},
    }

    noise_settings = default_noise_settings.get(arg, {})
    noise_settings.update(kwargs)
    return noise_settings


def _apply_noise(image: np.ndarray, noise_function: callable, **kwargs) -> np.ndarray:
    """Applique la fonction de bruitage sélectionnée à chaque pixel de l'image avec une barre de progression."""
    noisy_image = np.zeros_like(image)
    total_pixels = image.shape[0] * image.shape[0]

    with tqdm(total=total_pixels, desc="Application du bruit", unit=" pixels") as pbar:
        for i in range(image.shape[0]):
            for j in range(image.shape[0]):
                noisy_image[i, j] = noise_function(image[i, j], **kwargs)
                pbar.update(1)

    return np.clip(noisy_image, 0, 1)


def generate_noisy_image(arg: str, noise_name: str, image_path: str, display: bool = True, **kwargs) -> float:
    """Génerer une image bruitée en fonction du type de bruit sélectionné, avec paramètres personnalisables.

    Args:
        arg (str): Type de bruit à appliquer (a: additif, m: multiplicatif, p: poivre et sel)
        noise_name (str): Nom du type de bruit
        image_path (str): Chemin de l'image à bruiter
        display (bool, optional): Afficher les images bruitées. Defaults to True. Si False, les images ne sont pas affichées ni sauvegardées.
        **kwargs: Paramètres supplémentaires pour la fonction de bruitage. Par exemple, mean et std_dev pour le bruit additif ou multiplicatif, rate pour le bruit poivre et sel.
    """
    image = load_image(image_path)
    settings = _get_noise_settings(arg, **kwargs)

    noise_functions = {
        "a": lambda pixel, mean, std_dev: bruit_additif(pixel, float(mean), float(std_dev)),
        "m": lambda pixel, mean, std_dev: bruit_multiplicatif(pixel, float(mean), float(std_dev)),
        "p": lambda pixel, rate: salt_pepper_noise(pixel, int(rate)),
    }

    noisy_image = _apply_noise(image, noise_functions[arg], **settings)
    snr = get_snr(noisy_image, image)

    print(f"SNR: {snr:.2f} dB")

    if display:
        save_image(noisy_image, f"bruitage_{arg}")
        display_images(image, noisy_image, "bruitage", noise_name)
    return snr
