from ..config import *
from .scene import Scene

class SceneManager:
    def __init__(self,engine):
        self.engine = engine

        self.scenes = {}
        self.selected_scene = None

    def on_create(self):
        pass

    def on_event(self, event):
        pass

    def add_scene(self,name,scene):
        scene.engine = self.engine
        scene.on_create()

        if self.selected_scene is None:
            self.selected_scene = name

        self.scenes[name] = scene

    def on_update(self):
        if self.selected_scene:
            self.scenes[self.selected_scene].on_update()

    def on_render(self):
        if self.selected_scene:
            self.scenes[self.selected_scene].on_render()

    def on_close(self):
        for scene in self.scenes.values():
            scene.on_close()