import os


def is_os_windows() -> bool:
    return os.name == "nt"


def clear_screen() -> None:
    if is_os_windows():
        os.system("cls")
    else:
        os.system("clear")
