# Imagem inicial do jogo

import pygame as pg
import state_machine,tools,prepare


SCROLL_SPEED = 2
DELAY_UNTIL_SCROLL = 10000 #Miliseconds.
SKY_COLOR = (66, 120, 150)
SKY_RECT = pg.Rect(0, 0, 1200, 514)
BACkGROUND_RECT = pg.Rect(0, 0, 1200, 514)
STAR_COLORS = [(74,156,173), (40, 40, 50), (250, 230, 250)]
NIGHT_SKY_COLOR = (0, 0, 30)

class Title(state_machine._State):
    """This State is updated while our game shows the splash screen."""
    def __init__(self):
        state_machine._State.__init__(self)
        self.timer = None
        self.background = prepare.GFX['assets']['tela_inicial']


    def startup(self, now, persistant):
        self.persist = persistant
        self.start_time = now
        self.timer = tools.Timer(DELAY_UNTIL_SCROLL, 1)
        self.timer.check_tick(now)
        self.elements = self.make_elements()

    def make_elements(selfself):
        group = pg.sprite.LayeredUpdates()
        group.add(AnyKey(),layer=1)
        return group


    def update(self, keys, now):
         self.now = now
        # self.elements.update(now, self.scrolling)
        # if self.scrolling:
        #     self.star_field.update(now)
        # elif self.timer.check_tick(now):
        #     self.scrolling = True


    def draw(self, surface, interpolate):
        surface.fill(NIGHT_SKY_COLOR)
        # if self.scrolling:
            # self.star_field.draw(surface)
        surface.blit(self.background, BACkGROUND_RECT)
        self.elements.draw(surface)



    def get_event(self, event):
        """Get events from Control.  Currently changes to next state on any key
                press.
                """
        if event.type == pg.KEYDOWN:
            self.next = "SELECT"
            self.done = True




class AnyKey(pg.sprite.Sprite):
    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.raw_image = render_font("military_font_7", 30,
                                 "[Pressione alguma tecla]", (255,255,0))
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
