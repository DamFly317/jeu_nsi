import sys
import time

from pygame.surface import Surface, SurfaceType

from sprites.player import Player
from scenes.menus import *


class Game:
    def __init__(self):
        pygame.init()

        self.running = True

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.previous_time = 0
        self.dt = 0

        self.state = MainMenu(self)
        self.player = Player(self)

        self.last_arrow_pressed = None

    def start(self):
        # Instructions au démarage
        self.run()

    def run(self):
        self.previous_time = time.time()
        while self.running:
            self.dt = time.time() - self.previous_time
            self.previous_time = time.time()
            directions = [KEY_PLAYER_RIGHT, KEY_PLAYER_LEFT, KEY_PLAYER_UP, KEY_PLAYER_DOWN]

            self.state.draw()
            self.state.update()
            pygame.display.update()

        pygame.quit()
        sys.exit()
