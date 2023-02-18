from time import sleep
from bledom import BleLedDevice, run_sync
from os import system
import yaml
version = "1.6"
print("Запуск IlareBledom ", version)
sleep(1)
system("cls")
async def main(device: BleLedDevice):
	while True:
		system("cls")
		print("\nВстроеные эффекты:")
		print("r - статический красный")
		print("g - статический зеленый")
		print("b - статический синий")
		print("y - статический желтый")
		print("t - статический бирюзовый")
		print("p - статический фиолетовый")
		print("o - открыть программу для чтения пользовательских эффектов")
		effect = input("Введите имя эффекта >")
		if effect == "r":
			await device.set_color(255, 0, 0)
		elif effect == "g":
			await device.set_color(0, 255, 0)
		elif effect == "b":
			await device.set_color(0, 0, 255)
		elif effect == "y":
			await device.set_color(255, 255, 0)
		elif effect == "t":
			await device.set_color(0, 255, 255)
		elif effect == "p":
			await device.set_color(255, 0, 255)
		elif effect == "o":
			system("call effects.py")
			exit()

run_sync(main)