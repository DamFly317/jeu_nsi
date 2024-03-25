from values import *
from player import Player
from scenes.menus import *

class Game:
    def __init__(self):
        pygame.init()

        self.running = True

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()

        self.state = MainMenu(self)

        self.last_arrow_pressed = None

        self.player = Player(self)

    def start(self):
        # Instructions au démarage
        self.run()

    def run(self):
        while self.running:
            directions = [KEY_PLAYER_RIGHT, KEY_PLAYER_LEFT, KEY_PLAYER_UP, KEY_PLAYER_DOWN]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.state.draw()
            self.state.update()
