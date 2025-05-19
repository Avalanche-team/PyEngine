from avalanche_engine import *
import pygame as pg

class Test(Scene):
    def __init__(self):
        super().__init__()

        self.square = None
        self.mat = None
        self.texture = None
        self.obj = None
        self.c = 0

    def on_create(self):
        super().on_create()

        # Create a square mesh
        self.square = get_square_mesh()

        s = load_obj_model("test/rep_inf_ep3trooper.obj")
        print(s)

        # Create Material and set color and blending
        self.mat = Material()
        self.mat.colour = (self.c, self.c, self.c, 1.0)

        # Create Texture
        self.texture = Texture("test/rep_inf_ep3trooper.png")

        # Create GameObject and add components
        self.obj = GameObject()
        self.obj.add_component(s)
        self.obj.add_component(self.mat)
        self.obj.add_component(self.texture)

        # Add GameObject to scene
        self.add_game_object(self.obj)

    def on_update(self):
        super().on_update()

        self.c += self.engine.dt / 10000

        # Update color and blend factor
        self.mat.blend = 0.7
        self.mat.colour = (self.c, self.c, self.c, 1.0)  # Gradually change color


if __name__ == '__main__':
    window_prop = window_data
    window_prop[WINDOW_ICON] = "test/Icon.png"
    window_prop[WINDOW_TITLE] = "Test Engine 123123"

    log_to_console(LogLevel.INFO,"Hello World INFO")
    log_to_console(LogLevel.WARNING,"Hello World Warning",bold=True)
    log_to_console(LogLevel.ERROR,"Hello World ERROR")
    log_to_console(LogLevel.DEBUG,"Hello World DEBUG",bold=True)

    engine = Engine(debug=True)

    engine.scene_manager.add_scene("test",Test())

    engine.run()
