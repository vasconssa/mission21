import pygame
import pygame.gfxdraw
from pygame.locals import *
import prepare
from math import pi
import math

class CircleProgressBar:
    def __init__(self, pos=(0, 0)):
        self.color = (39, 95, 188)
        self.percentage = 50
        self.pos = pos
        self.rect = Rect(0,0,150,150)
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.font = prepare.FONTS["military_font_7"]

    def setPercentage(self, value):
        self.percentage = value

    def calcCirclePoints(self,center, finalAngle, radius=150.0):
        points = []
        start = pi/2
        final = pi/2 + finalAngle
        divs = 50
        step = (final - start)/divs
        angle = start
        for i in range(divs):
            angle = angle + step
            x = center[0] + radius*math.cos(angle)
            y = center[1] + radius*math.sin(angle)
            points.append([x,y])

        return points 

    def draw(self, surface):
        finalAngle = self.percentage*2*pi/100.0
        gray = (121, 127, 137)
        width = 15.0
        prec = 150
        step = width/prec
        radius = 100.0
        pygame.draw.circle(surface, gray, self.pos, int(radius), 15)
        for i in range(prec):
            points = self.calcCirclePoints(self.pos, finalAngle, radius)
            fillCirclePoints = self.calcCirclePoints(self.pos, 2*pi, radius)
            # pygame.draw.aalines(surface, gray, True, fillCirclePoints, 1)
            pygame.draw.lines(surface, self.color, False, points, 1)
            radius = radius - step
