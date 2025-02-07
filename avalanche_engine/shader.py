from .config import *

class Shader:
    VERTEX_SHADER = """
    #version 330 core
    
    void main(){
        gl_Position = vec4();
    }
    """

    FRAGMENT_SHADER = """
    #version 330 core
    
    void main(){
    
    }
    """

    def __init__(self):
        self.engine = None
        self.ctx = None

        self.shader_program = None

    def create(self):
        self.shader_program = self._get_shader_program()

    def _get_shader_program(self):
        return self.ctx.program(
            vertex_shader=Shader.VERTEX_SHADER,
            fragment_shader=Shader.FRAGMENT_SHADER
        )

