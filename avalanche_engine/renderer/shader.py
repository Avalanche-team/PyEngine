from ..config import *
from ..game_objects.game_object import GameObject


class Shader(GameObject):
    VERTEX_SHADER_SRC = """
    #version 330

    in vec3 in_position;

    void main() {
        gl_Position = vec4(in_position, 1.0);
    }
    """

    FRAGMENT_SHADER_SRC = """
    #version 330

    out vec4 f_color;

    void main() {
        f_color = vec4(1.0, 0.0, 0.0, 1.0);
    }
    """

    def __init__(self):
        super().__init__()
        self.program = None

    def on_create(self):
        try:
            self.program = self.engine.ctx.program(
                vertex_shader=self.VERTEX_SHADER_SRC,
                fragment_shader=self.FRAGMENT_SHADER_SRC
            )
        except Exception as e:
            print("Error compiling shader program:")
            print(e)
