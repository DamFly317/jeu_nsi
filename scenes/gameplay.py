from values import *


class GamePlay:
    def __init__(self, game):
        self.game = game

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
                    self.game.player.inventory.right()
                elif event.key == KEY_INVENTORY_LEFT:
                    self.game.player.inventory.left()

            if event.type == pygame.KEYUP:
                if event.key == self.game.last_arrow_pressed:
                    self.game.last_arrow_pressed = None

        self.game.player.update()

    def draw(self):
        self.game.screen.fill(BACKGROUND)

        self.game.player.draw(self.game.screen)

        self.game.player.inventory.draw(self.game.screen)
        pygame.display.update()
