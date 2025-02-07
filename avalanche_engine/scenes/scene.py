from ..config import *
from ..shader import Shader


class Scene:


    def __init__(self):
        self.engine = None
        self.ctx = None

        self.shader = Shader()

        self.game_objects = []

    def add_game_object(self,game_object):
        game_object.create()
        self.game_objects.append(game_object)

    def create(self):
        pass

    def event_handler(self,event):
        for game_object in self.game_objects:
            game_object.event_handler(event)

    def update(self):
        for game_object in self.game_objects:
            game_object.update()

    def render(self):
        for game_object in self.game_objects:
            game_object.render()

    def close(self):
        for game_object in self.game_objects:
            game_object.close()