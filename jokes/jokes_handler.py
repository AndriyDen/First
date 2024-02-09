import random
import pathlib



def get_joke():
    path = pathlib.Path(__file__).parent
    try:
        with open(path / "jokes.txt", "r", encoding="utf-8") as file:
            all_lines = [line.strip() for line in file.readlines()]
        return random.choice(all_lines)
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."
