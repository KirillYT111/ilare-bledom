from time import sleep
from bledom import BleLedDevice, run_sync
effname = "rgb"
print("Запуск IlareBledom эффекта ", effname)

async def main(device: BleLedDevice):
 while True:
  # Начало эффекта
  await device.set_color(255, 0, 0) # Цвет
  sleep(0.4) # Время ожидания перед сменой цветов
  await device.set_color(0, 255, 0)
  sleep(0.4)
  await device.set_color(0, 0, 255)
  sleep(0.4)
  # Конец эффекта
run_sync(main)