import pygame
import os
from Utils import Utils as Utils,ASSETS_PATH
from test import Teste
import prepare
import tools
from states import title,splash,select,game

def __configure_sound():
    pygame.mixer.init()
    player = prepare.MUSIC["music_background"]
    player = pygame.mixer.Sound(player)
    player.play(-1)

__configure_sound()

from states import title,splash,select,game, win_screen
app = tools.Control(prepare.ORIGINAL_CAPTION)
state_dict = {"SPLASH"   : splash.Splash(),
              "TITLE"    : title.Title(),
              "SELECT"   : select.Select(),
              # "REGISTER" : register.Register(),
              # "CONTROLS" : viewcontrols.ViewControls(),
              "GAME"     : game.Game(),
               "WINSCREEN"     : win_screen.WinScreen()
              }
app.state_machine.setup_states(state_dict, "SPLASH")


app.main()






#
# # Game Initialization
# pygame.init()
#
# # Center the Game Application
# os.environ['SDL_VIDEO_CENTERED'] = '1'
#
# # Game Resolution
# screen_width = Utils.DISPLAY_WIDTH
# screen_height = Utils.DISPLAY_HEIGHT
# screen = pygame.display.set_mode((screen_width, screen_height))
#
#
# # Text Renderer
# def text_format(message, textFont, textSize, textColor):
#     newFont = pygame.font.Font(textFont, textSize)
#     newText = newFont.render(message, 0, textColor)
#
#     return newText
#
#
# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)
# gray = (50, 50, 50)
# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# yellow = (255, 255, 0)
#
# # Game Fonts
# font = ASSETS_PATH.START_MENU_FONT_PATH
#
# # Game Framerate
# clock = pygame.time.Clock()
# FPS = 30
#
#
# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#
#
# backgroundImage = Background(ASSETS_PATH.BACKGROUND_IMG_PATH,[0, 0])
#
#
# def draw_text(surf, text, size, x, y,textColor = white):
#     ## selecting a cross platform font to display the score
#     newFont = pygame.font.Font(font, size)
#     text_surface = newFont.render(text, 0, textColor)
#
#     # text_surface = newFont.render(text, True, WHITE)       ## True denotes the font to be anti-aliased
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x, y)
#     surf.blit(text_surface, text_rect)
#
# # Main Menu
# def main_menu():
#     menu = True
#     selected = "start"
#
#     while menu:
#         # for event in pygame.event.get():
#         event = pygame.event.poll()
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 selected = "start"
#             elif event.key == pygame.K_DOWN:
#                 selected = "quit"
#             if event.key == pygame.K_RETURN:
#                 if selected == "start":
#                     print("Start")
#                     screen.fill(black)
#
#                     screen.blit(backgroundImage.image, backgroundImage.rect)
#                     loading = text_format("Loading...", font, 90, red)
#                     rect = loading.get_rect()
#                     draw_text(screen,"Loading...",90,screen_width/3,3*screen_height/4,red)
#                     pygame.display.update()
#                     break
#                 if selected == "quit":
#                     pygame.quit()
#                     quit()
#
#         # Main Menu UI
#         screen.fill(blue)
#         title = text_format("Mission 21", font, 90, yellow)
#         if selected == "start":
#             text_start = text_format("START", font, 75, red)
#         else:
#             text_start = text_format("START", font, 75, white)
#         if selected == "quit":
#             text_quit = text_format("QUIT", font, 75, red)
#         else:
#             text_quit = text_format("QUIT", font, 75, white)
#
#         title_rect = title.get_rect()
#         start_rect = text_start.get_rect()
#         quit_rect = text_quit.get_rect()
#
#         # Main Menu Text
#         screen.blit(backgroundImage.image,backgroundImage.rect)
#         # screen.blit(title.py, (screen_width / 2 - (title_rect[2] / 2), 80))
#
#         screen.blit(text_start, [(Utils.DISPLAY_WIDTH / 4), 7 * (Utils.DISPLAY_HEIGHT / 10)])
#         screen.blit(text_quit, [(Utils.DISPLAY_WIDTH / 4), 8.2 * (Utils.DISPLAY_HEIGHT / 10)])
#         pygame.display.update()
#         clock.tick(FPS)
#         pygame.display.set_caption("Mission21")
#
#     Teste().launch(screen)
# #Initialize the Game
# main_menu()
# pygame.quit()
# quit()




