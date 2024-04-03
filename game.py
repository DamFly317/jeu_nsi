import math
import sys
import time
from typing import List, Any

import pygame.sprite

from sprites.player import Player
from scenes.menus import *
from scenes.gameplay import CameraGroup


class Game:
    lifo_direction_key_pressed: List[Any]

    def __init__(self):
        pygame.init()

        self.running = True

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.previous_time = 0
        self.dt = 1

        self.state = MainMenu(self)
        self.difficulty = 0

        self.lifo_direction_key_pressed = []

    def start(self):
        # Instructions au démarage
        self.run()

    def run(self):
        self.previous_time = time.time()
        while self.running:

            self.state.draw()
            self.state.update()

            self.dt = time.time() - self.previous_time
            self.previous_time = time.time()

            pygame.display.update()

        pygame.quit()
        sys.exit()
