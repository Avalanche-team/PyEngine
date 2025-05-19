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

BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
CROSS_OUT = "\033[9m"

DIM = "\033[2m"
NORMAL = "\033[22m"
TEXT_COLOUR_REVERSE = "\033[7m"
INVISIBLE = "\033[8m"


def _get_colour_text(level, *args):
    temp_text = ""

    temp_text += BOLD if "bold" in args else ""
    temp_text += DIM if "dim" in args else ""
    temp_text += UNDERLINE if "underline" in args else ""
    temp_text += ITALIC if "italic" in args else ""
    temp_text += CROSS_OUT if "cross-out" in args else ""

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


def log_to_console(level: LogLevel, message: str, *args, extra_info: bool = True):
    text = ""

    text += _get_colour_text(level,*args)
    if extra_info:
        text += f"[{datetime.now().strftime("%H-%M-%S")}] "

    text += message + RESET

    print(text)
