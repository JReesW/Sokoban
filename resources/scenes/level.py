import pygame

from mothic import Scene, colors, director, Surface
from mothic.visuals import text
from mothic.dsa.cake import Cake

from things import load_level, Wall, Box


class LevelScene(Scene):
    def __init__(self, level):
        super().__init__()

        self.level = level
        self.init_state()
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.move(0, -1)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.move(-1, 0)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.move(0, 1)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.move(1, 0)
                elif event.key == pygame.K_r:
                    self.init_state()
                elif event.key == pygame.K_ESCAPE:
                    director.set_scene("LevelSelectScene")

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        surf, rect = text.render("SOKOBAN", colors.black, "Arial", 48, True)
        rect.center = surface.get_rect().centerx, 150
        surface.blit(surf, rect)

        self.cake.render(surface)

    def init_state(self):
        self.things, divided = load_level(self.level)
        self.boxes, self.goals, self.players, self.walls = divided
        self.player = self.players[0]

        self.cake = Cake()
        for thing in self.things:
            self.cake.insert(thing)
        
        self.box_colors()

    def find_at_pos(self, x, y):
        for thing in self.things:
            if thing.coords == (x, y):
                return thing
    
    def check_win(self):
        goal_coords = {goal.coords for goal in self.goals}
        box_coords = {box.coords for box in self.boxes}

        if len(goal_coords - box_coords) == 0:
            director.set_scene("WinScene", self)
    
    def box_colors(self):
        goal_coords = {goal.coords for goal in self.goals}
        for box in self.boxes:
            if box.coords in goal_coords:
                box.image.fill((*colors.green, 0), special_flags=pygame.BLEND_RGBA_MAX)
            else:
                box.image = box._image.copy()
    
    def move(self, dx, dy):
        stack = [self.player]
        pos = self.player.coords

        while True:
            pos = pos[0] + dx, pos[1] + dy
            found = self.find_at_pos(*pos)

            if isinstance(found, Wall):
                return
            elif isinstance(found, Box):
                stack.append(found)
            else:
                break

        for thing in stack:
            thing.coords = thing.coords[0] + dx, thing.coords[1] + dy
            x, y = thing.coords
            thing.rect.center = thing.xgen(x), thing.ygen(y)

        self.box_colors()
        self.check_win()        
