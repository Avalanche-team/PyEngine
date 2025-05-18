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

        self.engine_texture = None

    def on_create(self):
        self.engine_texture = self.engine.ctx.texture((self.width, self.height), 4, self.image_data)
        self.engine_texture.build_mipmaps()

    def on_update(self):
        if self.engine_texture:
            self.engine_texture.use(location=0)  # Needs to be bound every frame
