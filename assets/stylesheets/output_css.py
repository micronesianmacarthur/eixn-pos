import os


def get_style():
    current_dir = os.path.dirname(__file__)

    file_path = os.path.join(current_dir, "input.css")

    with open(file_path, "r") as f:
        return f.read()