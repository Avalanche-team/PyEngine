from .config import *

WINDOW_WIDTH = "window width"
WINDOW_HEIGHT = "window height"
WINDOW_TITLE = "window title"
WINDOW_VSYNC = "window vsync"
WINDOW_POSITION_X = "window position x"
WINDOW_POSITION_Y = "window position y"
WINDOW_FULLSCREEN = "window fullscreen"
WINDOW_BORDERLESS = "window borderless"
WINDOW_RESIZABLE = "window resizable"
WINDOW_BACKGROUND_COLOUR = "window background colour"
WINDOW_ICON = "window icon"

window_data = {
    WINDOW_WIDTH: 1080,
    WINDOW_HEIGHT: 720,
    WINDOW_TITLE: "Avalanche Engine",
    WINDOW_VSYNC: True,
    WINDOW_BACKGROUND_COLOUR:(0.1,0.4,0.8,1.0),
    WINDOW_POSITION_X: None,
    WINDOW_POSITION_Y: None,
    WINDOW_FULLSCREEN: False,
    WINDOW_BORDERLESS: False,
    WINDOW_RESIZABLE: False,
    WINDOW_ICON: None,
}

class Window:
    def __init__(self,engine):
        self.engine = engine

        flags = pg.OPENGL | pg.DOUBLEBUF
        self.window_data = window_data

        self.engine_dir = os.path.abspath(os.path.dirname(__file__))

        if self.window_data[WINDOW_FULLSCREEN]:
            flags |= pg.FULLSCREEN
        if self.window_data[WINDOW_BORDERLESS]:
            flags |= pg.NOFRAME
        if self.window_data[WINDOW_RESIZABLE]:
            flags |= pg.RESIZABLE


        pg.display.set_mode(
        (self.window_data[WINDOW_WIDTH],self.window_data[WINDOW_HEIGHT]),
            flags=flags,
            depth=0,
            display=0,
            vsync=self.window_data[WINDOW_VSYNC]
            )
        pg.display.set_caption(self.window_data[WINDOW_TITLE])

        if self.window_data[WINDOW_ICON]:
            icon = pg.image.load(self.window_data[WINDOW_ICON]).convert_alpha()
            pg.display.set_icon(icon)

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)


        self.running = True

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        pass

    def get_size(self):
        return pg.display.get_surface().get_size()

    def start_window(self):
        self.engine.ctx.clear(*self.window_data[WINDOW_BACKGROUND_COLOUR])

    def render(self):
        pg.display.flip()
