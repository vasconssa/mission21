from Vector2D import Vector2D
import pygame
from pygame.locals import *

class GameObject(pygame.sprite.Sprite):

    def __init__(self, name, image, pos):
        pygame.sprite.Sprite.__init__(self)

        self.originalImage = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.name = name
        self.imageAngle = 1
        self.heading = Vector2D(1.0, 0.0)
        self.pos = Vector2D(pos)
        self.vel = Vector2D(0.0, 0.0)
        self.surf = None 

    def setPos(newPos):
        self.pos = Vector2D(newPos)

    def setVel(newVel):
        self.vel = Vector2D(newVel)

    def rotateAroundCenter(self, angle, surf):
        # calcaulate the axis aligned bounding box of the rotated image
        x, y = self.pos
        w, h       = self.originalImage.get_size()
        originPos = (w/2, h/2)
        pos        = pygame.math.Vector2(x, y)
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot
        pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move   = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

        # get a rotated image
        rotated_image = pygame.transform.rotate(self.originalImage, angle)
        self.rect.topleft = origin
        # surf.blit(rotated_image, origin)
        pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)
        head = self.pos + self.heading*50
        pygame.draw.line(surf, (255, 200, 0), (pos[0], pos[1]), (head[0], head[1]), 2)
        pygame.draw.line(surf, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
        pygame.draw.line(surf, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
        return rotated_image

    def update(self):
        x, y = self.pos
        width, height = self.image.get_size()
        self.image = self.rotateAroundCenter(self.imageAngle, self.surf)
        # self.rect.center =  (x - width/2.0, y - height/2.0)



