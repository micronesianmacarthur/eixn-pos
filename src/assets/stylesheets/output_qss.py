import os


DARK_THEME = {
    "--bg-primary": "#1c1c1c",
    "--bg-secondary": "#2d2d2d",
    "--fg-primary": "#fafafa",
    "--fg-secondary": "#efefef",
    "--gray-primary": "#a9a9a9",
    "--gray-secondary": "#e9e9e9",
    "--red-primary": "#df2935",
    "--red-secondary": "#f00000",
    "--blue-primary": "#0094c6",
    "--blue-secondary": "#0077b6",
    "--green-primary": "#018e42",
    "--green-secondary": "#01682c",
    "--yellow-primary": "#f2c14e",
}


def get_style():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "input.qss")

    with open(file_path, "r") as f:
        content = f.read()

    sorted_keys = sorted(DARK_THEME.keys(), key=len, reverse=True)

    for variable in sorted_keys:
        content = content.replace(variable, DARK_THEME[variable])

    return content