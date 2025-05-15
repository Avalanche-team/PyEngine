from logging import fatal
from math import trunc

from ..config import *
from ..game_objects.game_object import GameObject


class Scene:
    def __init__(self):
        """this class will contain all the game objects and will act like a level that can change"""

        self.engine = None

        self.game_objects = []
        self.initialised = False

    def on_create(self):
        self.initialised = True

    def add_game_object(self,game_object):
        if isinstance(game_object,GameObject):
            if self.initialised:
                game_object.engine = self.engine
                game_object.scene = self
                game_object.on_create()

            self.game_objects.append(game_object)
        else:
            raise ValueError("Make sure the component is instance of class [GameObject]")

    def on_event(self,event):
        for game_object in self.game_objects:
            game_object.on_event(event)

    def on_update(self):
        for game_object in self.game_objects:
            game_object.on_update()

    def on_render(self):
        for game_object in self.game_objects:
            game_object.on_render()

    def on_close(self):
        for game_object in self.game_objects:
            game_object.on_close()