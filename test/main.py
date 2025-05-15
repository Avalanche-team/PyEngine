from avalanche_engine import *

class Test(Scene):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    window_prop = window_data
    window_prop[WINDOW_ICON] = "test/Icon.png"
    window_prop[WINDOW_TITLE] = "Test Engine 123123"

    engine = Engine()

    engine.scene_manager.add_scene("test",Test())

    engine.run()
