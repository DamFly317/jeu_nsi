import pygame
from settings import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, *groups, z=0):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy()


class Coin(Generic):
    def __init__(self, pos, *groups):
        super().__init__(
            (0, 0),
            pygame.transform.scale(pygame.image.load('graphics/coin.png'), (50, 50)),
            *groups,
            z=LAYERS[0]['Main']
        )
        self.rect.center = pos
        self.hitbox = self.rect.copy()
