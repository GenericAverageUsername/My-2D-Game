from PhysicsTemplate import PhysicsObject

class Wall(PhysicsObject):
    def __init__(self, model, hitBox, position, velocity):
        super().__init__(model, hitBox, position, velocity, "solid", False)