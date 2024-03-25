import pygame

pygame.init()

GAME_TITLE = 'Jeu'

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (720, 480)
BACKGROUND = '#d8dcb4'

# MENU
MENU_FONT = pygame.font.Font(None, 70)

# KEYS
KEY_PLAYER_DOWN = pygame.K_s
KEY_PLAYER_UP = pygame.K_z
KEY_PLAYER_LEFT = pygame.K_q
KEY_PLAYER_RIGHT = pygame.K_d

# PLAYER
PLAYER_SIZE = PLAYER_WIDTH, PLAYER_HEIGHT = (30, 30)
PLAYER_COLOR = (255, 0, 0)
PLAYER_SPEED = 200
