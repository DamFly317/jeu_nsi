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
                        self.last_arrow_pressed = arrow
            if event.type == pygame.KEYUP:
                if event.key == self.last_arrow_pressed:
                    self.last_arrow_pressed = None

        self.game.player.update()
        self.game.clock.tick(60)


    def draw(self):
        self.screen.fill(BACKGROUND)

        self.player.draw(self.screen)

        pygame.display.update()
