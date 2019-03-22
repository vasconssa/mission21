from GameObject import GameObject
from math import *
from RigidBody import RigidBody
from Player import Player
from EventHandler import EventHandler
from Vector2D import Vector2D
import pygame
from pygame.locals import *
from sys import exit
from source.Utils import Utils as Utils,IMG_PATH
from source.test import Teste

class Main:
    def __init__(self):
        self.gameDisplay = pygame.display.set_mode((Utils.DISPLAY_WIDTH, Utils.DISPLAY_HEIGHT),0,32)



    def launch_game(self):
        pygame.display.set_caption("Mission21")
        self.clock = pygame.time.Clock()

        self.game_intro()

        self.start_button = None

    def colorize(self,image, newColor):
        """
        Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
        original).
        :param image: Surface to create a colorized copy of
        :param newColor: RGB color to use (original alpha values are preserved)
        :return: New colorized Surface instance
        """
        image = image.copy()

        # zero out RGB values
        image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        # add in new RGB values
        image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

        return image

    def set_start_menu(self):
        imgPath = IMG_PATH.BACKGROUND_IMG_PATH

        background = Background(imgPath, [0, 0])
        # self.fill([255,255,255])
        self.gameDisplay.blit(background.image, background.rect)

        startPath = IMG_PATH.START_IMG_PATH

        img = pygame.image.load(startPath)

        img = self.colorize(img,(190,0,0))

        pygame.transform.scale(img,(70,50))

        rect = img.get_rect()

        rect.center = ((Utils.DISPLAY_WIDTH / 3), 3 * (Utils.DISPLAY_HEIGHT / 4))

        self.start_button = self.gameDisplay.blit(img,rect)

    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if(self.start_button.collidepoint(event.pos)):
                        intro = False
                        #TODO diminuir tempo de espera entre o clique no menu e o começo do jogo

                        #TODO capturar clique dentro do retângulo do botão de start
                        break


            self.set_start_menu()

            pygame.display.update()
            self.clock.tick(15)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()

main = Main()

main.launch_game()

Teste().launch()




# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()





#pygame.quit()
#quit()