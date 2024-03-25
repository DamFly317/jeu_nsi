import pygame.sprite
from values import *


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        surface = pygame.Surface((200, 50))
        surface.fill(PLAYER_COLOR)

        self.image = surface

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2


class MainMenu:
    def __init__(self, game):
        self.game = game
        self.buttons = pygame.sprite.Group(Button())

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in self.buttons.sprites():
                    if button.rect.collidepoint(x, y):
                        print('coucou')

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        self.buttons.draw(self.game.screen)

        pygame.display.update()
