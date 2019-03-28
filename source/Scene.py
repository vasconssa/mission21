from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
import pygame
from pygame.locals import *


class Scene():
    def __init__(self, screen):
        self.screen = screen
        self.player = None
        self.beginPlatform = None
        self.endPlatform = None
        self.background = None
        self.planets = []
        self.playerGroup = pygame.sprite.Group()
        self.planetGroup = pygame.sprite.Group()
        self.platformGroup = pygame.sprite.Group()
        self.createPlayer()
        self.addPlatforms()
        self.createBackgrond()

    def createBackgrond(self):
        self.background = pygame.image.load("../assets/background.png").convert()
        self.background = pygame.transform.scale(self.background, (1200, 900))


    def addPlanet(self, planet):
        self.planets.append(planet)
        self.planetGroup.add(planet)

    def createPlayer(self):
        player = Player((30, 450))
        player.surf = self.screen
        player.planets = self.planets
        self.player = player
        self.playerGroup.add(self.player)

    def addPlatforms(self):
        begin = pygame.image.load("../assets/base.png").convert_alpha()
        end = pygame.image.load("../assets/base.png").convert_alpha()
        self.beginPlatform = GameObject("PlataformaInicial", begin, (30, 450))
        self.endPlatform = GameObject("PlataformaFinal", end, (830, 450))
        self.platformGroup.add(self.beginPlatform)
        self.platformGroup.add(self.endPlatform)

    def update(self, dt):
        self.player.dt = dt
        self.player.update()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.platformGroup.draw(self.screen)
        self.playerGroup.draw(self.screen)
        self.planetGroup.draw(self.screen)
        

