import os

import pygame.image

from settings import *
from ui import Inventory
from debug import debug


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, collision_group, coin_group, *groups):
        self.game = game
        super().__init__(*groups)

        self.pos = pygame.math.Vector2(x * 4, y * 4)
        self.speed = 300
        self.direction = 'down'
        self.action = 'idle'

        self.collision_group = collision_group
        self.coin_group = coin_group

        self.slots_number = 6
        self.inventory = Inventory(self.slots_number)
        self.coins = 0

        self.frame_index = 0
        self.animation_frames = {}
        self.load_animations()

        self.next_level_rect = pygame.Rect(0, 0, 0, 0)
        self.next_level = 0

        self.image = self.animation_frames[self.action][self.direction][self.frame_index]
        self.rect = self.image.get_rect()
        self.z = LAYERS[self.game.world]['Main']
        self.hitbox = self.rect.copy().inflate(-130, -80)

    def reload(self, x, y, z, collision_group, coin_group, *groups):
        self.pos.x = x
        self.pos.y = y
        self.rect.centerx = round(self.pos.x)
        self.rect.centery = round(self.pos.y)

        self.z = z
        self.collision_group = collision_group
        self.coin_group = coin_group

        for group in groups:
            group.add(self)

        self.load_environement()

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

    def load_environement(self):
        for obj in self.game.gameplay.tmx_data.objects:
            if 'level' in obj.name:
                self.next_level_rect.topleft = (obj.x * 4, obj.y * 4)
                self.next_level_rect.width = obj.width * 4
                self.next_level_rect.height = obj.height * 4
                self.next_level = obj.name[6:]

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        self.move()
        self.collide()
        self.animate()

    def collide(self):
        for sprite in self.collision_group.sprites():
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

        for coin in self.coin_group:
            if coin.hitbox.colliderect(self.hitbox):
                coin.kill()
                self.coins += 1

        if self.next_level_rect.colliderect(self.hitbox):
            self.game.world = int(self.next_level)

            tmx_data = self.game.gameplay.load_map('data/tmx/level_' + str(self.next_level) + '.tmx')
            pos = tmx_data.get_object_by_name('player')
            self.reload(
                pos.x * 4,
                pos.y * 4,
                LAYERS[self.game.world]['Main'],
                self.collision_group,
                self.coin_group,
                self.game.gameplay.all_sprites
            )

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
