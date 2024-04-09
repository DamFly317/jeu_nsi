import os

import pygame.image

from settings import *
from ui import Inventory
from debug import debug


class Player(pygame.sprite.Sprite):
    def __init__(self, game, *groups):
        self.game = game
        super().__init__(*groups)

        self.pos = pygame.math.Vector2(1000, 1000)
        self.speed = 300
        self.inventory = Inventory()

        self.direction = 'down'
        self.action = 'idle'
        self.frame_index = 0
        self.animation_frames = {}
        self.load_animations()

        self.image = self.animation_frames[self.action][self.direction][self.frame_index]
        self.rect = self.image.get_rect()
        self.z = LAYERS['main']

    def load_animations(self):
        path = 'graphics/player/'
        for state in ('walk', 'idle'):
            self.animation_frames[state] = {}
            for direction in ('down', 'up', 'right', 'left'):
                directory = direction + '_' + state
                frames = []
                for i in range(len(os.listdir(path + directory))):
                    animaton_image = pygame.image.load(
                        path + directory + f'/{i}.png'
                    ).convert_alpha()
                    frames.append(animaton_image)

                self.animation_frames[state][direction] = frames

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.move()
        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        if len(self.game.lifo_direction_key_pressed) > 0:
            self.action = 'walk'
            distance = self.speed * self.game.dt
            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_UP:
                self.pos.y -= distance
                self.direction = 'up'
            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_DOWN:
                self.pos.y += distance
                self.direction = 'down'
            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_LEFT:
                self.pos.x -= distance
                self.direction = 'left'
            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_RIGHT:
                self.pos.x += distance
                self.direction = 'right'

        else:
            self.action = 'idle'

        self.rect.topleft = self.pos

    def animate(self):
        self.frame_index += 3 * self.game.dt
        self.frame_index = self.frame_index % len(self.animation_frames[self.action][self.direction])

        self.image = self.animation_frames[self.action][self.direction][int(self.frame_index)]
