import pygame
from scenes.menus import Button
from settings import *


class Pause:
    def __init__(self, game):
        self.game = game
        self.background = pygame.Surface((self.game.screen_width, self.game.screen_height), pygame.SRCALPHA)

        self.buttons = pygame.sprite.Group()

        self.button_resume = Button('Reprendre', 0, self.buttons)
        self.button_exit = Button('Quitter', 1, self.buttons)

        for button in self.buttons:
            button.set_position()

    def draw(self):
        self.game.gameplay.draw()
        pygame.draw.rect(
            self.background,
            (128, 128, 128, 150),
            (0, 0, self.game.screen_width, self.game.screen_height)
        )
        self.game.screen.blit(self.background, (0, 0))

        # Dessin d'un repère rouge au milieu de l'écran :
        # pygame.draw.line(self.game.screen, 'red', (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))

        for button in self.buttons:
            button.draw(self.game.screen)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.quit()

            if event.type == pygame.KEYUP:
                if event.key in self.game.lifo_direction_key_pressed:
                    self.game.lifo_direction_key_pressed.remove(event.key)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(x, y):
                        if button == self.button_resume:
                            self.game.state = self.game.gameplay
                        elif button == self.button_exit:
                            self.game.quit()
