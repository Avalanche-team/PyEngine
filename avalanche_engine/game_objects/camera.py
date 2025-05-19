from .game_object import GameObject
from ..config import *

class Camera(GameObject):
    def __init__(self,position=None,yaw=-90,pitch=0):
        super().__init__()

        self.fov = 50
        self.near = 0.1
        self.far = 100
        self.speed = 10
        self.sensitivity = 0.1

        self.position = position if position else glm.vec3(2,3,3)
        self.up = glm.vec3(0,1,0)
        self.right = glm.vec3(1,0,0)
        self.forward = glm.vec3(0,0,-1)

        self.yaw = yaw
        self.pitch = pitch

        self.win_size = pg.display.get_surface().size

        self.aspect_ratio = self.win_size[0] / self.win_size[1]

        self.m_proj = None
        self.m_view = None

        pg.mouse.set_visible(False)
        pg.event.set_grab(True)

        self.active = True

    def move(self):
        velocity = self.speed * self.scene.engine.dt
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_SPACE]:
            self.position += self.up * velocity
        if keys[pg.K_LCTRL]:
            self.position -= self.up * velocity

    def rotate(self):
        rel_x,rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * self.sensitivity
        self.pitch -= rel_y * self.sensitivity
        self.pitch = max(-89,min(89,self.pitch))

    def update_camera_vectors(self):
        yaw,pitch = glm.radians(self.yaw),glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward,glm.vec3(0,1,0)))
        self.up = glm.normalize(glm.cross(self.right,self.forward))

    def on_create(self):
        self.m_proj = self._get_projection_matrix()
        self.m_view = self._get_view_matrix()

    def _get_projection_matrix(self):
        return glm.perspective(glm.radians(self.fov),self.aspect_ratio,self.near,self.far)

    def _get_view_matrix(self):
        return glm.lookAt(self.position,self.position + self.forward,self.up)

    def on_update(self):
        if self.active:
            self.move()
            self.rotate()
            self.update_camera_vectors()

            pg.mouse.set_visible(False)
            pg.event.set_grab(True)
        else:
            pg.mouse.set_visible(True)
            pg.event.set_grab(False)

        self.m_view = self._get_view_matrix()

        self.scene.shader.program["u_proj"].write(self.m_proj)
        self.scene.shader.program["u_view"].write(self.m_view)
