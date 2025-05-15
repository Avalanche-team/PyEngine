from ..components.component import Component
from ..config import *

class GameObject:
    def __init__(self):
        """this class is for any custom game objects to inherit"""

        self.engine = None
        self.scene = None

        self.components = {}
        self.initialised = False

    def on_create(self):
        """this function will initialise this class and all the components attached to this object at this moment"""
        self.initialised = True

        for component in self.components.values():
            component.engine = self.engine
            component.scene = self.scene
            component.game_object = self
            component.on_create()

    def add_component(self,component):
        """
        this function will attach the component to this class if the class has already been created it will
        automatically initialise the component
        """

        if isinstance(component,Component):
            if self.initialised:
                component.engine = self.engine
                component.scene = self.scene
                component.game_object = self
                component.on_create()

            self.components[component.type] = component
        else:
            raise ValueError("Make sure the component is instance of class [Component]")

    def on_event(self,event):
        for component in self.components.values():
            component.on_event(event)

    def on_update(self):
        """this function will update every frame and update all the components"""
        for component in self.components.values():
            component.on_update()

    def on_render(self):
        """this function will render every frame and render all the components"""
        for component in self.components.values():
            component.on_render()

    def on_close(self):
        for component in self.components.values():
            component.on_render()