import pygame

class Button:

    def __init__(self, image, pos, callback):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.callback = callback

        # fill images with color - red, gree, blue
        self._images[0].fill((255,0,0))
        self._images[1].fill((0,255,0))
        self._images[2].fill((0,0,255))

        # get image size and position
        self._rect = pygame.Rect(position, size)

        # select first image
        self._index = 0

    def draw(self, screen):

        # draw selected image
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):

        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    self._index = (self._index+1) % 3 # change image
                    self.callback()

