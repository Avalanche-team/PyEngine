from avalanche_engine import *


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

        # Create Material and set color and blending
        self.mat = Material()
        self.mat.colour = (self.c, self.c, self.c, 1.0)

        # Create Texture
        self.texture = Texture("test/Icon.png")

        # Create GameObject and add components
        self.obj = GameObject()
        self.obj.add_component(self.square)
        self.obj.add_component(self.mat)
        self.obj.add_component(self.texture)

        # Add GameObject to scene
        self.add_game_object(self.obj)

    def on_update(self):
        super().on_update()

        # Update color and blend factor
        self.mat.blend = 0.7
        self.mat.colour = (self.c, self.c, self.c, 1.0)  # Gradually change color


if __name__ == '__main__':
    window_prop = window_data
    window_prop[WINDOW_ICON] = "test/Icon.png"
    window_prop[WINDOW_TITLE] = "Test Engine 123123"

    engine = Engine()

    engine.scene_manager.add_scene("test",Test())

    engine.run()
