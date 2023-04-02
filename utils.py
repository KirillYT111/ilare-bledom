import os


def is_os_windows() -> bool:
    return os.name == "nt"


def clear_screen() -> None:
    if is_os_windows():
        os.system("cls")
    else:
        os.system("clear")


def run_python(filename: str):
    if is_os_windows():
        os.system(f"call {filename}")
    else:
        os.system(f"python3 {filename}")


def get_help_msg() -> str:
    return """
    \nВстроеные эффекты:
    \nr - статический красный
    \ng - статический зеленый
    \nb - статический синий"
    \ny - статический желтый
    \nt - статический бирюзовый
    \np - статический фиолетовый
    \no - открыть программу для чтения пользовательских эффектов
    """
