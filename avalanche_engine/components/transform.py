from ..config import *
from .component import Component

class Transform(Component):
    def __init__(self,position=(0,0,0),rotation=(0,0,0),scale=(1,1,1)):
        super().__init__()

        self.type = "TRANSFORM"

        self.position = glm.vec3(position)
        self.rotation = glm.vec3(rotation)
        self.scale = glm.vec3(scale)

        self.m_model = glm.mat4(1.0)  # Initialize with identity matrix
        self.last_position = glm.vec3(position)
        self.last_rotation = glm.vec3(rotation)
        self.last_scale = glm.vec3(scale)


    def on_create(self):
        super().on_create()
        self.m_model = self.get_model_matrix()

    def get_model_matrix(self):
        model = glm.mat4(1.0)

        model = glm.translate(model, self.position)

        model = glm.rotate(model, self.rotation.x, glm.vec3(1, 0, 0))
        model = glm.rotate(model, self.rotation.y, glm.vec3(0, 1, 0))
        model = glm.rotate(model, self.rotation.z, glm.vec3(0, 0, 1))

        model = glm.scale(model, self.scale)

        return model

