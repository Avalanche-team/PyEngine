from ..config import *
from enum import Enum


class Type:
    CUSTOM = "custom"
    MESH = "mesh"

class Component:
    def __init__(self):
        self.engine = None
        self.game_object = None
        self.ctx = None

        self.shader = None

    def create(self):
        pass

    def event_handler(self,event):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def close(self):
        pass