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


class SceneManager:
    def __init__(self, screen):
        self.scenes = []
        self.screen = screen
        self.createScenes()

    def createScenes(self):
        # Scene 1
        scene1 = Scene(self.screen)
        planeta = prepare.GFX["assets"]['greenPlanet']
        rect = planeta.get_rect()
        w, h = rect.width, rect.height
        planetafase1 = pygame.transform.scale(planeta, (floor(0.3 * w), floor(0.3 * h)))
        wS, hS = self.screen.get_size()
        x = 0.5
        y = 0.5
        screenCoord = self.coord2Screen(x,y)
        planetfase1 = Planet("teste2", planetafase1, 100001.0, screenCoord, 150.0)
        scene1.addPlanet(planetfase1)

        self.scenes.append(scene1)

        # Scene 2
        scene2 = Scene(self.screen)
        planetafase2 = prepare.GFX["assets"]['moonPlanet'].convert_alpha()
        planeta2fase2 = prepare.GFX["assets"]['rocketPlanet'].convert_alpha()
        rect = planetafase2.get_rect()
        w, h = rect.width, rect.height
        planetafase2 = pygame.transform.scale(planetafase2, (floor(0.3 * w), floor(0.3 * h)))
        planeta2fase2 = pygame.transform.scale(planeta2fase2, (floor(0.3 * w), floor(0.3 * h)))
        wS, hS = self.screen.get_size()
        x = 0.7
        y = 0.8
        screenCoord = self.coord2Screen(x,y)
        planetfase2 = Planet("teste2", planetafase2, 100001.0, screenCoord, 250.0)
        x = 0.4
        y = 0.3
        screenCoord = self.coord2Screen(x,y)
        planet2fase2 = Planet("teste2", planeta2fase2, 100001.0, screenCoord, 200.0)
        scene2.addPlanet(planetfase2)
        scene2.addPlanet(planet2fase2)

        self.scenes.append(scene2)

        # Scene 3
        scene3 = Scene(self.screen)
        planetafase3 = prepare.GFX["assets"]['sandPlanet'].convert_alpha()
        rect = planetafase3.get_rect()
        w, h = rect.width, rect.height
        planetafase3 = pygame.transform.scale(planetafase3, (floor(0.4 * w), floor(0.4 * h)))
        wS, hS = self.screen.get_size()
        x = 0.3
        y = 0.4
        screenCoord = self.coord2Screen(x,y)
        planetfase3 = Planet("teste2", planetafase3, 100001.0, screenCoord, 150.0)
        scene3.addPlanet(planetfase3)

        self.scenes.append(scene3)
        self.scenes.append(scene3)


    def coord2Screen(self, x, y):
        w, h = self.screen.get_size()
        xS = x*w
        yS = y*h
        return (int(xS), int(yS))
