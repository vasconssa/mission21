# Jogo em si
from Scene import Scene
from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
import pygame
from pygame.locals import *
from sys import exit
from Utils import Utils
import prepare
import state_machine
from CircleProgressBar import CircleProgressBar
from SceneManager import SceneManager

class Game(state_machine._State):
    """This State is updated while our game shows the splash screen."""
    def __init__(self):
        state_machine._State.__init__(self)


    def startup(self, now, persistant):
        self.scenes = SceneManager(pygame.display.get_surface()).scenes
        self.scene = self.scenes[0]
        self.clock = pygame.time.Clock()
        self.eventHandler = EventHandler()
        self.prog = None

        self.prog = CircleProgressBar((150, 150))

        # planets.append(planet1)

        # background = pygame.image.load("../assets/background.png").convert()
        # background = pygame.transform.scale(background, (1200, 900))

        # groups = pygame.sprite.Group()
        # players = pygame.sprite.Group()
        # player.planets = planets
        # groups.add(player)
        # players.add(player)
        # groups.add(planet)

    def update(self, keys, now):
        # screen.blit(background, (0,0))
        dt = self.clock.tick() / 1000.0
        # player.dt = dt

        # planet.render(screen)
        # planet1.render(screen)
        # player.render(screen)
        self.scene.update(dt)
        self.prog.setPercentage(50)
        # pygame.display.flip()


    def draw(self, surface, interpolate):
        self.scene.draw(surface)
        self.prog.draw(surface)


    def get_event(self, event):
        self.eventHandler.handleEvent(event, self.scene.player)


