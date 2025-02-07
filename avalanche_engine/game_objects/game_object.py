from avalanche_engine.config import *

class GameObject:
    def __init__(self):
        self.engine = None
        self.scene = None
        self.ctx = None

        self.components = {}

    def add_component(self,comp_type,component):
        if comp_type not in self.components:
            self.components[comp_type] = component

    def get_component(self,comp_type):
        if comp_type in self.components:
            return self.components[comp_type]

    def create(self):
        pass

    def event_handler(self,event):
        pass

    def update(self):
        for component in self.components.values():
            component.update()

    def render(self):
        for component in self.components.values():
            component.render()

    def close(self):
        for component in self.components.values():
            component.close()