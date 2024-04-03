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
        self.fps = 0
        self.fps_count = 0
        self.previous_second = 0

        self.state = MainMenu(self)
        self.difficulty = 0

        self.lifo_direction_key_pressed = []

    def start(self):
        # Instructions au démarage
        self.run()

    def run(self):
        self.previous_time = time.time()
        self.previous_second = math.floor(self.previous_time)

        while self.running:
            self.dt = time.time() - self.previous_time
            self.previous_time = time.time()

            if math.floor(self.previous_time) > self.previous_second:
                self.fps = self.fps_count
                self.fps_count = 0
                self.previous_second = math.floor(self.previous_time)

            self.state.draw()
            self.state.update()
            debug('FPS : ' + str(self.fps), x=SCREEN_WIDTH - 100)
            pygame.display.update()
            self.fps_count += 1

        pygame.quit()
        sys.exit()

    def count_fps(self):
        pass

