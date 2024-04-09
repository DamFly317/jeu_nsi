import pygame.image

from settings import *
from debug import debug
from sprites.sprites import Generic
from sprites.player import Player


class GamePlay:
    def __init__(self, game):
        self.game = game
        self.all_visible_sprites = CameraGroup(self.game)

        self.player = Player(self.game, self.all_visible_sprites)
        # Ground
        self.ground = Generic(
            (0, 0),
            pygame.image.load('graphics/ground.png').convert_alpha(),
            self.all_visible_sprites,
            z=LAYERS['ground']
        )

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
                    self.game.state = self.game.main_menu

            if event.type == pygame.KEYUP:
                if event.key in self.game.lifo_direction_key_pressed:
                    self.game.lifo_direction_key_pressed.remove(event.key)

        self.player.update()

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        self.all_visible_sprites.custom_draw(self.player, self.ground)

        self.player.inventory.draw(self.game.screen)
        pygame.display.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player, ground):
        self.offset.x = min(
            ground.rect.width - self.game.screen_width,
            max(0, player.rect.centerx - self.game.screen_width // 2)
        )
        self.offset.y = min(
            ground.rect.height - self.game.screen_height,
            max(0, player.rect.centery - self.game.screen_height // 2)
        )

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.game.screen.blit(sprite.image, offset_rect)
