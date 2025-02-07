from .component import Component
from ..config import *

class Mesh(Component):
    def __init__(self,vertices=None,indices=None,tex_coords=None):
        super().__init__()

        self.vertices = vertices
        self.indices = indices
        self.tex_coords = tex_coords


    def _get_vertex_data(self):
        return np.array(self.vertices,dtype="f4")

    def _get_vbo(self):
        vertex_data = self._get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def create(self):
        pass

    def render(self):
        pass

    def update(self):
        print("ss")

    def close(self):
        pass