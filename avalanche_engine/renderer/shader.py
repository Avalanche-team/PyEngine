from ..config import *

class Shader:
    VERTEX_SHADER_SRC = """
    #version 330
    
    in vec3 in_position;
    in vec2 in_tex_coords;
    in vec3 in_normal;
    
    void main() {
        gl_Position = vec4(in_position, 1.0);
    }
    """

    FRAGMENT_SHADER_SRC = """
    #version 330
    
    out vec4 f_color;
    
    void main() {
        f_color = vec4(1.0);
    }
    """