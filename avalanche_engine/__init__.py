#----------------------------------------------------------
#                        CORE
#----------------------------------------------------------
from .engine import Engine
from .window import *

#----------------------------------------------------------
#                        SCENES
#----------------------------------------------------------
from .scenes.scene import Scene

#----------------------------------------------------------
#                      GAME OBJECTS
#----------------------------------------------------------
from .game_objects.game_object import GameObject

#----------------------------------------------------------
#                       COMPONENTS
#----------------------------------------------------------
from .components.component import Component

#----------------------------------------------------------
#                         UTILS
#----------------------------------------------------------

__all__ = [
    "Window",
    "Engine",
    "window_data",

    "WINDOW_WIDTH",
    "WINDOW_HEIGHT",
    "WINDOW_TITLE",
    "WINDOW_VSYNC",
    "WINDOW_POSITION_X",
    "WINDOW_POSITION_Y",
    "WINDOW_FULLSCREEN",
    "WINDOW_BORDERLESS",
    "WINDOW_RESIZABLE",
    "WINDOW_BACKGROUND_COLOUR",
    "WINDOW_ICON",

    "Scene",

    "GameObject",

    "Component"
]