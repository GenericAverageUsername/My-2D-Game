from Data.PhysicsTemplate import PhysicsObject

class Missile(PhysicsObject):
    def __init__(self, model, hitBox, position, velocity, damage):
        super().__init__(model, hitBox, position, velocity, "projectile", False)

        self.damage = damage