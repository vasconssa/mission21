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
from source import menu_helpers
import math

SMALL_FONT = pygame.font.Font(prepare.FONTS["military_font_7"], 32) ###

PLAY_AGAIN_OPTIONS = ["Try Again", "Quit"]
PLAY_AGAIN = prepare.GFX["assets"]["cross"]
PLAY_AGAIN_NEXT = ["GAME", "SELECT"]

PLAY_AGAIN_CENTERS = [(prepare.PLAY_RECT.centerx, 175),
                      (prepare.PLAY_RECT.centerx, 525)]
IRIS_MIN_RADIUS = 30
IRIS_TRANSPARENCY = (0, 0, 0, 175)
IRIS_STRIP_RECT = pygame.Rect(prepare.PLAY_RECT.w-5, 0, 5, prepare.PLAY_RECT.h)
IRIS_STRIP_COLOR = (255, 73, 73)

class Game(state_machine._State):
    """This State is updated while our game shows the splash screen."""
    def __init__(self):
        state_machine._State.__init__(self)


    def startup(self, now, persistant):
        self.scenes = SceneManager(pygame.display.get_surface()).scenes
        self.scene = self.scenes[0]
        self.clock = pygame.time.Clock()
        self.eventHandler = EventHandler()
        self.iris = None

        self.play_again = None


        # planets.append(planet1)

        # background = pygame.image.load("../assets/background.png").convert()
        # background = pygame.transform.scale(background, (1200, 900))

        # groups = pygame.sprite.Group()
        # players = pygame.sprite.Group()
        # player.planets = planets
        # groups.add(player)
        # players.add(player)
        # groups.add(planet)

    def cleanup(self):
        self.done = False

    def update(self, keys, now):
        # screen.blit(background, (0,0))
        dt = self.clock.tick() / 1000.0
        # player.dt = dt

        # planet.render(screen)
        # planet1.render(screen)
        # player.render(screen)
        self.scene.update(dt)

        if not self.scene.player.alive:
            self.update_on_death()


        # pygame.display.flip()


    def draw(self, surface, interpolate):
        self.scene.draw(surface)
        if not self.scene.player.alive and self.iris:
            self.iris.draw(surface)
            if self.iris.done:
                self.play_again.draw(surface, interpolate)


    def get_event(self, event):
        if self.iris and self.iris.done:
            self.play_again.get_event(event)
        else:
            self.eventHandler.handleEvent(event, self.scene.player)


    def update_on_death(self):
        if self.scene.player.death_anim.done:
            if not self.iris:
                x, y = self.scene.player.rect.center
                self.iris = IrisIn((x, y + 10))
                center = self.scene.player.rect.centery < prepare.PLAY_RECT.centery
                self.play_again = PlayAgain(PLAY_AGAIN_CENTERS[center])
            self.iris.update()
            if self.iris.done:
                self.play_again.update()
                if self.play_again.done:
                    self.done = True
                    self.next = self.play_again.next
                    self.scene.player.reset()



class IrisIn(object):
    """
    Class for displaying and updating an iris that closes on the player
    upon death.
    """
    def __init__(self, center, rect=prepare.PLAY_RECT):
        self.center = center
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert_alpha()
        self.rad = self.get_start_radius()
        self.speed = 4.0 #Rate radius shrinks in pixels per frame.
        self.done = False

    def get_start_radius(self):
        """
        Find the required max radius of the circle based on center distance
        from each corner.
        """
        max_radius = 0
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            x, y = getattr(self.rect, attribute)
            vec = self.center[0]-x, self.center[1]-y
            distance_to_corner = math.hypot(*vec)
            if distance_to_corner > max_radius:
                max_radius = distance_to_corner
        return max_radius

    def update(self):
        """
        Decrease the radius size appropriately; set done to True if radius has
        reached IRIS_MIN_RADIUS; recreate image.
        """
        self.rad = max(self.rad-self.speed, IRIS_MIN_RADIUS)
        if self.rad == IRIS_MIN_RADIUS:
            self.done = True
        self.image.fill(IRIS_TRANSPARENCY)
        self.image.fill(IRIS_STRIP_COLOR, IRIS_STRIP_RECT)
        pygame.draw.circle(self.image, (0,0,0,0), self.center, int(self.rad))

    def draw(self, surface):
        """Standard draw method."""
        surface.blit(self.image, self.rect)


class PlayAgain(menu_helpers.BasicMenu):
    """A class for the simple menu that runs on game over."""
    def __init__(self, center):
        menu_helpers.BasicMenu.__init__(self, 2)
        self.rect = PLAY_AGAIN.get_rect(center=center)
        self.options = self.make_options(SMALL_FONT, PLAY_AGAIN_OPTIONS,
                                         self.rect.y+130, 35,
                                         prepare.PLAY_RECT.centerx)
        # skel_pos = [(self.rect.x+100, self.rect.y+100),
        #            (self.rect.right-100, self.rect.y+100)]
        # self.skeletons = pygame.sprite.Group(RetrySkeleton(p) for p in skel_pos)

    def update(self):
        """Update the animated skeletons."""
        # self.skeletons.update(now)
        pass
    def draw(self, surface, interpolate):
        """Draw window options and skeletons to the screen."""
        surface.blit(PLAY_AGAIN, self.rect)
        for i,val in enumerate(PLAY_AGAIN_OPTIONS):
            which = "selected" if i==self.index else "unselected"
            msg, rect = self.options[which][i]
            surface.blit(msg, rect)
        # self.skeletons.draw(surface)

    def pressed_enter(self):
        """Set next to the selected item."""
        self.done = True
        self.next = PLAY_AGAIN_NEXT[self.index]





