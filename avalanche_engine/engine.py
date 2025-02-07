from .config import *
from .scenes.scene_manager import SceneManager

class Engine:
    win_size:tuple[int,int]
    title:str

    def __init__(self,win_size=(1080,720),title="Avalanche Engine"):
        self.win_size = win_size

        pg.display.set_mode(self.win_size,flags=pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption(title)

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK , pg.GL_CONTEXT_PROFILE_CORE)

        self.ctx = mgl.create_context()

        self.running = True

        self.clock = pg.time.Clock()
        self.fps = 120
        self.dt = 0
        self.time = 0

        self.scene_manager = SceneManager(self)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            self.scene_manager.event_handler(event)

    def render(self):
        self.ctx.clear(0.2,0.4,0.8)

        self.scene_manager.render()

        pg.display.flip()

    def update(self):
        self.dt = self.clock.tick(self.fps) / 1000
        self.fps = self.clock.get_fps()
        self.time = self.clock.get_time()

        self.scene_manager.update()

    def quit(self,status=0):
        self.scene_manager.close()
        pg.quit()
        sys.exit(status)

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()

        self.quit()