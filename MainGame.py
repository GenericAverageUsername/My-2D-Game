import pygame
import time
import Data.CommonVars as CommonVars
from Data.Player import Player
from Data.Terrain.Missile import Missile
from Data.Terrain.Wall import Wall

pygame.init()

player = Player(CommonVars.PLAYER_MODELS, CommonVars.PLAYER_HIT_BOX, CommonVars.playerPosition, [0, 0])
walls = []
for i in range(0, 1000):
    walls.append(Wall(CommonVars.WALL_MODEL, CommonVars.WALL_HIT_BOX, [40*i, 0], [0, 0]))

run = True
while run:
    time.sleep(1/CommonVars.FPS)

    CommonVars.screen.fill((128, 0, 128))

    player.move()
    for i in walls:
        i.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()