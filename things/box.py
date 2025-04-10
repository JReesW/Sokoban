from mothic.media.image import load_image
from things import Pushable


class Box(Pushable):
    def __init__(self, center, coords, gens):
        super().__init__(center, coords, gens)

        self.image = load_image('box')
        self._image = load_image('box')

    def reset_image(self):
        self.image = self._image.copy()
