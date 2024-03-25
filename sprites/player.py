import pygame
from values import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        surface = pygame.Surface(PLAYER_SIZE)
        surface.fill(PLAYER_COLOR)

        self.image = surface

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        if self.game.last_arrow_pressed == KEY_PLAYER_UP:
            self.rect.y -= PLAYER_SPEED
        if self.game.last_arrow_pressed == KEY_PLAYER_DOWN:
            self.rect.y += PLAYER_SPEED
        if self.game.last_arrow_pressed == KEY_PLAYER_LEFT:
            self.rect.x -= PLAYER_SPEED
        if self.game.last_arrow_pressed == KEY_PLAYER_RIGHT:
            self.rect.x += PLAYER_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)
