import pygame.sprite
from settings import *
from debug import debug
from scenes.gameplay import GamePlay


class Button(pygame.sprite.Sprite):
    def __init__(self, text, i, group):
        super().__init__(group)
        self.group = group
        self.i = i
        self.text = text
        font = pygame.font.Font(None, 70)
        self.image = font.render(str(self.text), True, (0, 0, 0))

        self.rect = self.image.get_rect()

        self.space_between = 75
        self.height = self.rect.height

    def set_position(self):
        n = len(self.group)
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        x = (screen_width - self.rect.width) // 2

        y = (
                screen_height / 2 - n / 2 * (self.height + self.space_between) +
                self.i * (self.height + self.space_between) + self.space_between / 2
        )

        self.rect.x = x
        self.rect.y = y

        return self

    def draw(self, screen):
        bg = pygame.Surface((self.rect.width + 20, self.rect.height + 20))
        bg.fill((50, 200, 50))

        screen.blit(bg, (self.rect.x - 10, self.rect.y - 10))

        screen.blit(self.image, self.rect)


class MainMenu:
    def __init__(self, game):
        self.game = game

        self.buttons = pygame.sprite.Group()

        self.button_play = Button('Jouer', 0, self.buttons)
        self.button_exit = Button('Quitter', 1, self.buttons)

        for button in self.buttons:
            button.set_position()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(x, y):
                        if button == self.button_play:
                            self.game.state = self.game.gameplay
                        elif button == self.button_exit:
                            self.game.quit()

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        # Dessin d'un repère rouge au milieu de l'écran :
        # pygame.draw.line(self.game.screen, 'red', (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))

        for button in self.buttons:
            button.draw(self.game.screen)


class DifficultyMenu(MainMenu):
    def __init__(self, game):
        super().__init__(game)
        self.game = game

        self.buttons = pygame.sprite.Group()

        self.button_easy = Button('Facile', 0, self.buttons)
        self.button_medium = Button('Moyen', 1, self.buttons)
        self.button_hard = Button('Hardcore', 2, self.buttons)

        for button in self.buttons:
            button.set_position()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(x, y):
                        if button == self.button_easy:
                            self.game.difficulty = 0
                        elif button == self.button_medium:
                            self.game.difficulty = 1
                        elif button == self.button_hard:
                            self.game.difficulty = 2

                        self.game.state = self.game.main_menu
