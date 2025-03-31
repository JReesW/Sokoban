from mothic.media.image import load_image
from things import Pushable


class Goal(Pushable):
    def __init__(self, center, coords, gens):
        super().__init__(center, coords, gens)

        self.image = load_image('goal')
        self._image = load_image('goal')

        self.default_render_layer = 0
