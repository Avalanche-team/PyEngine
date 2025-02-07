from ..config import *

class SceneManager:
    def __init__(self,engine):
        self.engine = engine

        self.scenes = {}
        self.selected_scene = None


    def add_scene(self,name,scene):
        if name not in self.scenes:
            if len(self.scenes) == 0:
                self.selected_scene = name

            scene.engine = self.engine
            scene.ctx = self.engine.ctx

            scene.create()

            self.scenes[name] = scene

    def event_handler(self,event):
        if self.selected_scene:
            self.scenes[self.selected_scene].event_handler(event)

    def render(self):
        if self.selected_scene:
            self.scenes[self.selected_scene].render()

    def update(self):
        if self.selected_scene:
            self.scenes[self.selected_scene].update()

    def close(self):
        for scene in self.scenes.values():
            scene.close()