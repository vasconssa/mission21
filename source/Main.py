from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

display_width = 1200
display_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)


gameDisplay = pygame.display.set_mode((display_width, display_height),0,32)
pygame.display.set_caption('Mission21')
clock = pygame.time.Clock()



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def set_background(display):
    imgPath = '../assets/tela_inicial.png'

    background = Background(imgPath, [0, 0])

    display.fill([255,255,255])

    display.blit(background.image,background.rect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        set_background(gameDisplay)
        #gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        txt = largeText.render("Start",True,(red))
        TextSurf, TextRect = text_objects("Start", largeText)
        TextRect.center = ((display_width / 3), 3*(display_height / 4))
        gameDisplay.blit(txt, TextRect)
        pygame.display.update()
        clock.tick(15)


game_intro()

#pygame.quit()
#quit()