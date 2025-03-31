import pygame
from pygame import Surface, display

from mothic import Scene, colors, director
from mothic.visuals import text

from ui.button import Button
from scenes.level_select import LevelSelectScene
from scenes.settings import SettingsScene


class MainMenuScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = display.get_surface().get_rect().centerx

        self.cake.insert_many([
            Button('Level Select', (200, 60), center=(centerx, 400)).set_func(director.set_scene_uninitialized, LevelSelectScene),
            Button('Settings', (200, 60), center=(centerx, 500)).set_func(director.set_scene_uninitialized, SettingsScene),
            Button('Quit', (200, 60), center=(centerx, 600)).set_func(pygame.quit),
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
