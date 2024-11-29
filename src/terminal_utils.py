import os

from InquirerPy.separator import Separator
from InquirerPy import prompt


def list_files(directory=".") -> list:
    """
    Liste les fichiers d'un répertoire

    Args:
        directory (str): Répertoire à lister
    """
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != ".gitkeep"]
    return [os.path.join(directory, f) for f in files]


def generate_menu(options: dict, title: str) -> int:
    """
    Genere un menu à partir d'un dictionnaire d'options

    Args:
        options (dict): Dictionnaire d'options
        title (str): Titre du menu
    """
    choices = [{"name": f"{v[1]}", "value": i} for i, v in options.items()]
    choices.append({"name": Separator(), "value": None})
    choices.append({"name": "Quitter", "value": len(options)})

    question = [
        {
            "type": "list",
            "name": "menu_choice",
            "message": title,
            "choices": choices,
        }
    ]
    answer = prompt(question)
    return answer["menu_choice"]
