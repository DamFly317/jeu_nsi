from typing import List

import pygame.sprite
from values import *
from debug import debug
from scenes.gameplay import GamePlay


class Button(pygame.sprite.Sprite):
    def __init__(self, text, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2):
        super().__init__()
        self.text = text
        self.image = MENU_FONT.render(str(self.text), True, (0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, screen):
        bg = pygame.Surface((self.rect.width + 20, self.rect.height + 20))
        bg.fill((50, 200, 50))

        screen.blit(bg, (self.rect.x - 10, self.rect.y - 10))

        screen.blit(self.image, self.rect)


class MainMenu:
    def __init__(self, game):
        self.game = game
        self.buttons = [
            Button('Jouer')
        ]

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(x, y):
                        self.game.state = GamePlay(self.game)

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        for button in self.buttons:
            button.draw(self.game.screen)
