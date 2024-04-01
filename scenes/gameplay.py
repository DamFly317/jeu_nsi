import pygame.image

from values import *
from sprites.sprites import Generic
from sprites.player import Player


class GamePlay:
    def __init__(self, game):
        self.game = game
        self.all_sprites = CameraGroup(self.game)

        self.player = Player(self.game, self.all_sprites)
        # Ground
        Generic(
            (0, 0),
            pygame.image.load('graphics/ground.png'),
            self.all_sprites,
            z=LAYERS['ground']
        )

    def update(self):
        directions = [KEY_PLAYER_RIGHT, KEY_PLAYER_LEFT, KEY_PLAYER_UP, KEY_PLAYER_DOWN]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                for arrow in directions:
                    if event.key == arrow:
                        self.game.last_arrow_pressed = arrow
                if event.key == KEY_INVENTORY_RIGHT:
                    self.player.inventory.right()
                elif event.key == KEY_INVENTORY_LEFT:
                    self.player.inventory.left()

            if event.type == pygame.KEYUP:
                if event.key == self.game.last_arrow_pressed:
                    self.game.last_arrow_pressed = None

        self.player.update()

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        self.all_sprites.custom_draw(self.player)

        self.player.inventory.draw(self.game.screen)
        pygame.display.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH // 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT // 2
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.game.screen.blit(sprite.image, offset_rect)
