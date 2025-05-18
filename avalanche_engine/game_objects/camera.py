from math import radians

from ..config import *
from .game_object import GameObject

class Camera(GameObject):
    FOV = 50
    NEAR = 0.1
    FAR = 3000
    SPEED = 0.005
    SENSITIVITY = 0.04

    def __init__(self,position=(0,0,4),yaw=-90,pitch=0):
        super().__init__()

        self.aspect_ratio = None
        self.position = vector3.create(position[0],position[1],position[2])
        self.up = vector3.create(0, 1, 0)
        self.right = vector3.create(1, 0, 0)
        self.forward = vector3.create(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch

    def on_create(self):
        self.aspect_ratio = self.engine.active_window.get_size()[0] / self.engine.active_window.get_size()[1]
        self.up = vector3.create(0, 1, 0)
        self.right = vector3.create(1, 0, 0)
        self.forward = vector3.create(0, 0, -1)

    def on_update(self):
        print(self.get_view_matrix())
        self.scene.shader.program["u_view"].value = self.get_view_matrix()
        self.scene.shader.program["u_proj"].value = self.get_projection_matrix()

    def get_view_matrix(self):
        view_mat = matrix44.create_look_at(self.position, self.position + self.forward, self.up)
        return view_mat.flatten()

    def get_projection_matrix(self):
        proj_mat =  matrix44.create_perspective_projection_matrix(
            radians(Camera.FOV), self.aspect_ratio, Camera.NEAR, Camera.FAR
        )
        return proj_mat.flatten()