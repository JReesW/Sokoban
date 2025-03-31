import pygame
from pygame import Surface, display

from mothic import Scene, colors, director
from mothic.visuals import text

from ui.button import Button


class SettingsScene(Scene):
    def __init__(self):
        super().__init__()

        centerx = display.get_surface().get_rect().centerx

        from scenes.main_menu import MainMenuScene
        
        self.cake.insert_many([
            Button("Reset Progress", (200, 60), center=(centerx, 400)).set_func(self.reset_data),
            Button("Return", (200, 60), center=(centerx, 600)).set_func(director.set_scene_uninitialized, MainMenuScene)
        ])

    def handle_events(self, events):
        self.cake.handle_events(events)

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        surf, rect = text.render("SOKOBAN", colors.black, "Arial", 48, True)
        rect.center = surface.get_rect().centerx, 150
        surface.blit(surf, rect)

        surf, rect = text.render("Settings", colors.black, "Arial", 24, True)
        rect.center = surface.get_rect().centerx, 200
        surface.blit(surf, rect)

        self.cake.render(surface)
    
    def reset_data(self):
        with open('resources/levels/completed.txt', 'w') as file:
            file.write('000000000')
