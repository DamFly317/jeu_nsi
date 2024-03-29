import pygame.transform

from values import *


class Slot(pygame.sprite.Sprite):
    def __init__(self, i):
        super().__init__()
        self.size = 64
        self.space_between = 7

        self.image_selected = pygame.transform.scale2x(
            pygame.image.load('assets/slot_selected.png')
        )
        self.image_available = pygame.transform.scale2x(
            pygame.image.load('assets/slot_available.png')

        )

        self.image = self.image_available

        x = (
                SCREEN_WIDTH // 2 - 5 * (self.size + self.space_between) +
                i * (self.size + self.space_between) + self.space_between // 2
        )
        y = SCREEN_HEIGHT - self.size - 5
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_state(self, selected: bool):
        if selected:
            self.image = self.image_selected
        else:
            self.image = self.image_available


class Inventory(pygame.sprite.Group):
    def __init__(self):
        self.items_number = 10
        self.slots = [Slot(i) for i in range(self.items_number)]
        self.items = [None for _ in range(self.items_number)]
        self.selected_slot = 0

        super().__init__(self.slots)
        self.slots[self.selected_slot].change_state(selected=True)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.slots[self.selected_slot].change_state(selected=True)

    def right(self):
        self.slots[self.selected_slot].change_state(selected=False)
        self.selected_slot += 1
        if self.selected_slot >= self.items_number:
            self.selected_slot = 0
        self.update()

    def left(self):
        self.slots[self.selected_slot].change_state(selected=False)
        self.selected_slot -= 1
        if self.selected_slot < 0:
            self.selected_slot = self.items_number - 1
        self.update()
