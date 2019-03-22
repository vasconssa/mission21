from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
import pygame
from pygame.locals import *
from sys import exit
from source.Utils import Utils


class Teste():
    def launch(self):
        # pygame.init()

        screen = pygame.display.set_mode((Utils.DISPLAY_WIDTH, Utils.DISPLAY_HEIGHT), 0, 32)
        player = Player((50,50))
        planets = []

        planeta = pygame.image.load("../assets/greenPlanet.png").convert_alpha()
        rect = planeta.get_rect()
        w, h = rect.width, rect.height
        planeta = pygame.transform.scale(planeta, (floor(0.3*w), floor(0.3*h)))
        planet = RigidBody("teste2", planeta, 100001.0, (600, 450), 150.0)

        player.surf = screen
        planet.surf = screen
        planets.append(planet)
        # planets.append(planet1)
        clock = pygame.time.Clock()

        background = pygame.image.load("../assets/background.png").convert()
        background = pygame.transform.scale(background, (1200, 900))
        eventHandler = EventHandler()
        groups = pygame.sprite.Group()
        players = pygame.sprite.Group()
        player.planets = planets
        groups.add(player)
        players.add(player)
        groups.add(planet)

        while True:

            for event in pygame.event.get():
                eventHandler.handleEvent(event, player)

            screen.blit(background, (0,0))
            dt = clock.tick()/1000.0
            player.dt = dt

            # planet.render(screen)
            # planet1.render(screen)
            # player.render(screen)
            players.update()
            groups.draw(screen)



            pygame.display.flip()
