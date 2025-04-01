import pygame
from pygame import Rect

from mothic import Thing, draw, colors
from mothic.visuals import text

from typing import Callable


class Button(Thing):
    def __init__(self, label, size, center, color=colors.black, onclick: Callable=None):
        super().__init__(
            rect=Rect(0, 0, *size),
            default_render_layer=99
        )

        self.rect.center = center

        self.image.fill(colors.beige)
        draw.rect(self.image, color, (0, 0, *self.rect.size), 3, 5)

        surf, rect = text.render(label, colors.black, "Arial", 18)
        rect.center = self.rect.width / 2, self.rect.height / 2
        self.image.blit(surf, rect)

        self.onclick = onclick

    def handle_events(self, events, **kwargs):
        mouse = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.onclick is not None and self.rect.collidepoint(*mouse):
                    self.onclick()
