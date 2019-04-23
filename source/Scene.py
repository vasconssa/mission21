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
        self.createPlayer()
        self.addPlatforms()
        self.createBackgrond()
        self.hud = Hud()
        self.predictor = Predictor()

    def createBackgrond(self):
        self.background = prepare.GFX['assets']['background'].convert()
        self.background = pygame.transform.scale(self.background, (1200, 900))


    def addPlanet(self, planet):
        self.planets.append(planet)
        self.planetGroup.add(planet)

    def createPlayer(self):
        screenW, screenH = self.screen.get_size()
        player = Player((30, screenH/2.0))
        player.surf = self.screen
        player.planets = self.planets
        self.player = player
        self.playerGroup.add(self.player)

    def addPlatforms(self):
        begin = prepare.GFX["assets"]['base'].convert_alpha()
        rect = begin.get_rect()
        w, h = rect.width, rect.height
        begin = pygame.transform.scale(begin, (floor(0.15*w), floor(0.15*h)))
        end = prepare.GFX["assets"]['base'].convert_alpha()
        rect = end.get_rect()
        w, h = rect.width, rect.height
        end = pygame.transform.scale(end, (floor(0.15*w), floor(0.15*h)))
        rect = end.get_rect()
        w, h = rect.width, rect.height
        screenW, screenH = self.screen.get_size()
        # self.beginPlatform = GameObject("PlataformaInicial", begin, (w/2.0, screenH/2.0))
        # self.endPlatform = GameObject("PlataformaFinal", end, (screenW - w/2.0, screenH/2.0))
        self.beginPlatform = platform.Platform("PlataformaInicial", begin, (w/2.0, screenH/2.0))
        self.endPlatform = platform.Platform("PlataformaFinal", end, (screenW - w/2.0, screenH/2.0),True)
        self.platformGroup.add(self.beginPlatform)
        self.platformGroup.add(self.endPlatform)

    def update(self, dt):
        if(self.player.alive):
            self.check_collisions()

            self.player.dt = dt
            self.player.update()
            self.predictor.trajectory(self.player)
            fuel = self.player.fuel
            score = self.hud.score
            if self.player.ignite:
                score -= 1
            self.hud.updateScore(score)
            self.hud.updateFuel(fuel)


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
        # self.process_attacks()
        

