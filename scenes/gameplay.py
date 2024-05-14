import pygame.image
from pytmx.util_pygame import load_pygame
from pytmx.util_pygame import *

from settings import *
from debug import debug
from sprites.sprites import *
from sprites.player import Player


class GamePlay:
    def __init__(self, game):
        self.game = game
        self.all_sprites = CameraGroup(self.game)
        self.collision_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()

        self.letters_e = {}
        self.visible_letters_e = {}

        self.world_width = 0
        self.world_height = 0
        self.tmx_data = self.load_map(f'data/tmx/level_{self.game.level}.tmx')

        player_pos = self.tmx_data.get_object_by_name('player')
        self.player = Player(
            self.game,
            player_pos.x,
            player_pos.y,
            self.collision_group,
            self.coin_group,
            self.all_sprites
        )

    def load_map(self, path):
        self.tmx_data = load_pygame(path)

        self.world_width = self.tmx_data.width * 64
        self.world_height = self.tmx_data.height * 64

        self.all_sprites.empty()
        self.collision_group.empty()
        self.coin_group.empty()

        for obj in self.tmx_data.objects:
            if obj.name == 'collision':
                surf = pygame.Surface((obj.width * 4, obj.height * 4))
                surf.fill('red')
                Generic(
                    (obj.x * 4, obj.y * 4),
                    surf,
                    self.collision_group
                )

            if 'letter_e' in obj.name:
                self.letters_e[obj.name[9:]] = KeyE(self.game, obj.x * 4, obj.y * 4)

        for layer_name in LAYERS[self.game.level].keys():
            try:
                tiles = self.tmx_data.get_layer_by_name(layer_name).tiles()
            except ValueError:
                tiles = []

            for x, y, surf in tiles:
                if layer_name == 'Walls':
                    Generic(
                        (x * 64, y * 64),
                        pygame.transform.scale(surf, (64, 64)),
                        self.all_sprites, self.collision_group,
                        z=LAYERS[self.game.level][layer_name]
                    )
                if layer_name == 'Labyrinth':
                    LabyrinthWall(
                        (x * 64, y * 64),
                        pygame.transform.scale(surf, (64, 64)),
                        self.all_sprites, self.collision_group
                    )
                elif layer_name == 'Coins':
                    Coin(
                        (x * 64, y * 64),
                        self.all_sprites, self.coin_group
                    )
                else:
                    Generic(
                        (x * 64, y * 64),
                        pygame.transform.scale(surf, (64, 64)),
                        self.all_sprites,
                        z=LAYERS[self.game.level][layer_name]
                    )

        return self.tmx_data

    def update(self):
        directions = [KEY_PLAYER_RIGHT, KEY_PLAYER_LEFT, KEY_PLAYER_UP, KEY_PLAYER_DOWN]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key in directions:
                    self.game.lifo_direction_key_pressed.append(event.key)

                if event.key == KEY_INVENTORY_RIGHT:
                    self.player.inventory.right()
                elif event.key == KEY_INVENTORY_LEFT:
                    self.player.inventory.left()

                if event.key == pygame.K_ESCAPE:
                    self.game.state = self.game.pause_menu

            if event.type == pygame.KEYUP:
                if event.key in self.game.lifo_direction_key_pressed:
                    self.game.lifo_direction_key_pressed.remove(event.key)

        self.player.update()

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        self.all_sprites.custom_draw(self.player)

        self.player.inventory.draw(self.game.screen)


class CameraGroup(pygame.sprite.Group):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.pos.x - self.game.screen_width // 2
        self.offset.x = min(self.offset.x, self.game.gameplay.world_width - self.game.screen_width)
        self.offset.x = max(0, self.offset.x)

        self.offset.y = player.pos.y - self.game.screen_height // 2
        self.offset.y = min(self.offset.y, self.game.gameplay.world_height - self.game.screen_height)
        self.offset.y = max(0, self.offset.y)

        for layer_name, layer in LAYERS[self.game.level].items():
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.game.screen.blit(sprite.image, offset_rect)

                    if layer == 'Walls':
                        pygame.draw.rect(
                            self.game.screen,
                            'yellow',
                            (
                                sprite.hitbox.x - self.offset.x,
                                sprite.hitbox.y - self.offset.y,
                                sprite.hitbox.w,
                                sprite.hitbox.h
                            ),
                            1
                        )

        for sprite in self.game.gameplay.visible_letters_e.values():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.game.screen.blit(sprite.image, offset_rect)
            sprite.animate()
