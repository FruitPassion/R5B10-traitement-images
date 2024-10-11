#!.venv/bin/python3

from src.bruitage.bruitage import generate_noisy_image
from src.debruitage.debruitage import denoising_image
from src.terminal_utils import generate_menu, list_files
from simple_term_menu import TerminalMenu


def menu_choix_image() -> str:
    files = list_files("out")
    files2 = list_files("images_reference")
    files = files + files2
    files.append("q - Quitter")

    menu = TerminalMenu(files, title="Choix de l'image")
    menu_entry_index = menu.show()

    if menu_entry_index is None:
        return "q - Quitter"
    else:
        print(f"Image sélectionnée: {files[menu_entry_index]}")
        return files[menu_entry_index]


def menu_bruitage():
    options = {0: ("a", "Additif"), 1: ("m", "Multiplicatif"), 2: ("p", "Poivre et Sel"), 3: ("q", "Quitter")}

    while True:
        menu = generate_menu(options, "Choix du bruit")

        if menu == 3:
            break
        elif menu < 3:
            arg, noise_name = options[menu]
            image_path = menu_choix_image()
            if image_path != "q - Quitter":
                print(f"Génération bruit {noise_name}")
                generate_noisy_image(arg, noise_name, image_path)


def menu_debruitage():
    options = {0: ("m", "Médian"), 1: ("c", "Convultion"), 2: ("q", "Quitter")}

    while True:
        menu = generate_menu(options, "Choix du debruitage")

        if menu == 2:
            break
        elif menu < 2:
            arg, denoise_name = options[menu]
            image_path = menu_choix_image()
            if image_path != "q - Quitter":
                print(f"Débruitage par filtre {denoise_name}")
                denoising_image(arg, denoise_name, image_path)


def menu_utiles():
    options = {0: ("v", "Vider dossier out"), 1: ("q", "Quitter")}

    while True:
        menu = generate_menu(options, "Choix de l'utilitaire")

        if menu == 1:
            break
        elif menu == 0:
            import os
            import shutil

            shutil.rmtree("out")
            os.mkdir("out")
            open("out/.gitkeep", "w").close()
            print("Dossier out vidé.")


def menu_calcul_snr():
    print("Calcul du SNR à implémenter")


def main() -> None:
    options = {0: ("b", "Bruitage"), 1: ("d", "Debruitage"), 2: ("s", "Calcul du SNR"), 3: ("c", "Détection des contour"), 4: ("u", "Utiles"), 5: ("q", "Quitter")}

    while True:
        menu = generate_menu(options, "Choix de l'opération")

        if menu == 0:
            menu_bruitage()
        elif menu == 1:
            menu_debruitage()
        elif menu == 2:
            print("Calcul du SNR à implémenter")
        elif menu == 3:
            print("Détection des contours à implémenter")
        elif menu == 4:
            menu_utiles()
        else:
            break


if __name__ == "__main__":
    main()
