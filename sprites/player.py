from values import *
from inventory import Inventory


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
        self.speed = 200
        self.inventory = Inventory()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        distance = self.speed * self.game.dt

        if self.game.last_arrow_pressed == KEY_PLAYER_UP:
            self.pos.y -= distance
        if self.game.last_arrow_pressed == KEY_PLAYER_DOWN:
            self.pos.y += distance
        if self.game.last_arrow_pressed == KEY_PLAYER_LEFT:
            self.pos.x -= distance
        if self.game.last_arrow_pressed == KEY_PLAYER_RIGHT:
            self.pos.x += distance

        self.rect.topleft = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
