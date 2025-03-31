from mothic.media.image import load_image
from things import Pushable


class Wall(Pushable):
    def __init__(self, center, coords, gens):
        super().__init__(center, coords, gens)

        self.image = load_image('wall')
        self._image = load_image('wall')
