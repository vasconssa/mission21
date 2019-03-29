from RigidBody import RigidBody
from Vector2D import Vector2D
import pygame
from pygame.locals import *
from sys import exit

class EventHandler:
    def __init__(self):
        pass

    def handleEvent(self, event, player):
        evType = event.type
        if evType == QUIT:
            pygame.quit()
            exit()
        elif evType == KEYDOWN or evType == KEYUP:
            try:

                player.handleInput(event)
            except:
                a = "teste"
