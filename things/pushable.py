from mothic import Thing


class Pushable(Thing):
    def __init__(self, center, coords, gens):
        super().__init__()

        self.rect.center = center
        self.coords = coords
        self.xgen, self.ygen = gens

        self.default_render_layer = 1
