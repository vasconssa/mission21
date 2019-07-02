from AbstractScene import AbstractScene
from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
from components import platform
import pygame
from pygame.locals import *
import prepare,tools
from Scene import Scene
from components.planet import Planet


class SceneBuilder:
    def __init__(self, screen):
        self.screen = screen
        self.scene = Scene(screen)
        self.setBackground()
        self.createPlayer()
        self.createPlatforms()

    def setBackground(self, backgroundName = 'background'):
        self.scene.background = prepare.GFX['assets']['background'].convert()
        self.scene.background = pygame.transform.scale(self.scene.background, (1200, 900))
        return self

    def createPlayer(self):
        screenW, screenH = self.screen.get_size()
        player = Player((30, screenH/2.0))
        player.surf = self.screen
        player.planets = self.scene.planets
        self.scene.player = player
        self.scene.playerGroup.add(self.scene.player)
        return self

    def createPlatforms(self):
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
        self.scene.beginPlatform = platform.Platform("PlataformaInicial", begin, (w/2.0, screenH/2.0))
        self.scene.endPlatform = platform.Platform("PlataformaFinal", end, (screenW - w/2.0, screenH/2.0),True)
        self.scene.platformGroup.add(self.scene.beginPlatform)
        self.scene.platformGroup.add(self.scene.endPlatform)
        return self
    

    def setPlanets(self, planetAssets, positions, masses, gConstants):
        for planetName, position, mass, G in zip(planetAssets, positions, masses, gConstants):
            planetImg = prepare.GFX["assets"][planetName]
            rect = planetImg.get_rect()
            w, h = rect.width, rect.height
            planeta = pygame.transform.scale(planetImg, (floor(0.3 * w), floor(0.3 * h)))
            wS, hS = self.screen.get_size()
            x = position[0]
            y = position[1]
            screenCoord = self.coord2Screen(x,y)
            planet = Planet(planetName, planeta, mass, screenCoord, G)
            self.scene.addPlanet(planet)

        return self

    def __call__(self):
        if self.scene:
            scene = self.scene
            self.reset()
            return scene
        return None

    def reset(self):
            self.scene = Scene(self.screen)
            self.setBackground()
            self.createPlayer()
            self.createPlatforms()


    def coord2Screen(self, x, y):
        w, h = self.screen.get_size()
        xS = x*w
        yS = y*h
        return (int(xS), int(yS))

    
class SceneManager:
    def __init__(self, screen):
        self.scenes = []
        self.screen = screen
        self.builder = SceneBuilder(screen)
        self.createScenes()

    def createScenes(self):
        # Scene 1
        scene1 = self.builder.setBackground().setPlanets(['greenPlanet'], [(0.5, 0.5)], [100001.0], [150.0])()
        self.scenes.append(scene1)

        # Scene 2
        scene2 = self.builder.setBackground().setPlanets(['moonPlanet', 'rocketPlanet'], [(0.7, 0.8), (0.4, 0.3)],
                                            [100001.0, 100001.0], [250.0, 250.0])()

        self.scenes.append(scene2)

        # Scene 3
        scene3 = self.builder.setBackground().setPlanets(['sandPlanet'], [(0.3, 0.4)], [100001.0], [150.0])()

        self.scenes.append(scene3)
        self.scenes.append(scene3)


