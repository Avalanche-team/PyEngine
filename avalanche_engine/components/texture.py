from ..config import *
from .component import Component

class Texture(Component):
    def __init__(self, texture_path):
        super().__init__()

        self.type = "TEXTURE"

        self.texture = pg.image.load(texture_path).convert_alpha()
        self.texture = pg.transform.flip(self.texture, False, True)

        self.image_data = pg.image.tobytes(self.texture, "RGBA", True)
        self.width, self.height = self.texture.get_size()
        self.channels = 4

        self.on_create()


    def get_size(self):
        return self.width,self.height

    def get_channels(self):
        return self.channels

    def get_image_data(self):
        return self.image_data