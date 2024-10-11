import os

from simple_term_menu import TerminalMenu


def list_files(directory="."):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != ".gitkeep"]
    return [os.path.join(directory, f) for f in files]


def generate_menu(options: dict, title: str) -> int:
    menu = TerminalMenu([f"[{v[0]}] {v[1]}" for v in options.values()], title=title)
    return menu.show()
