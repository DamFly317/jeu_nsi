import os

import pygame.image

from settings import *
from ui import Inventory
from debug import debug


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, collision_sprites, *groups):
        self.game = game
        super().__init__(*groups)

        self.pos = pygame.math.Vector2(x*4, y*4)
        self.speed = 300
        self.direction = 'down'
        self.action = 'idle'

        self.collision_sprites = collision_sprites

        self.slots_number = 6
        self.inventory = Inventory(self.slots_number)

        self.frame_index = 0
        self.animation_frames = {}
        self.load_animations()

        self.image = self.animation_frames[self.action][self.direction][self.frame_index]
        self.rect = self.image.get_rect()
        self.z = LAYERS[self.game.world]['Main']
        self.hitbox = self.rect.copy().inflate(-126, -70)

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
        self.collide()
        self.animate()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide(self):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction == 'right':
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction == 'left':
                        self.hitbox.left = sprite.hitbox.right
                    if self.direction == 'up':
                        self.hitbox.top = sprite.hitbox.bottom
                    if self.direction == 'down':
                        self.hitbox.bottom = sprite.hitbox.top

                    self.rect.center = self.hitbox.center
                    self.pos.x = self.rect.centerx
                    self.pos.y = self.rect.centery

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

        self.rect.centerx = round(self.pos.x)
        self.rect.centery = round(self.pos.y)
        self.hitbox.center = self.pos

    def animate(self):
        self.frame_index += 3 * self.game.dt
        self.frame_index = self.frame_index % len(self.animation_frames[self.action][self.direction])

        self.image = self.animation_frames[self.action][self.direction][int(self.frame_index)]
