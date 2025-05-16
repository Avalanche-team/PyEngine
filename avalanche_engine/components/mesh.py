from ..config import *
from .component import Component

class Mesh(Component):
    def __init__(self):
        super().__init__()

        self.type = "MESH"

        self.vao = None
