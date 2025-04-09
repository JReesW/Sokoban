from mothic import Scene, colors, director, quit, Surface, display, draw, Rect
from mothic.visuals import text

from ui.button import Button


class MainMenuScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = director.settings['surface_size'][0] // 2

        self.cake.insert_many([
            Button('Level Select', (160, 60), center=(centerx, 230), onclick=lambda: director.set_scene("LevelSelectScene")),
            Button('Settings', (160, 60), center=(centerx, 310), onclick=lambda: director.set_scene("SettingsScene")),
            Button('Quit', (160, 60), center=(centerx, 390), onclick=quit),
        ])

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        surf, rect = text.render("SOKOBAN", colors.black, "The Last Shuriken", 48, True)
        rect.center = surface.get_rect().centerx, 130
        surface.blit(surf, rect)

        self.cake.render(surface)
