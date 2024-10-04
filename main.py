#!.venv/bin/python3
from simple_term_menu import TerminalMenu

from src.bruitage.bruitage import generate_noisy_image
from src.debruitage.debruitage import denoising_img


def generate_menu(options: dict, title: str) -> int:
    menu = TerminalMenu([f"[{v[0]}] {v[1]}" for v in options.values()], title=title)
    return menu.show()


def menu_bruitage():
    options = {0: ("a", "Additif"), 1: ("m", "Multiplicatif"), 2: ("p", "Poivre et Sel"), 3: ("q", "Quitter")}

    while True:
        menu = generate_menu(options, "Choix du bruit")

        if menu == 3:
            break
        elif menu < 3:
            arg, noise_name = options[menu]
            print(f"Génération bruit {noise_name}")
            generate_noisy_image(arg, noise_name)


def menu_debruitage():
    options = {0: ("m", "Médian"), 1: ("q", "Quitter")}

    while True:
        menu = generate_menu(options, "Choix du debruitage")

        if menu == 1:
            break
        elif menu == 0:
            denoising_img()


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
            # add .gitkeep file to keep the directory in git
            open("out/.gitkeep", "w").close()
            print("Dossier out vidé.")


def main() -> None:
    options = {0: ("b", "Bruitage"), 1: ("d", "Debruitage"), 2: ("s", "Calcul du SNR"), 3: ("u", "Utiles"), 4: ("q", "Quitter")}

    while True:
        menu = generate_menu(options, "Choix de l'opération")

        if menu == 0:
            menu_bruitage()
        elif menu == 1:
            menu_debruitage()
        elif menu == 2:
            menu_debruitage()
        elif menu == 3:
            menu_utiles()
        else:
            break


if __name__ == "__main__":
    main()
