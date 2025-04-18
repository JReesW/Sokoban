from mothic import Scene, colors, director, Surface
from mothic.visuals import text


class WinScene(Scene):
    def __init__(self, bg_scene):
        super().__init__()

        self.bg_scene = bg_scene

        self.time_left = 90

        with open('resources/levels/completed.txt', 'r') as file:
            completed = [int(c) for c in file.readline().strip()]
        completed[self.bg_scene.level - 1] = 1
        with open('resources/levels/completed.txt', 'w') as file:
            file.write(''.join([str(c) for c in completed]))

    def handle_events(self, events):
        self.cake.handle_events(events)

    def update(self):
        self.time_left -= 1
        if self.time_left == 0:
            director.set_scene("LevelSelectScene")

    def render(self, surface: Surface):
        self.bg_scene.render(surface)

        surf, rect = text.render("LEVEL COMPLETE", colors.black, "The Last Shuriken", 48, True)
        rect.center = surface.get_rect().centerx, 80
        surface.blit(surf, rect)

        self.cake.render(surface)
