from values import *
from debug import debug
from inventory import inventory


class GamePlay:
    def __init__(self, game):
        self.game = game
        self.inventory = inventory

    def update(self):
        directions = [KEY_PLAYER_RIGHT, KEY_PLAYER_LEFT, KEY_PLAYER_UP, KEY_PLAYER_DOWN]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.KEYDOWN:
                for arrow in directions:
                    if event.key == arrow:
                        self.game.last_arrow_pressed = arrow
            if event.type == pygame.KEYUP:
                if event.key == self.game.last_arrow_pressed:
                    self.game.last_arrow_pressed = None

        self.game.player.update()

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        self.game.player.draw(self.game.screen)
        self.inventory.draw(self.game.screen)

        pygame.display.update()
