from mothic import Scene, colors, director, Surface, keys, etypes
from mothic.visuals import text

from ui.button import Button


class SettingsScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = director.settings['surface_size'][0] // 2
        
        self.cake.insert_many([
            Button("Reset Progress", (160, 60), center=(centerx, 260), onclick=self.reset_data),
            Button("Return", (160, 60), center=(centerx, 340), onclick=lambda: director.set_scene("MainMenuScene"))
        ])

    def handle_events(self, events):
        self.cake.handle_events(events)

        for event in events:
            if event.type == etypes.KEYDOWN:
                if event.key == keys.K_ESCAPE:
                    director.set_scene("MainMenuScene")

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        surf, rect = text.render("SOKOBAN", colors.black, "The Last Shuriken", 48, True)
        rect.center = surface.get_rect().centerx, 130
        surface.blit(surf, rect)

        surf, rect = text.render("Settings", colors.black, "The Last Shuriken", 24, True)
        rect.center = surface.get_rect().centerx, 180
        surface.blit(surf, rect)

        self.cake.render(surface)

    @staticmethod
    def reset_data():
        with open('resources/levels/completed.txt', 'w') as file:
            file.write('000000000')
