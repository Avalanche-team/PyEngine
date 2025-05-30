# PyEngine

![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/Avalanche-team/PyEngine?utm_source=oss&utm_medium=github&utm_campaign=Avalanche-team%2FPyEngine&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)
 
### steps to create a window
```python
from avalanche_engine import *

# this creates the engine that is the entry point of the whole project
# debug is automatically set to 'False' and allows you to see the project speeds on the title
# debug can be set in the system arguments with '--debug'
engine = Engine(debug=True)

# gets the window data and overrides the default values 
window_props = window_data
window_props[WINDOW_ICON] = "path/to/icon/image"
window_props[WINDOW_TITLE] = "Window Title"

# updates, renders and checks for closing the windows 
engine.run()
```

### the entity component system
**Scenes** class is an example of a world or a level in a game,
create a class that parents **Scenes** if we have multiple scenes use the engine to swap scenes

**Game Object** is an example of a player or enemies or tiles.

**Component** have premade classes that can be used to move and render the game objects but can 
also be used to create custom components to create special effects

### steps to add a 3D model
```python

# make sure all classes that need to be scenes parent the 
# Scene Class in avalanche_engine 

class Test(Scene): 
    def __init__(self):
        super().__init__()
        
        # this is not needed but would be good to make 
        # pre-defined variables to stop warnings
        
        self.mat = None
        self.texture = None
        self.obj = None

    def on_create(self):
        super().on_create() # <- always make sure to super on a built in function

        # texture holds the pixel data width and height and channels
        self.texture = Texture("path/to/texture.png")
        
        # will hold the base colour, texture and the blend between 
        # the base coloue and texture
        self.mat = Material()
        self.mat.set_diffuse_map(self.texture) # <- adds texture to the material


        mesh = load_obj_model("paht/to/model.obj") # <- loads a obj model 

        self.obj = GameObject()
        
        # adds components to the game object, one component can be added to multiple 
        # Game objects aswell
        self.obj.add_component(mesh) 
        self.obj.add_component(self.mat)

        
        self.add_game_object(self.obj) # <- adds game object to the scene

if __name__ == '__main__':
    window_prop = window_data
    window_prop[WINDOW_TITLE] = "Test Engine"

    engine = Engine(debug=True)

    # make sure to set the starter scene or else just a window will display
    engine.scene_manager.add_scene("test",Test()) 

    engine.run()
```
## Possible Problems
* make sure all overriding functions have "super().function_name" overridable functions are on_create(), on_event(event), on_render(), on_update(), on_close()
