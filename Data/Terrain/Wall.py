from Data.PhysicsTemplate import PhysicsObject
import Data.CommonVars as CommonVars

class Wall(PhysicsObject):
    def __init__(self, model, hitBox, position, velocity):
        super().__init__(model, hitBox, position, velocity, "solid", False)
    
    def move(self):
        if abs(self.position[0] - CommonVars.playerPosition[0]) > CommonVars.SCREEN_WIDTH/2 + CommonVars.PLAYER_HIT_BOX[2] or abs(self.position[1] - CommonVars.playerPosition[1]) > CommonVars.SCREEN_HEIGHT/2 + CommonVars.PLAYER_HIT_BOX[3]:
            self.active = False
        else:
            self.active = True

        PhysicsObject.move(self)