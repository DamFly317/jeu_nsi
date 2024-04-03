from values import *
from ui import Inventory
from debug import debug


class Player(pygame.sprite.Sprite):
    def __init__(self, game, *groups):
        self.game = game
        super().__init__(*groups)

        surface = pygame.Surface(PLAYER_SIZE)
        surface.fill(PLAYER_COLOR)

        self.image = surface
        self.rect = self.image.get_rect(center=(1000, 1000))
        self.z = LAYERS['main']

        self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.speed = 300
        self.direction = 'down'
        self.inventory = Inventory()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        distance = self.speed * self.game.dt

        if len(self.game.lifo_direction_key_pressed) > 0:

            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_UP:
                self.pos.y -= distance
            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_DOWN:
                self.pos.y += distance
            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_LEFT:
                self.pos.x -= distance
            if self.game.lifo_direction_key_pressed[-1] == KEY_PLAYER_RIGHT:
                self.pos.x += distance

        self.rect.topleft = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
