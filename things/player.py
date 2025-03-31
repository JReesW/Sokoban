from mothic.media.image import load_image
from things import Pushable


class Player(Pushable):
    def __init__(self, center, coords, gens):
        super().__init__(center, coords, gens)

        self.image = load_image('player')
        self._image = load_image('player')
