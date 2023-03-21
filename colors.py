from dataclasses import dataclass
from enum import Enum


@dataclass
class RgbColor:
    RED: int
    GREEN: int
    BLUE: int

    def get_raw_values(self) -> tuple[int, int, int]:
        return self.RED, self.GREEN, self.BLUE


RED = RgbColor(255, 0, 0)
GREEN = RgbColor(0, 255, 0)
BLUE = RgbColor(0, 0, 255)
YELLOW = RgbColor(255, 255, 0)
CYAN = RgbColor(0, 255, 255)
PURPLE = RgbColor(255, 0, 255)
ORANGE = RgbColor(196, 98, 16)


class CommandColor(str, Enum):
    RED = "r"
    GREEN = "g"
    BLUE = "b"
    YELLOW = "y"
    CYAN = "t"
    PURPLE = "p"
    ORANGE = "o"


COLORS = {
    CommandColor.RED.value: RED,
    CommandColor.GREEN.value: GREEN,
    CommandColor.BLUE.value: BLUE,
    CommandColor.YELLOW.value: YELLOW,
    CommandColor.CYAN.value: CYAN,
    CommandColor.PURPLE.value: PURPLE,
    CommandColor.ORANGE.value: ORANGE,
}
