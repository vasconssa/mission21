
"""
Tela de transição
The splash screen of the game. The first thing the user sees.
"""

import pygame as pg

import prepare, state_machine


class WinScreen(state_machine._State):
    """This State is updated while our game shows the splash screen."""
    def __init__(self):
        state_machine._State.__init__(self)
        self.next = "TITLE"
        self.timeout = 5
        self.alpha = 0
        self.alpha_speed  = 2  #Alpha change per frame
        self.image = prepare.GFX["assets"]['tela_inicial'].copy().convert()
        self.image.set_alpha(self.alpha)
        # self.rect = self.image.get_rect(center=prepare.SCREEN_RECT.center)
        self.rect = pg.Rect(0, 0, 1200, 514)

        self.text = render_font("military_font_7", 30,
                                     "Congratulations! You have completed all missions!", (255, 255, 0))

    def update(self, keys, now):
        """Updates the splash screen."""
        self.now = now
        self.alpha = min(self.alpha+self.alpha_speed, 255)
        self.image.set_alpha(self.alpha)
        if self.now-self.start_time > 1000.0*self.timeout:
            self.done = True

    def draw(self, surface, interpolate):
        surface.fill(prepare.BACKGROUND_COLOR)
        surface.blit(self.image, self.rect)
        # self.elements.draw(surface)
        center = (prepare.SCREEN_RECT.centerx / 3, 650)
        surface.blit(self.text,center)

    def get_event(self, event):
        """
        Get events from Control. Changes to next state on any key press.
        """
        self.done = event.type == pg.KEYDOWN
    def make_elements(self):
        group = pg.sprite.LayeredUpdates()
        raw_image = render_font("military_font_7", 30,
                                     "Congratulations! You have completed all missions!", (255, 255, 0))
        group.add(raw_image, layer=1)
        return group

    def render_font(font, size, msg, color=(255, 255, 255)):
        """
        Takes the name of a loaded font, the size, and the color and returns
        a rendered surface of the msg given.
        """
        selected_font = pg.font.Font(prepare.FONTS[font], size)
        return selected_font.render(msg, 1, color)

class Congratulations(pg.sprite.Sprite):
    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.raw_image = render_font("military_font_7", 30,
                                 "Congratulations! You have completed all missions!", (255,255,0))
        self.null_image = pg.Surface((1,1)).convert_alpha()
        self.null_image.fill((0,0,0,0))
        self.image = self.raw_image
        center = (prepare.SCREEN_RECT.centerx/2, 650)
        self.rect = self.image.get_rect(center=center)
        self.blink = False
        self.timer = tools.Timer(200)

    def update(self, now, *args):
        if self.timer.check_tick(now):
            self.blink = not self.blink
        self.image = self.raw_image if self.blink else self.null_image


def render_font(font, size, msg, color=(255,255,255)):
        """
        Takes the name of a loaded font, the size, and the color and returns
        a rendered surface of the msg given.
        """
        selected_font = pg.font.Font(prepare.FONTS[font], size)
        return selected_font.render(msg, 1, color)
