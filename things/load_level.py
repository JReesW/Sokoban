from mothic import director
from things import Box, Player, Wall, Goal


def load_level(level):
    players = []
    walls = []
    goals = []
    boxes = []

    size = director.settings["surface_size"]
    center = size[0] // 2, size[1] // 2

    with open(f'resources/levels/level{level}.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        width = len(lines[0])
        height = len(lines)

        xgen = lambda x: (x - width//2) * 37 + center[0] - (21 if width % 2 else 0)
        ygen = lambda y: (y - height//2) * 37 + center[1]

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                xp = xgen(x)
                yp = ygen(y)

                if char == 'X':
                    walls.append(Wall((xp, yp), (x, y), (xgen, ygen)))
                elif char == 'B':
                    boxes.append(Box((xp, yp), (x, y), (xgen, ygen)))
                elif char == 'G':
                    goals.append(Goal((xp, yp), (x, y), (xgen, ygen)))
                elif char == 'P':
                    players.append(Player((xp, yp), (x, y), (xgen, ygen)))
                elif char == 'C':
                    boxes.append(Box((xp, yp), (x, y), (xgen, ygen)))
                    goals.append(Goal((xp, yp), (x, y), (xgen, ygen)))

    things = [*boxes, *goals, *players, *walls]
    return things, (boxes, goals, players, walls)
