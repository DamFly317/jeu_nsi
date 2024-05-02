import pygame


class Pause:
    def __init__(self, game):
        self.game = game
        self.surface = pygame.Surface((self.game.screen_width, self.game.screen_height), pygame.SRCALPHA)

    def draw(self):
        self.game.gameplay.draw()
        pygame.draw.rect(
            self.surface,
            (128, 128, 128, 150),
            (0, 0, self.game.screen_width, self.game.screen_height)
        )
        self.game.screen.blit(self.surface, (0, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.state = self.game.gameplay

            if event.type == pygame.KEYUP:
                if event.key in self.game.lifo_direction_key_pressed:
                    self.game.lifo_direction_key_pressed.remove(event.key)
