from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
import pygame
from pygame.locals import *
from abc import ABC, ABCMeta, abstractmethod

class AbstractScene():
    def __init__(self, screen):
        self.screen = screen
        self.nextScene = None

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self):
        pass

