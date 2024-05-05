import math
import sys
import time
from typing import List, Any

import pygame.sprite

from scenes.menus import *
from scenes.pause import Pause


class Game:
    lifo_direction_key_pressed: List[Any]

    def __init__(self):
        pygame.init()

        self.running = True

        self.screen = pygame.display.set_mode((0, 0))
        pygame.display.set_caption(GAME_TITLE)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.clock = pygame.time.Clock()
        self.previous_time = 0
        self.dt = 1
        self.fps = 0
        self.fps_count = 0
        self.previous_second = 0

        self.difficulty = 0
        self.level = 0
        self.main_menu = MainMenu(self)
        self.gameplay = GamePlay(self)
        self.gameplay.player.load_environement()
        self.pause_menu = Pause(self)
        self.state = self.main_menu

        self.lifo_direction_key_pressed = []

    def start(self):
        # Instructions au démarage
        self.run()

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def run(self):
        self.previous_time = time.time()
        self.previous_second = math.floor(self.previous_time)

        while self.running:
            self.dt = time.time() - self.previous_time
            self.previous_time = time.time()

            self.state.draw()
            pygame.display.update()
            self.state.update()
            self.count_fps()
            pygame.display.update()
            self.fps_count += 1

        self.quit()

    def count_fps(self):
        if math.floor(self.previous_time) > self.previous_second:
            self.fps = self.fps_count
            self.fps_count = 0
            self.previous_second = math.floor(self.previous_time)

        debug('FPS : ' + str(self.fps), x=self.screen_width - 100)
