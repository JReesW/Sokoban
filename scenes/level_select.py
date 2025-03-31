import pygame
from pygame import Surface, display

from mothic import Scene, colors, director
from mothic.visuals import text

from ui.button import Button
from scenes.level import LevelScene


class LevelSelectScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = display.get_surface().get_rect().centerx

        with open('resources/levels/completed.txt', 'r') as file:
            completed = [int(c) for c in file.readline().strip()]

        for x in range(-1, 2):
            for y in range(-1, 2):
                level = (y+1)*3+(x+1)+1
                color = colors.lime if completed[level - 1] else colors.black

                self.cake.insert(
                    Button(str(level), (80, 80), (centerx + x*150, 500 + y*150), color).set_func(director.set_scene_uninitialized, LevelScene, level)
                )
        
        from scenes.main_menu import MainMenuScene
        self.cake.insert(
            Button("Return to Menu", (200, 60), (centerx, 800)).set_func(director.set_scene_uninitialized, MainMenuScene)
        )

    def handle_events(self, events):
        self.cake.handle_events(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from scenes import MainMenuScene
                    director.set_scene(MainMenuScene())

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        surf, rect = text.render("SOKOBAN", colors.black, "Arial", 48, True)
        rect.center = surface.get_rect().centerx, 150
        surface.blit(surf, rect)

        surf, rect = text.render("Level Select", colors.black, "Arial", 24, True)
        rect.center = surface.get_rect().centerx, 200
        surface.blit(surf, rect)

        self.cake.render(surface)
