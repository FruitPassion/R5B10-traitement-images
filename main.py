from simple_term_menu import TerminalMenu

from src.noise_generator import generate_noisy_image


def main() -> None:
    options = {0: ("a", "Additif"), 1: ("m", "Multiplicatif"), 2: ("p", "Poivre et Sel"), 3: ("q", "Quitter")}

    while True:
        menu = TerminalMenu([f"[{v[0]}] {v[1]}" for v in options.values()], title="Choix du bruitage")
        menu_entry_index = menu.show()

        if menu_entry_index == 3:
            break

        # if menu_entry_index beetwen 0 and 2
        if menu_entry_index < 3:
            arg, noise_name = options[menu_entry_index]
            print(f"Génération bruit {noise_name}")
            generate_noisy_image(arg, noise_name)


if __name__ == "__main__":
    main()
