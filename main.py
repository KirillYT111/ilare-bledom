from os import system
from time import sleep

import yaml

from bledom import BleLedDevice, run_sync

from colors import COLORS
from utils import get_help_msg, clear_screen, run_python

EFFECT = "o"
version = "1.6"


async def main(device: BleLedDevice):
    while True:
        clear_screen()
        print(get_help_msg())
        effect = input("Введите имя эффекта > ")
        
        if effect == EFFECT:
            run_python("effects.py")

        color = COLORS.get(effect)
        if color is None:
            continue

        await device.set_color(*color.get_raw_values())


if __name__ == "__main__":
    print("Запуск IlareBledom ", version)
    sleep(1)
    clear_screen()
    run_sync(main)
