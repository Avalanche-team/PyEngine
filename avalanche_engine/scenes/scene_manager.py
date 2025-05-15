from ..config import *
from .scene import Scene

class SceneManager:
    def __init__(self,engine):
        self.engine = engine

        self.scenes = {}
        self.selected_scene = None

    def add_scene(self,name,scene):
        if isinstance(scene,Scene):
            self.scenes[name] = scene
            scene.engine = self.engine
            scene.on_create()

            if not self.selected_scene:
                self.selected_scene = name

    def get_scene(self,name) -> Scene:
        return self.scenes.get(name,None)

    def on_event(self,event):
        if self.scenes.get(self.selected_scene,False):
            self.scenes[self.selected_scene].on_event(event)

    def on_update(self):
        if self.scenes.get(self.selected_scene,False):
            self.scenes[self.selected_scene].on_update()

    def on_render(self):
        if self.scenes.get(self.selected_scene, False):
            self.scenes[self.selected_scene].on_render()

    def on_close(self):
        if self.scenes.get(self.selected_scene,False):
            self.scenes[self.selected_scene].on_close()
