import os


DARK_THEME = {
    "--bg-primary": "#1a1a1a",
    "--bg-secondary": "#2b2b2b",
    "--fg-primary": "#f9f9f9",
    "--fg-secondary": "#e8e8e8",
    "--disabled": "#797979",
    "--danger": "#bf0000",
    "--danger-hover": "#ff0000",
    "--blue": "#23a2ff",
    "--blue-hover": "#0392cf",
    "--btn-general": "#3f3f3f",
    "--btn-general-hover": "#6f6f6f",
}


def get_style():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "input.css")

    with open(file_path, "r") as f:
        content = f.read()

    sorted_keys = sorted(DARK_THEME.keys(), key=len, reverse=True)

    for variable in sorted_keys:
        content = content.replace(variable, DARK_THEME[variable])

    return content