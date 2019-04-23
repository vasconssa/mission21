from GameObject import GameObject
from RigidBody import RigidBody
from Vector2D import Vector2D
from math import *
import pygame
from pygame.locals import *
from abc import ABC, ABCMeta, abstractmethod
import prepare

BLACK = (0,0,0)


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

    def addImage(self, key, imageName):
        image = prepare.GFX["assets"][imageName].convert_alpha()
        image = pygame.transform.scale(image, (60, 60))
        image = pygame.transform.rotate(image, -90)
        self.images[key] = image

class Player(RigidBody):

    def __init__(self, initialPos):

        self.alive = True
        self.final = False

        self.imageMap = ImageMap()
        # self.imageMap.addImage("normal", "../assets/spaceShip.png")
        # self.imageMap.addImage("fwd", "../assets/spaceShipFwd.png")
        # self.imageMap.addImage("rvs", "../assets/spaceShipRv.png")
        # self.imageMap.addImage("left", "../assets/spaceShipLft.png")
        # self.imageMap.addImage("right", "../assets/spaceShipRgt.png")

        self.imageMap.addImage("normal", "spaceShip")
        self.imageMap.addImage("fwd", "spaceShipFwd")
        self.imageMap.addImage("rvs", "spaceShipRv")
        self.imageMap.addImage("left", "spaceShipLft")
        self.imageMap.addImage("right", "spaceShipRgt")

        pos = (initialPos[0], initialPos[1])
        super(Player, self).__init__("Player", self.imageMap.images["normal"], 1.0, pos, 1.0)
        self.inputHandler = InputHandler()
        self.power = 0
        self.ignite = False
        self.fuel = 100.0
        self.rotateAngle = 0
        self.dt = 30/100.0
        self.planets = None
        self.mask = self.make_mask()
        self.death_anim = None
        self.got_hit=False

        self.prepare_death_animation()




    def setForce(self, power):
        self.internalForce = power

    def setRotate(self, angleStep):
        self.rotateAngle = angleStep

    def handleInput(self, event):
        self.inputHandler.handle(self, event)

    def update(self):
        if(self.final):
            return
        if self.alive:
            self.rotate(self.rotateAngle)

            if self.ignite:
                super(Player, self).update(self.dt, self.planets)
            if self.internalForce != 0:
                self.ignite = True
                self.fuel -= 0.1

                self.rotate(self.rotateAngle)
                super(Player, self).update(self.dt, self.planets)
        else:
            if self.death_anim is not None:
                self.death_anim.update()






    def reset(self):
        #TODO melhorar
        self.health = prepare.MAX_HEALTH


    def make_mask(self):
        """Create a collision mask for the player."""
        #TODO melhorar essa máscara
        temp = pygame.Surface((prepare.CELL_SIZE)).convert_alpha()
        temp.fill((0, 0, 0, 0))
        temp.fill(pygame.Color("white"), (10, 20, 30, 30))
        return pygame.mask.from_surface(temp)


    def collide_with_solid(self, cancel_knock=True):
        """Called from level when the player walks into a solid tile."""
        #TODO aqui entra a animação de explosão
        if not self.alive :
            self.death_anim = Explosion(self.rect.center)
        elif self.final:
            pass

        print("Colision")


    def got_hit(self, enemy):
        """Called on collision with enemy."""
        # if not self.hit_state:
        #     damage = max(enemy.attack-self.defense, 1)
        #     self.health = max(self.health-damage, 0)
        #     self.hit_state = tools.Timer(50, 10)
        #     knock_dir = self.get_collision_direction(enemy)
        #     self.knock_state = (knock_dir, tools.Timer(100, 1))
        pass



    def prepare_death_animation(self):
        for i in range(9):
            filename = 'regularExplosion0{}'.format(i)
            img = prepare.GFX['assets'][filename]
            img.set_colorkey(BLACK)
            img = pygame.transform.scale(img, (75, 75))
            Explosion.explosion_anim.append(img)



class Explosion(pygame.sprite.Sprite):
    explosion_anim = []

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = Explosion.explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.done =False
        self.configure_sound()

    def configure_sound(self):
        player = prepare.MUSIC["explosion_player"]
        player = pygame.mixer.Sound(player)
        player.play(0)

    def update(self):
        now = pygame.time.get_ticks()
        if (now - self.last_update) > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(Explosion.explosion_anim):
                self.kill()
                self.done = True
            else:
                center = self.rect.center
                self.image = Explosion.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        else:
            self.done = True
            pass
