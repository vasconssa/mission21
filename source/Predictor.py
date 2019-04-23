from GameObject import GameObject
from RigidBody import RigidBody, Integrator
from Vector2D import Vector2D
from math import *
import pygame
from pygame.locals import *
import prepare

class Predictor:
    def __init__(self):
        self.integrator = Integrator()
        self.trajPoints = []

    def trajectory(self, player):
        internalForce = player.internalForce
        pos = player.pos
        vel = player.vel
        dt = 20*player.dt
        heading = player.heading
        planets = player.planets
        steps = 50
        self.trajPoints = []
        for i in range(steps):
            pos, vel = self.integrator.integrate(pos, vel, heading, 0.0, dt, planets, internalForce)
            self.trajPoints.append((pos[0], pos[1]))

    def draw(self, surface):
        color = (241, 95, 188)
        pygame.draw.lines(surface, color, False, self.trajPoints)

