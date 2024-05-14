import pygame
from settings import *
import os


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


class KeyE(Generic):
    def __init__(self, game, centerx, centery):
        self.size = (50, 50)

        super().__init__(
            pos=(centerx, centery),
            surf=pygame.transform.scale(pygame.image.load('graphics/sprite_e/e0.png'), self.size),
            z=LAYERS[1]['Coins']
        )
        self.rect.center = (centerx, centery)

        self.game = game
        self.frame_index = 0
        self.animation_frames = {}
        self.load_animations()

    def load_animations(self):
        path = 'graphics/sprite_e'
        self.animation_frames = []
        for i in range(len(os.listdir(path))):
            animaton_image = pygame.transform.scale(
                pygame.image.load(path + f'/e{i}.png'), self.size
            ).convert_alpha()
            self.animation_frames.append(animaton_image)

    def animate(self):
        self.frame_index += 15 * self.game.dt
        self.frame_index = self.frame_index % len(self.animation_frames)

        self.image = self.animation_frames[int(self.frame_index)]

