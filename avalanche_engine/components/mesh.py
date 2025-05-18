from ..config import *
from .component import Component

class Mesh(Component):
    def __init__(self,
                 positions: list[float] = None,
                 texture_coord: list[float] = None):
        super().__init__()

        self.type = "MESH"
        self.positions = positions or []
        self.texture_coord = texture_coord or []

        self.vao = None
        self.vbo = None
        self.ebo = None
        self.should_render = True

    def on_create(self):
        positions = np.array(self.positions, dtype='f4').reshape(-1, 3)
        texcoords = np.array(self.texture_coord, dtype='f4').reshape(-1, 2)

        vertex_data = np.hstack((positions, texcoords)).flatten().astype('f4')

        self.vbo = self.engine.ctx.buffer(vertex_data.tobytes())
        content = [(self.vbo, '3f 2f', 'in_position',"in_texcoord")]

        # Uses engine.shader (make sure it exists before mesh is created!)
        self.vao = self.engine.ctx.vertex_array(self.scene.shader.program, content)

    def on_render(self):
        if self.should_render and self.vao:
            self.vao.render(mode=mgl.TRIANGLES)

    def on_close(self):
        self.vao.release()