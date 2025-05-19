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



        s = load_obj_model("test/wanwan.obj")

        # Create Material and set color and blending
        self.mat = Material()

        # Create Texture
        self.texture = Texture("test/ob_wan_body.png")
        self.mat.set_diffuse_map(self.texture)

        # Set different textures or materials for each object
        self.texture1 = Texture("test/ob_wan_body.png")
        self.mat1 = Material()
        self.mat1.set_diffuse_map(self.texture1)

        self.texture2 = Texture("test/ob_wan_body.png")
        self.mat2 = Material()
        self.mat2.set_diffuse_map(self.texture2)

        # Create first GameObject with different material
        self.obj = GameObject()
        self.obj.add_component(s)
        self.obj.add_component(self.mat1)
        self.obj.transform.position.x = 2

        # Create second GameObject with different material
        self.obj2 = GameObject()
        self.obj2.add_component(s)
        self.obj2.add_component(self.mat2)
        self.obj2.transform.position.x = 1

        # Add GameObject to scene
        self.add_game_object(self.obj2)

        print(f"Obj position: {self.obj.transform.position.x}")  # Debug obj position
        print(f"Obj2 position: {self.obj2.transform.position.x}")  # Debug obj2 position

    def on_update(self):
        super().on_update()

        self.obj.transform.position.x += 1 * self.engine.dt



if __name__ == '__main__':
    window_prop = window_data
    window_prop[WINDOW_ICON] = "test/Icon.png"
    window_prop[WINDOW_TITLE] = "Test Engine"

    engine = Engine(debug=True)

    engine.scene_manager.add_scene("test",Test())

    engine.run()
