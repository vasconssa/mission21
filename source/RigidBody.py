from GameObject import GameObject
from Vector2D import Vector2D
import pygame

class Integrator:
    
    def __init__(self):
        pass

    def acceleration(self, pos, vel, heading, dt, planets, thrust = 0.0):
        heading.normalize()
        accel = heading*thrust

        for planet in planets:
            direction = planet.pos - pos
            dis = direction.length()
            direction.normalize()
            gField = planet.G*planet.mass/(dis*dis)
            accel += direction*gField

        return accel

    def evaluate(self, pos, vel, heading, t, dt, derivative, planets, thrust):
        (dx, dy, dvx, dvy) = derivative
        newPos = pos + Vector2D.fromCartesian(dx*dt, dy*dt)
        newVel = vel + Vector2D.fromCartesian(dvx*dt, dvy*dt)

        accel = self.acceleration(newPos, newVel, heading, t+dt, planets, thrust)

        return (newVel.x(), newVel.y(), accel.x(), accel.y())

    def integrate(self, pos, vel, heading, t, dt, planets, thrust = 0.0):
        a = self.evaluate(pos, vel, heading, t, 0.0, (0.0, 0.0, 0.0, 0.0), planets, thrust)
        ax, ay, avx, avy = a
        b = self.evaluate(pos, vel, heading, t, dt*0.5, a, planets, thrust)
        bx, by, bvx, bvy = b
        c = self.evaluate(pos, vel, heading, t, dt*0.5, b, planets, thrust)
        cx, cy, cvx, cvy = c
        dx, dy, dvx, dvy = self.evaluate(pos, vel, heading, t, dt, c, planets, thrust)

        dxDt = (1.0/6.0)*(ax + 2.0*(bx + cx) + dx)
        dyDt = (1.0/6.0)*(ay + 2.0*(by + cy) + dy)
        
        dvxDt = (1.0/6.0)*(avx + 2.0*(bvx + cvx) + dvx)
        dvyDt = (1.0/6.0)*(avy + 2.0*(bvy + cvy) + dvy)

        newPos = pos + Vector2D.fromCartesian(dxDt*dt, dyDt*dt)
        newVel = vel + Vector2D.fromCartesian(dvxDt*dt, dvyDt*dt)

        return (newPos, newVel)

            

class RigidBody(GameObject):

    def __init__(self, name, image, mass, pos, G):
        super(RigidBody, self).__init__(name, image, pos)

        self.mass = mass
        self.G = 15.0
        # self.heading = Vector2D(1.0, 0.0)
        self.integrator = Integrator()
        self.internalForce = 0

    def rotate(self, angle):
        self.heading.rotate(-angle)
        self.imageAngle += angle

    def update(self, dt, planets):
        self.pos, self.vel = self.integrator.integrate(self.pos, self.vel, self.heading, 0.0, dt, planets, self.internalForce)
        super(RigidBody, self).update()

    def collide_with_player(self, player):
        pass
