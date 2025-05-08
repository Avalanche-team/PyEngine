from .config import *

WINDOW_WIDTH = "window width"
WINDOW_HEIGHT = "window height"
WINDOW_TITLE = "window title"
WINDOW_VSYNC = "window vsync"
WINDOW_POSITION_X = "window position x"
WINDOW_POSITION_Y = "window position y"
WINDOW_FULLSCREEN = "window fullscreen"
WINDOW_BORDERLESS = "window borderless"
WINDOW_RESIZABLE = "window resizable"
WINDOW_ICON = "window icon"

window_data = {
    WINDOW_WIDTH: 1080,
    WINDOW_HEIGHT: 720,
    WINDOW_TITLE: "Avalanche Engine",
    WINDOW_VSYNC: True,
    WINDOW_POSITION_X: None,
    WINDOW_POSITION_Y: None,
    WINDOW_FULLSCREEN: False,
    WINDOW_BORDERLESS: False,
    WINDOW_RESIZABLE: False,
    WINDOW_ICON: None,
}

class Window:
    def __init__(self, data=None):
        if data is None:
            data = window_data

        flags = pg.OPENGL | pg.DOUBLEBUF

        pg.display.set_mode(
        (data[WINDOW_WIDTH],data[WINDOW_HEIGHT]),
            flags=flags,
            depth=0,
            display=0,
            vsync=data[WINDOW_VSYNC]
            )