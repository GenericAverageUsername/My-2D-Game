import pygame
import time
import math
from Data.PhysicsTemplate import PhysicsObject
from Data.PhysicsTemplate import myCollidelist
import Data.CommonVars as CommonVars

class Player(PhysicsObject):
    def __init__(self, model, hitBox, position, velocity):
        super().__init__(model, hitBox, position, velocity, "none", True)

    def inputs(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.velocity[1] = -4
            self.facing = "up"

            self.changeModel(1)
        elif key[pygame.K_s]:
            self.velocity[1] = 4
            self.facing = "down"

            self.changeModel(0)
        else:
            if self.velocity[1] < 0:
                self.velocity[1] += 8/15
            elif self.velocity[1] > 0:
                self.velocity[1] -= 8/15

        if key[pygame.K_a]:
            self.velocity[0] = -4
            self.facing = "left"

            self.changeModel(2)
        elif key[pygame.K_d]:
            self.velocity[0] = 4
            self.facing = "right"

            self.changeModel(3)
        else:
            if self.velocity[0] < 0:
                self.velocity[0] += 8/15
            elif self.velocity[0] > 0:
                self.velocity[0] -= 8/15

        if abs(self.velocity[0]) < 0.27:
            self.velocity[0] = 0
        if abs(self.velocity[1]) < 0.27:
            self.velocity[1] = 0
    
    def move(self):
        self.inputs()

        updatedHitBox = pygame.Rect(self.hitBox.left + self.velocity[0], self.hitBox.top + self.velocity[1], self.hitBox.width, self.hitBox.height)
        collide = myCollidelist(updatedHitBox, CommonVars.solids)
        while len(collide[0]) > 0:
            if collide[1][0] == "left":
                self.position[0] = collide[0][0].left - self.hitBox.width - CommonVars.PLAYER_HIT_BOX[0]
                self.velocity[0] = 0
            elif collide[1][0] == "up":
                self.position[1] = collide[0][0].top - self.hitBox.height - CommonVars.PLAYER_HIT_BOX[1]
                self.velocity[1] = 0
            elif collide[1][0] == "right":
                self.position[0] = collide[0][0].left + collide[0][0].width - CommonVars.PLAYER_HIT_BOX[0]
                self.velocity[0] = 0
            elif collide[1][0] == "down":
                self.position[1] = collide[0][0].top + collide[0][0].height - CommonVars.PLAYER_HIT_BOX[1]
                self.velocity[1] = 0
            self.hitBox = pygame.Rect(self.position[0] + self.hitBoxData[0], self.position[1] + self.hitBoxData[1], self.hitBoxData[2], self.hitBoxData[3])
            collide = myCollidelist(self.hitBox, CommonVars.solids)
            
        PhysicsObject.move(self)