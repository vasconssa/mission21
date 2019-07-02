from AbstractScene import AbstractScene
from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Predictor import Predictor
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
from components import platform
import pygame
from pygame.locals import *
from Hud import Hud
import prepare,tools

class Scene(AbstractScene):
    def __init__(self, screen):
        super(Scene, self).__init__(screen)
        self.player = None
        self.beginPlatform = None
        self.endPlatform = None
        self.background = None
        self.planets = []
        self.playerGroup = pygame.sprite.Group()
        self.planetGroup = pygame.sprite.Group()
        self.platformGroup = pygame.sprite.Group()
        self.hud = Hud()
        self.predictor = Predictor()

    def addPlanet(self, planet):
        self.planets.append(planet)
        self.planetGroup.add(planet)


    def update(self, dt):
        if(self.player.alive and not self.player.final):
            self.check_collisions()

            self.player.dt = dt
            self.player.update()
            self.predictor.trajectory(self.player)
            fuel = self.player.fuel
            score = self.hud.score
            if self.player.ignite:
                score -= 10
            self.hud.updateScore(score)
            self.hud.updateFuel(fuel)
        elif(self.player.alive):
            self.player.update()



    def draw(self,surface):
        surface.blit(self.background, (0,0))
        # self.platformGroup.draw(self.screen)
        # self.playerGroup.draw(self.screen)
        # self.planetGroup.draw(self.screen)
        self.platformGroup.draw(surface)
        self.playerGroup.draw(surface)
        self.predictor.draw(surface)
        self.planetGroup.draw(surface)
        self.hud.draw(surface)


    def check_collisions(self):
        print("Checa colisões")
        """
                Check collisions and call the appropriate functions of the affected
                sprites.
                """
        callback = tools.rect_then_mask
        groups = pygame.sprite.Group(self.planetGroup, self.platformGroup)
        hits = pygame.sprite.spritecollide(self.player, groups, False, callback)
        for hit in hits:
            hit.collide_with_player(self.player)
        if (self.player.rect.top>prepare.SCREEN_SIZE[1] or self.player.rect.right>prepare.SCREEN_SIZE[0] or self.player.rect.bottom<0):
            self.player.alive=False

            pass
        # self.process_attacks()
        

