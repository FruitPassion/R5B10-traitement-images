#!.venv/bin/python3
from InquirerPy import prompt

from src.bruitage.bruitage import generate_noisy_image
from src.debruitage.debruitage import denoising_image
from src.terminal_utils import list_files, generate_menu
from src.snr import get_snr
from skimage import io


def menu_choix_image(nom_menu: str = "Choix de l'image") -> str:
    files = list_files("out")
    files2 = list_files("images_reference")
    files = files + files2
    files.append("q - Quitter")

    question = [
        {
            "type": "list",
            "name": "image_choice",
            "message": nom_menu,
            "choices": files,
        }
    ]

    answer = prompt(question)
    image_path = answer["image_choice"]

    if image_path == "q - Quitter":
        return "q - Quitter"
    else:
        print(f"Image sélectionnée: {image_path}")
        return image_path


def menu_bruitage():
    options = {0: ("a", "Additif"), 1: ("m", "Multiplicatif"), 2: ("p", "Poivre et Sel")}

    while True:
        menu = generate_menu(options, "Choix du bruit")

        if menu < 3:
            arg, noise_name = options[menu]
            image_path = menu_choix_image()
            if image_path != "q - Quitter":
                print(f"Génération bruit {noise_name}")
                generate_noisy_image(arg, noise_name, image_path)
        else:
            break


def menu_debruitage():
    options = {0: ("m", "Médian"), 1: ("c", "Convolution")}

    while True:
        menu = generate_menu(options, "Choix du debruitage")

        if menu < 2:
            arg, denoise_name = options[menu]
            image_path = menu_choix_image()
            if image_path != "q - Quitter":
                print(f"Débruitage par filtre {denoise_name}")
                denoising_image(arg, denoise_name, image_path)
        else:
            break


def menu_utiles():
    options = {0: ("v", "Vider dossier out")}

    while True:
        menu = generate_menu(options, "Choix de l'utilitaire")

        if menu == 0:
            import os
            import shutil

            shutil.rmtree("out")
            os.mkdir("out")
            open("out/.gitkeep", "w").close()
            print("Dossier out vidé.")
        else:
            break


def menu_calcul_snr():
    image_signal_path = menu_choix_image(nom_menu="Choix de l'image signal")
    image_bruit_path = menu_choix_image(nom_menu="Choix de l'image bruitée")
    image_signal = io.imread(image_signal_path)
    image_bruit = io.imread(image_bruit_path)
    print("SNR : ", get_snr(image_signal, image_bruit))


def main() -> None:
    options = {0: ("b", "Bruitage"), 1: ("d", "Debruitage"), 2: ("s", "Calcul du SNR"), 3: ("c", "Détection des contours"), 4: ("u", "Utiles")}

    while True:
        menu = generate_menu(options, "Choix de l'opération")

        if menu == 0:
            menu_bruitage()
        elif menu == 1:
            menu_debruitage()
        elif menu == 2:
            menu_calcul_snr()
        elif menu == 3:
            print("Détection des contours à implémenter")
        elif menu == 4:
            menu_utiles()
        else:
            break


if __name__ == "__main__":
    main()
