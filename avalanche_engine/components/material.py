from ..config import *
from .component import Component

class Material(Component):
    def __init__(self):
        super().__init__()
        self.colour = (1.0, 0.0, 1.0, 1.0)
        self.blend = 0.5

    def on_update(self):
        shader = self.scene.shader.program
        shader["u_colour"].value = self.colour
        shader["u_blend"].value = self.blend

