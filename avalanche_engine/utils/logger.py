from ..config import *
from enum import Enum, auto
from datetime import datetime


class LogLevel(Enum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    DEBUG = auto()


BLUE = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
PURPLE = "\033[35m"
RESET = "\033[0m"
BOLD = "\33[1m"


def _get_colour_text(level, bold=False):
    temp_text = ""

    if bold:
        temp_text += BOLD

    match level:
        case LogLevel.INFO:
            temp_text += BLUE
        case LogLevel.WARNING:
            temp_text += YELLOW
        case LogLevel.ERROR:
            temp_text += RED
        case LogLevel.DEBUG:
            temp_text += PURPLE

    return temp_text


def log_to_console(level: LogLevel, message: str, extra_info: bool = True,bold:bool=False):
    text = ""

    text += _get_colour_text(level,bold)
    if extra_info:
        text += f"[{datetime.now().strftime("%H-%M-%S")}] "

    text += message + RESET

    print(text)
