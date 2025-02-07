from avalanche_engine import *


class Test(Scene):
    def __init__(self):
        super().__init__()

        mesh = Mesh()

        player = GameObject()
        player.add_component(Type.MESH,mesh)

        self.add_game_object(player)


if __name__ == '__main__':
    engine = Engine()
    engine.scene_manager.add_scene("test",Test())
    engine.run()