import math
import CommonVars
import pygame

class PhysicsObject:
    def __init__(self, models, hitBox, position, velocity, collisionType, player):
        self.active = True

        self.models = models
        self.model = models[0]
        self.position = position
        self.velocity = velocity
        self.hitBoxData = hitBox
        self.isPlayer = player
        self.collisionType = collisionType
        self.hitBox = pygame.Rect(self.position[0] + hitBox[0], self.position[1] + hitBox[1], hitBox[2], hitBox[3])

        if collisionType == "enimy":
            CommonVars.enimies.append([self.hitBox, True])
            self.collisionId = len(CommonVars.solids) - 1
        elif collisionType == "projectile":
            CommonVars.projectiles.append([self.hitBox, True])
            self.collisionId = len(CommonVars.solids) - 1
        elif collisionType == "solid":
            CommonVars.solids.append([self.hitBox, True])
            self.collisionId = len(CommonVars.solids) - 1

        self.canDeleteHitbox = True

    def changeModel(self, modelNum):
        self.model = self.models[modelNum]

    def move(self):
        if self.collisionType == "enimy":
            CommonVars.enimies[self.collisionId][1] = self.active
        elif self.collisionType == "projectile":
            CommonVars.projectiles[self.collisionId][1] = self.active
        elif self.collisionType == "solid":
            CommonVars.solids[self.collisionId][1] = self.active

        if self.active:
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]

            self.hitBox = pygame.Rect(self.position[0] + self.hitBoxData[0], self.position[1] + self.hitBoxData[1], self.hitBoxData[2], self.hitBoxData[3])

            self.draw()
    
    def draw(self):
        #pygame.draw.rect(CommonVars.screen, (255, 0, 0), self.hitBox)
        CommonVars.screen.blit(self.model, [self.position[0] - (CommonVars.playerPosition[0] - CommonVars.DEF_PLAYER_POSITION[0]), self.position[1] - (CommonVars.playerPosition[1] - CommonVars.DEF_PLAYER_POSITION[1])])




def myCollidelist(rectangle: pygame.Rect, rectangleList: list[list]):
    stuffCollidedWith = []
    directionCollidedWith = []
    for j in rectangleList:
        i = j[0]
        if j[1] and rectangle.left < i.left + i.width and rectangle.left > i.left - rectangle.width and rectangle.top < i.top + i.height and rectangle.top > i.top - rectangle.height:
            stuffCollidedWith.append(i)
        
            rectangleMiddle = [rectangle.left + rectangle.width/2, rectangle.top + rectangle.height/2]
            rectangle2Middle = [i.left + i.width/2, i.top + i.height/2]
            if rectangle.width > rectangle.height:
                if rectangleMiddle[0] < rectangle2Middle[0]:
                    rectangleMiddle = [rectangle.left + rectangle.width - rectangle.height/2, rectangle.top + rectangle.height/2]
                else:
                    rectangleMiddle = [rectangle.left + rectangle.height/2, rectangle.top + rectangle.height/2]
            elif rectangle.width < rectangle.height:
                if rectangleMiddle[1] < rectangle2Middle[1]:
                    rectangleMiddle = [rectangle.left + rectangle.width/2, rectangle.top + rectangle.height - rectangle.width/2]
                else:
                    rectangleMiddle = [rectangle.left + rectangle.width/2, rectangle.top + rectangle.width/2]

            if rectangleMiddle[0] - rectangle2Middle[0] != 0:
                slope = (rectangleMiddle[1] - rectangle2Middle[1])/(rectangleMiddle[0] - rectangle2Middle[0])
                angle = math.atan(slope)*180/math.pi
                if rectangleMiddle[0] - rectangle2Middle[0] > 0:
                    if angle > -45 and angle < 45:
                        directionCollidedWith.append("right")
                    if angle >= 45 and angle < 90:
                        directionCollidedWith.append("down")
                    if angle > -90 and angle <= -45:
                        directionCollidedWith.append("up")
                else:
                    angle += 180
                    if angle > 225 and angle < 270:
                        directionCollidedWith.append("up")
                    if angle > 135 and angle <= 225:
                        directionCollidedWith.append("left")
                    if angle > 90 and angle <= 135:
                        directionCollidedWith.append("down")
            else:
                if rectangleMiddle[1] - rectangle2Middle[1] > 0:
                    directionCollidedWith.append("down")
                else:
                    directionCollidedWith.append("up")

    return [stuffCollidedWith, directionCollidedWith]