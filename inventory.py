import pygame


class Slot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        surface = pygame.Surface((32 * 1.5, 32 * 1.5))
        surface.fill((200, 200, 200))
        self.image = surface
        self.rect = self.image.get_rect()


inventory = pygame.sprite.Group(Slot())
