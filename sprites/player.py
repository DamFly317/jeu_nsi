from values import *
from inventory import Inventory


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        surface = pygame.Surface(PLAYER_SIZE)
        surface.fill(PLAYER_COLOR)

        self.image = surface

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2

        self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.inventory = Inventory()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)

        distance = PLAYER_SPEED * self.game.dt

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
