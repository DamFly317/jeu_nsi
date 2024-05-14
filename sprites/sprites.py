import pygame
from settings import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, *groups, z=0):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy()


class LabyrinthWall(Generic):
    def __init__(self, pos, surf, *groups):
        super().__init__(
            pos,
            surf,
            *groups,
            z=LAYERS[1]['Main']
        )
        self.test = True
        self.hitbox = self.hitbox.inflate(-12, -12)


class Coin(Generic):
    def __init__(self, pos, *groups):
        super().__init__(
            pos,
            pygame.transform.scale(pygame.image.load('graphics/coin.png'), (50, 50)),
            *groups,
            z=LAYERS[1]['Main']
        )
