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


from source import state_machine
class Game(state_machine._State):
    """This State is updated while our game shows the splash screen."""
    def __init__(self):
        state_machine._State.__init__(self)
        self.scene = Scene(pygame.display.get_surface())
        self.clock = pygame.time.Clock()
        self.eventHandler = EventHandler()

    def startup(self, now, persistant):
        # pygame.init()

        # screen = pygame.display.set_mode((Utils.DISPLAY_WIDTH, Utils.DISPLAY_HEIGHT), 0, 32)
        # player = Player((50,50))
        # planets = []

        planeta = pygame.image.load("../assets/greenPlanet.png").convert_alpha()
        rect = planeta.get_rect()
        w, h = rect.width, rect.height
        planeta = pygame.transform.scale(planeta, (floor(0.3 * w), floor(0.3 * h)))
        planet = RigidBody("teste2", planeta, 100001.0, (600, 450), 150.0)
        self.scene.addPlanet(planet)

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
        # pygame.display.flip()


    def draw(self, surface, interpolate):
        self.scene.draw()


    def get_event(self, event):
        self.eventHandler.handleEvent(event, self.scene.player)


