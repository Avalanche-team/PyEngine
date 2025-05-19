from ..config import *
from .component import Component
from .texture import Texture

class Material(Component):
    def __init__(self):
        super().__init__()

        self.type = "MATERIAL"

        self.colour = (1.0, 0.0, 1.0, 1.0)
        self.blend = 0.0

        self.textures_to_add = {}

        self.diffuse_map = None
        self.normal_map = None
        self.height_map = None
        self.specular_map = None
        self.glossiness_map = None
        self.roughness_map = None
        self.metalic_map_map = None
        self.ambient_occlusion_map = None

        self.set_normal_map(int)

    def set_diffuse_map(self,texture:Texture):
        if self.initialised:
            # Sets texture if this component is initialised
            if hasattr(texture, "type") and texture.type == "TEXTURE":
                self.diffuse_map = self.engine.ctx.texture(texture.get_size(), texture.get_channels(),
                                                           texture.get_image_data())
                self.diffuse_map.build_mipmaps()

                self.diffuse_map.use(location=0)
        else:
            # adds it to a list to add
            self.textures_to_add["diffuse map"] = texture

    def set_normal_map(self,texture):
        self.normal_map = texture if issubclass(texture,Texture) else None

    def on_create(self):
        # create textures that are waiting to be added
        super().on_create()
        
        for texture_type in self.textures_to_add:
            texture = self.textures_to_add[texture_type]
            match texture_type:
                case "diffuse map":
                    self.set_diffuse_map(texture)

    def on_update(self):
        shader = self.scene.shader.program

        shader["u_colour"].value = self.colour
        shader["u_blend"].value = self.blend

        if self.diffuse_map:
            self.diffuse_map.use(location=0)

