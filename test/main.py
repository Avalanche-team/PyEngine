from avalanche_engine import *
import math

class Test(Scene):
    def __init__(self):
        super().__init__()

        self.mat = None
        self.texture = None
        self.obj = None

        self.player_1_x = 0

    def on_create(self):
        super().on_create()

        self.texture = Texture("test/rep_inf_ep3trooper.png")
        self.mat = Material()
        self.mat.set_diffuse_map(self.texture)


        mesh = load_obj_model("test/rep_inf_ep3trooper.obj")

        self.obj = GameObject()
        self.obj.add_component(mesh)
        self.obj.add_component(self.mat)

        self.obj2 = GameObject()
        self.obj2.add_component(mesh)
        self.obj2.add_component(self.mat)

        self.obj2.transform.position.z = 2


        self.add_game_object(self.obj)
        self.add_game_object(self.obj2)

    def on_update(self):
        super().on_update()
        self.player_1_x +=  self.engine.dt

        self.obj.transform.rotation.y = self.player_1_x
        self.obj.transform.position.y = math.sin(self.player_1_x)

        self.obj2.transform.rotation.z = self.player_1_x




if __name__ == '__main__':
    window_prop = window_data
    window_prop[WINDOW_ICON] = "test/Icon.png"
    window_prop[WINDOW_TITLE] = "Test Engine"

    engine = Engine(debug=True)

    engine.scene_manager.add_scene("test",Test())

    engine.run()
