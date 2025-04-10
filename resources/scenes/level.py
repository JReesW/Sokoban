import pygame  # TODO: add blend modes to mothic

from mothic import Scene, colors, director, Surface, etypes, keys
from mothic.visuals import text
from mothic.dsa.cake import Cake

from things import load_level, Wall, Box, Goal


class LevelScene(Scene):
    def __init__(self, level):
        super().__init__()

        self.things = None
        self.level = level
        self.state = self.init_state()
        self.box_colors()
        
    def handle_events(self, events):
        for event in events:
            if event.type == etypes.KEYDOWN:
                if event.key == keys.K_w or event.key == keys.K_UP:
                    self.move(0, -1)
                elif event.key == keys.K_a or event.key == keys.K_LEFT:
                    self.move(-1, 0)
                elif event.key == keys.K_s or event.key == keys.K_DOWN:
                    self.move(0, 1)
                elif event.key == keys.K_d or event.key == keys.K_RIGHT:
                    self.move(1, 0)
                elif event.key == keys.K_r:
                    self.state = self.init_state()
                elif event.key == keys.K_ESCAPE:
                    director.set_scene("LevelSelectScene")

    def update(self):
        self.cake.update()

    def render(self, surface: Surface):
        surface.fill(colors.beige)

        self.cake.render(surface)

    def init_state(self):
        self.things, divided = load_level(self.level)
        boxes, goals, players, walls = divided
        player = players[0]

        self.cake = Cake()
        for thing in self.things:
            self.cake.insert(thing)

        return {
            "boxes": boxes,
            "goals": goals,
            "player": player,
            "walls": walls
        }

    def find_at_pos(self, x, y):
        for thing in self.things:
            if thing.coords == (x, y):
                return thing
    
    def check_win(self):
        goal_coords = {goal.coords for goal in self.state["goals"]}
        box_coords = {box.coords for box in self.state["boxes"]}

        if len(goal_coords - box_coords) == 0:
            director.set_scene("WinScene", self)
    
    def box_colors(self):
        goal_coords = {goal.coords for goal in self.state["goals"]}
        for box in self.state["boxes"]:
            if box.coords in goal_coords:
                box.image.fill((*colors.green, 0), special_flags=pygame.BLEND_RGBA_MAX)
            else:
                box.reset_image()
    
    def move(self, dx, dy):
        pos = self.state["player"].coords

        pos1 = pos[0] + dx, pos[1] + dy
        pos2 = pos1[0] + dx, pos1[1] + dy
        found1 = self.find_at_pos(*pos1)
        found2 = self.find_at_pos(*pos2)

        if isinstance(found1, Box) and (isinstance(found2, Goal) or found2 is None):
            found1.reposition(pos2)
            self.state["player"].reposition(pos1)
        elif found1 is None or isinstance(found1, Goal):
            self.state["player"].reposition(pos1)

        self.box_colors()
        self.check_win()        
