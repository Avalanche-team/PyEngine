from avalanche_engine import *
import math

class TestWorld(Scene):
    def __init__(self):
        super().__init__()

        self.trooper = None

    def on_create(self):
        super().on_create()
        self.mesh = load_obj_model("test/rep_inf_ep3trooper.obj")
        self.texture = Texture("test/rep_inf_ep3trooper.png")

        self.mat = Material()
        self.mat.set_diffuse_map(self.texture)
        self.mat.blend = 0.25

        self.trooper = GameObject()
        self.trooper.add_component(self.mat)
        self.trooper.add_component(self.mesh)

        self.add_game_object(self.trooper)

        self.player_y = 0

    def on_update(self):
        super().on_update()
        self.player_y += self.engine.dt * 2

        self.trooper.transform.position.y = math.sin(self.player_y)
        self.trooper.transform.rotation.y = self.player_y


if __name__ == '__main__':

    window_data[WINDOW_TITLE] = "Test Game 1234"
    window_data[WINDOW_ICON] = "test/Icon.png"
    window_data[WINDOW_BACKGROUND_COLOUR] = (0.8, 0.8, 1.0)

    engine = Engine(debug=True)

    engine.scene_manager.add_scene("test",TestWorld())

    engine.run()
