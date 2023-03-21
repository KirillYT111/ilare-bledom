from os import system
from utils import run_python, clear_screen

clear_screen()

print("Запуск IlareBledom effects")
print(
    """\nВведите название эффекта без расширения\n
    Устройство станет доступным только
    после закрытия эффекта"""
)

effect = input("Название эффекта(без расширения) > ")

run_python(f"{effect}.py")
