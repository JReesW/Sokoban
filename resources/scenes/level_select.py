import pygame

from mothic import Scene, colors, director, Surface, keys, etypes
from mothic.visuals import text

from ui.button import Button


class LevelSelectScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = director.settings['surface_size'][0] // 2

        with open('resources/levels/completed.txt', 'r') as file:
            completed = [int(c) for c in file.readline().strip()]

        for x in range(-1, 2):
            for y in range(-1, 2):
                level = (y+1)*3+(x+1)+1
                color = colors.lime if completed[level - 1] else colors.black

                self.cake.insert(
                    Button(str(level), (65, 65), (centerx + x*90, 350 + y*90), color, onclick=lambda l=level: director.set_scene("LevelScene", l))
                )
        
        self.cake.insert(
            Button("Return to Menu", (200, 60), (centerx, 800), onclick=lambda: director.set_scene("MainMenuScene"))
        )

    def handle_events(self, events):
        self.cake.handle_events(events)

        for event in events:
            if event.type == etypes.KEYDOWN:
                if event.key == keys.K_ESCAPE:
                    director.set_scene("MainMenuScene")

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        surf, rect = text.render("SOKOBAN", colors.black, "The Last Shuriken", 48, True)
        rect.center = surface.get_rect().centerx, 130
        surface.blit(surf, rect)

        surf, rect = text.render("Level Select", colors.black, "The Last Shuriken", 24, True)
        rect.center = surface.get_rect().centerx, 180
        surface.blit(surf, rect)

        self.cake.render(surface)
