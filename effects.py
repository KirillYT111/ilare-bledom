from os import system
system("cls")
print("Запуск IlareBledom effects")
print("\nВведите название эффекта без расширения\nУстройство станет доступным только после закрытия эффекта")
effect = input("Название эффекта(без расширения) >")
system(f'start {effect}.py')
