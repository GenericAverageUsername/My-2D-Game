import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

PLAYER_MODELS = [pygame.image.load("Data\\Images\\PlayerDown.png"), pygame.image.load("Data\\Images\\PlayerUp.png"), pygame.image.load("Data\\Images\\PlayerLeft.png"), pygame.image.load("Data\\Images\\PlayerRight.png")]
MISSILE_MODEL = [pygame.image.load("Data\\Images\\missle.png")]
WALL_MODEL = [pygame.image.load("Data\\Images\\Wall.png")]

PLAYER_HIT_BOX = [3, 0, 33, 66]
MISSILE_HIT_BOX = [7, 5, 7, 7]
WALL_HIT_BOX = [0, 0, 40, 40]

DEF_PLAYER_POSITION = [SCREEN_WIDTH/2 - PLAYER_HIT_BOX[2]/2, SCREEN_HEIGHT/2 - PLAYER_HIT_BOX[3]/2]
playerPosition = [SCREEN_WIDTH/2 - PLAYER_HIT_BOX[2]/2, SCREEN_HEIGHT/2 - PLAYER_HIT_BOX[3]/2]

enimies = []
projectiles = []
solids = []

screenVelocity = [0, 0]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))