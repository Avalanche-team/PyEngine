from ..config import *
from .component import Component
from .texture import Texture

class Material(Component):
    def __init__(self):
        super().__init__()

        self.type = "MATERIAL"

        self.colour = (1.0, 0.0, 1.0, 1.0)
        self.blend = 0.5

        self.diffuse_map = None
        self.normal_map = None
        self.height_map = None
        self.specular_map = None
        self.glossiness_map = None
        self.roughness_map = None
        self.metalic_map_map = None
        self.ambient_occlusion_map = None

        self.set_normal_map(int)

    def set_diffuse_map(self,texture):
        self.diffuse_map = texture if issubclass(texture,Texture) else None

    def set_normal_map(self,texture):
        self.normal_map = texture if issubclass(texture,Texture) else None

    def on_update(self):
        shader = self.scene.shader.program

        shader["u_colour"].value = self.colour
        shader["u_blend"].value = self.blend

