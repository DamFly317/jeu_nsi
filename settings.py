import pygame

GAME_TITLE = 'Jeu'

BACKGROUND = '#5a79c8'

# KEYS
KEY_PLAYER_DOWN = pygame.K_s
KEY_PLAYER_UP = pygame.K_z
KEY_PLAYER_LEFT = pygame.K_q
KEY_PLAYER_RIGHT = pygame.K_d
KEY_PLAYER_ATTACK = pygame.K_SPACE

KEY_INVENTORY_RIGHT = pygame.K_RIGHT
KEY_INVENTORY_LEFT = pygame.K_LEFT

# PLAYER
PLAYER_SIZE = PLAYER_WIDTH, PLAYER_HEIGHT = (50, 50)
PLAYER_COLOR = (255, 0, 0)

LAYERS = [
    {
        'Ground': 0,
        'Walls': 1,
        'Decoration': 2,
        'Main': 3
    }
]

