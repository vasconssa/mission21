import pygame
import prepare
from CircleProgressBar import CircleProgressBar

class Hud:
    def __init__(self):
        self.progBar = None
        self.color = (39, 95, 188)
        self.score = 10000
        self.createHud()
        self.font = prepare.FONTS["military_font_7"]

    def createHud(self):
        self.progBar = CircleProgressBar((150, 100))
        self.progBar.setPercentage(100)

    def draw(self, surface):
        self.progBar.draw(surface)
        text = str(self.score)
        font = pygame.font.Font(self.font, 40)
        tw, th = font.size(text)
        text = font.render(text, True, self.color)
        tx, ty = 1100 - tw/2.0, 50 - th/2.0
        surface.blit(text, (tx, ty))

    def updateFuel(self, percentage):
        self.progBar.setPercentage(percentage)

    def updateScore(self, score):
        self.score = score

