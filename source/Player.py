from GameObject import GameObject
from RigidBody import RigidBody
from Vector2D import Vector2D
from math import *
import pygame
from pygame.locals import *
from abc import ABC, ABCMeta, abstractmethod

class InputHandler:
    def __init__(self):
        self.command = 0
        self.commands = {
                K_LEFT : RotateLeftCommnad(0.5),
                K_RIGHT: RotateRightCommnad(0.5),
                K_UP: ForwardThrustCommand(50),
                K_DOWN: ReverseThrustCommand(50)
        }

    def handle(self, player, event):
        if event.type == KEYDOWN:
            self.commands[event.key].execute(player)
        elif event.type == KEYUP:
            self.commands[event.key].undo(player)

class Command:
    def __init__(self):
        self.active = False

    @abstractmethod
    def execute(self, player):
        pass

    @abstractmethod
    def undo(self):
        pass

class RotateLeftCommnad(Command):
    def __init__(self, angleStep):
        self.angleStep = angleStep

    def execute(self, player):
        player.setRotate(self.angleStep)
        player.originalImage = player.imageMap.images["left"]

    def undo(self, player):
        player.setRotate(0)
        player.originalImage = player.imageMap.images["normal"]

class RotateRightCommnad(Command):
    def __init__(self, angleStep):
        self.angleStep = -angleStep

    def execute(self, player):
        player.setRotate(self.angleStep)
        player.originalImage = player.imageMap.images["right"]

    def undo(self, player):
        player.setRotate(0)
        player.originalImage = player.imageMap.images["normal"]

class ForwardThrustCommand(Command):
    def __init__(self, power):
        self.power = power

    def execute(self, player):
        player.setForce(self.power)
        player.originalImage = player.imageMap.images["fwd"]

    def undo(self, player):
        player.setForce(0)
        player.originalImage = player.imageMap.images["normal"]

class ReverseThrustCommand(Command):
    def __init__(self, power):
        self.power = -power

    def execute(self, player):
        player.setForce(self.power)
        player.originalImage = player.imageMap.images["rvs"]

    def undo(self, player):
        player.setForce(0)
        player.originalImage = player.imageMap.images["normal"]

class ImageMap:
    def __init__(self):
        self.images = {}

    def addImage(self, key, imagePath):
        image = pygame.image.load(imagePath).convert_alpha()
        image = pygame.transform.scale(image, (60, 60))
        image = pygame.transform.rotate(image, -90)
        self.images[key] = image

class Player(RigidBody):

    def __init__(self, initialPos):
        self.imageMap = ImageMap()
        self.imageMap.addImage("normal", "../assets/spaceShip.png")
        self.imageMap.addImage("fwd", "../assets/spaceShipFwd.png")
        self.imageMap.addImage("rvs", "../assets/spaceShipRv.png")
        self.imageMap.addImage("left", "../assets/spaceShipLft.png")
        self.imageMap.addImage("right", "../assets/spaceShipRgt.png")
        pos = (initialPos[0], initialPos[1])
        super(Player, self).__init__("Player", self.imageMap.images["normal"], 1.0, pos, 1.0)
        self.inputHandler = InputHandler()
        self.power = 0
        self.rotateAngle = 0
        self.dt = 30/100.0
        self.planets = None


    def setForce(self, power):
        self.internalForce = power

    def setRotate(self, angleStep):
        self.rotateAngle = angleStep

    def handleInput(self, event):
        self.inputHandler.handle(self, event)

    def update(self):
        self.rotate(self.rotateAngle)
        super(Player, self).update(self.dt, self.planets)

    # def render(self, screen):
        # selfrender(screen)
