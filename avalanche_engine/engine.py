from .config import *
from .window import Window
from .scenes.scene_manager import SceneManager

class Engine:
    def __init__(self,debug=False):
        self.debug = debug

        self.active_window = Window(self)
        self.ctx = mgl.create_context()

        self.scene_manager = SceneManager(self)

        self.clock = pg.Clock()

        self.ctx.enable(mgl.BLEND)
        self.ctx.blend_func = mgl.SRC_ALPHA, mgl.ONE_MINUS_SRC_ALPHA

        self.dt = 0
        self.time = 0


    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active_window.running = False

            self.scene_manager.on_event(event)

    def update(self):
        self.dt = self.clock.tick(60)

        self.scene_manager.on_update()
        self.active_window.update()

    def render(self):
        self.active_window.start_window()
        self.scene_manager.on_render()
        self.active_window.render()


    def close(self):
        self.scene_manager.on_close()
        self.active_window.quit()

    def run(self):
        while self.active_window.running:
            self.event_handler()
            self.update()
            self.render()
        self.close()