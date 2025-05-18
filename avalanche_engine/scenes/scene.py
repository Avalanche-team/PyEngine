from avalanche_engine.game_objects.shader import Shader


class Scene:
    def __init__(self):
        self.engine = None

        self.game_object = []
        self.game_objects_to_create = []

        self.shader = None

        self.initialised = False

    def on_event(self,event):
        pass

    def on_create(self):
        self.initialised = True

        self.shader = Shader()
        self.add_game_object(self.shader)

        for game_object in self.game_objects_to_create:
            self.add_game_object(game_object)

    def add_game_object(self, game_object):
        if self.initialised:
            game_object.engine = self.engine
            game_object.scene = self
            game_object.on_create()

            self.game_object.append(game_object)
        else:
            self.game_objects_to_create.append(game_object)

    def on_update(self):
        for component in self.game_object:
            component.on_update()

    def on_render(self):
        for component in self.game_object:
            component.on_render()

    def on_close(self):
        for component in self.game_object:
            component.on_close()