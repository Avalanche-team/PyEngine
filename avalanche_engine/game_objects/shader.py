from avalanche_engine.config import *
from avalanche_engine.game_objects.game_object import GameObject


class Shader(GameObject):
    VERTEX_SHADER_SRC = """
    #version 330 core

    in vec3 in_position;
    in vec2 in_texcoord;
    
    out vec2 f_texcoord;
    
    uniform mat4 u_view;
    uniform mat4 u_proj;
    uniform mat4 u_model;  
    
    void main() {
        f_texcoord = in_texcoord;
    
        gl_Position = u_proj * u_view * u_model * vec4(in_position, 1.0);
    }
    """

    FRAGMENT_SHADER_SRC = """
    #version 330

    out vec4 f_color;
    
    in vec2 f_texcoord;
    
    uniform sampler2D u_texture;  // Diffuse texture, or your first texture
    uniform vec4 u_colour;        // The color to mix with
    uniform float u_blend;        // Blend factor between texture and color
    
    void main() {
    float gamma = 2.2;

    vec4 textureColour = texture(u_texture, f_texcoord);
    vec4 colour = mix(textureColour, u_colour, u_blend);

    // Remove gamma correction to test
    f_color = colour;  
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

    def on_update(self):
        super().on_update()

    def on_close(self):
        self.program.release()