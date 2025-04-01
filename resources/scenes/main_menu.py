from mothic import Scene, colors, director, quit, Surface, display
from mothic.visuals import text

from ui.button import Button


class MainMenuScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = display.get_surface().get_rect().centerx

        self.cake.insert_many([
            Button('Level Select', (200, 60), center=(centerx, 400), onclick=lambda: director.set_scene("LevelSelectScene")),
            Button('Settings', (200, 60), center=(centerx, 500), onclick=lambda: director.set_scene("SettingsScene")),
            Button('Quit', (200, 60), center=(centerx, 600), onclick=quit),
        ])

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        surf, rect = text.render("SOKOBAN", colors.black, "Arial", 48, True)
        rect.center = surface.get_rect().centerx, 150
        surface.blit(surf, rect)

        self.cake.render(surface)
