from ..components.transform import Transform
from ..config import *
from ..components.component import Component
from ..components.transform import Transform

class GameObject:
    def __init__(self):
        self.engine = None
        self.scene = None
        self.initialised = False

        self.components = {}
        self.components_to_create = {}

        self.transform = Transform()
        self.add_component(self.transform)


    def on_create(self):
        self.initialised = True

        for component in self.components_to_create.values():
            self.add_component(component)

    def add_component(self,component):
        if self.initialised:
            component.engine = self.engine
            component.scene = self.scene
            component.on_create()

            self.components[component.type] = component
        else:
            self.components_to_create[component.type] = component


    def on_update(self):
        for component in self.components.values():
            component.on_update()

    def on_render(self):
        for component in self.components.values():
            component.on_render()

    def on_close(self):
        for component in self.components.values():
            component.on_close()