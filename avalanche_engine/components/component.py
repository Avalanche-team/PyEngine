from ..config import *
from ..utils.logger import log_to_console, LogLevel


class Component:
    def __init__(self):
        """this class will be the base class for other classes to inherit to become a component."""

        self.type = "UNDEFINED"

        self.initialised = False

        self.engine = None
        self.scene = None
        self.game_object = None

    def on_create(self):
        """this function will be called when this class is to be initialised"""
        self.initialised = True
        log_to_console(LogLevel.INFO,f"Created {self.type}","bold","underline",extra_info=True)

    def on_event(self,event):
        pass

    def on_update(self):
        """this function calls every frame for code only (NO RENDERING)"""
        pass

    def on_render(self):
        """this function calls every frame to render graphics to the screen"""
        pass

    def on_close(self):
        log_to_console(LogLevel.WARNING, f"Destroyed {self.type}", "bold", "underline", extra_info=True)