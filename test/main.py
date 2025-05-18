from avalanche_engine import *

class Test(Scene):
    def __init__(self):
        super().__init__()

        self.square = None

        self.obj = None


    def on_create(self):
        super().on_create()

        self.square = get_square_mesh()
        self.obj = GameObject()
        self.obj.add_component(self.square)

        self.add_game_object(self.obj)

if __name__ == '__main__':
    window_prop = window_data
    window_prop[WINDOW_ICON] = "test/Icon.png"
    window_prop[WINDOW_TITLE] = "Test Engine 123123"

    engine = Engine()

    engine.scene_manager.add_scene("test",Test())

    engine.run()
