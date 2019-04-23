# Menu inicial, pode conter alguma configuração


import pygame as pg
import state_machine,prepare,menu_helpers


FONT = pg.font.Font(prepare.FONTS["military_font_7"], 60) ###
SMALL_FONT = pg.font.Font(prepare.FONTS["military_font_7"], 32) ###

OPTIONS = ["START", "QUIT"]
#OPTIONS = ["START","CHOOSE MAP", "OPTIONS", "QUIT"]

HIGHLIGHT_COLOR = (108, 148, 136)

#Placement and spacing constants.
OPT_Y = 450
OPT_CENTER = 450
OPT_SPACER = 59
SLOT_SPACER = 125
# MAIN_TOPLEFT = (100, 40)
MAIN_TOPLEFT = (0,0)

NAME_START = (320, 115)
PLAYER_START = (170, 95)
ITEM_IMAGES = (625, 95)
ITEM_START = (ITEM_IMAGES[0]+85, ITEM_IMAGES[1])
ITEM_SPACER = 60
STAT_START = (805, 128)
STAT_SPACER = 75
STAT_TEXT_SPACE = 45


class Select(state_machine._State):
    """
    This State is updated while our game shows the player select screen.
    This state is made up of four substates to organize updating;
    Options, SelectRegister, Delete, and Confirm.
    """
    def __init__(self):
        state_machine._State.__init__(self)
        self.next = "GAME"
        self.timeout = 15
        self.state_machine = state_machine.StateMachine()

    def startup(self, now, persistant):
        """
        Recreate the substates and substate dict when this state starts up.
        """
        state_machine._State.startup(self, now, persistant)
        state_dict = {"OPTIONS" : Options(),
                      # "SELECT/REGISTER" : SelectRegister(),
                      # "DELETE" : Delete(),
                      # "CONFIRM" : Confirm()}
                      }

        self.state_machine.setup_states(state_dict, "OPTIONS")

    def cleanup(self):
        """
        Add variables that should persist to the self.persist dictionary.
        Then reset State.done to False.
        """
        self.done = False
        self.state_machine.done = False
        # regi = self.state_machine.state_dict["SELECT/REGISTER"]
        options = self.state_machine.state_dict["OPTIONS"]
        # self.persist["save_slot"] = regi.index
        # self.persist["player"] = options.players[regi.index]
        return self.persist

    def update(self, keys, now):
        """
        Updates the Cabbages; then the current substate; and finally
        checks to see if the game state or substate needs to change.
        """
        self.state_machine.update(keys, now)
        check_timeout = now-self.start_time > 1000.0*self.timeout
        if self.state_machine.state_name == "OPTIONS" and check_timeout:
            self.next = "TITLE"
            self.done = True
        elif self.state_machine.done:
            self.next = self.state_machine.state.next
            self.done = True

    def draw(self, surface, interpolate):
        """
        Fill the screen; let the substates handle their own rendering;
        then draw the Cabbages.
        """
        surface.fill(prepare.BACKGROUND_COLOR)
        self.state_machine.state.draw(surface, interpolate)

    def get_event(self, event):
        """
        Get events from Control.
        """
        if event.type == pg.KEYDOWN:
            self.start_time = pg.time.get_ticks()
        self.state_machine.get_event(event)


class SelectState(menu_helpers.BasicMenu):
    """Base class for all Select state substates."""
    def __init__(self, option_length):
        menu_helpers.BasicMenu.__init__(self, option_length)
        self.rendered = {}



class Options(SelectState):
    """
    Essentially the main menu state of the whole game.
    """
    def __init__(self):
        SelectState.__init__(self, 4)
        self.options = self.make_options(FONT, OPTIONS, OPT_Y, OPT_SPACER,OPT_CENTER)
        self.image = pg.Surface(prepare.SCREEN_SIZE).convert()
        self.image.set_colorkey(prepare.COLOR_KEY)
        self.image.fill(prepare.COLOR_KEY)

    def startup(self, now, persistant):
        """Reload all players and rerender their names on startup."""
        state_machine._State.startup(self, now, persistant)
        self.image.fill(prepare.COLOR_KEY)



    def cleanup(self):
        """
        Add variables that should persist to the self.persist dictionary.
        Then reset State.done to False.
        """
        self.done = False
        self.persist["options_bg"] = self.image
        return self.persist

    def pressed_enter(self):
        """Enter next substate or view the controls screen on enter."""
        self.next = OPTIONS[self.index]
        if self.next == "DELETE":
            if not all(player=="EMPTY" for player in self.players):
                self.done = True
        elif self.next == "OPTIONS":
            pass
            # self.quit = True
        elif self.next=='START':
            self.next = 'GAME'
            self.quit = True
            self.done = True
        else: self.done=True

    def draw(self, surface, interpolate):
        """
        Blit the base image and options to a seperate surface for later use.
        Then blit that surface and the players to the screen.
        """
        self.image.blit(prepare.GFX["assets"]["tela_inicial"], MAIN_TOPLEFT)
        # for name_info in self.names:
        #     self.image.blit(*name_info)
        for i,val in enumerate(OPTIONS):
            which = "selected" if i==self.index else "unselected"
            msg, rect = self.options[which][i]
            self.image.blit(msg, rect)
        surface.blit(self.image, (0,0))
        # for i,player_sprite in enumerate(self.players):
        #     self.draw_player(surface, player_sprite, i)
'''

class Confirm(SelectState):
    """
    Select substate that updates when the user is asked to confirm the
    deletion of a character.
    """
    def __init__(self):
        self.box_image = prepare.GFX["misc"]["delete"]
        centerx = prepare.SCREEN_RECT.centerx
        top = MAIN_TOPLEFT[1]+130
        self.rect = self.box_image.get_rect(centerx=centerx, top=top)
        SelectState.__init__(self, 2)
        self.options = self.make_options(SMALL_FONT, ["Confirm", "Cancel"],
                                         self.rect.y+130, 35)
        self.player = None

    def startup(self, now, persistant):
        """
        Make options default to Cancel to be polite.
        Set the currently selected player's hit_state so they damage strobe.
        """
        state_machine._State.startup(self, now, persistant)
        del_index = self.persist["del_index"]
        self.player = self.persist["players"][del_index]
        self.player.hit_state = True
        self.index = 1

    def draw(self, surface, interpolate):
        """
        Draw the background, players, delete window and options.
        """
        surface.blit(self.persist["options_bg"], (0,0))
        for i,player_sprite in enumerate(self.persist["players"]):
            redraw = i == self.persist["del_index"]
            self.draw_player(surface, player_sprite, i, redraw)
        surface.blit(self.box_image, self.rect)
        for i in (0,1):
            which = "selected" if i==self.index else "unselected"
            msg, rect = self.options[which][i]
            surface.blit(msg, rect)


    def pressed_enter(self):
        """
        Return to menu on 'Cancel'; set player to 'dead' on 'Confirm'.
        """
        if not self.index:
            self.player.action_state = "dead"
        else:
            self.pressed_exit()

    def update(self, keys, now):
        """
        If a player deletion has been confirmed and death animation completed,
        return to menu.
        # """
        # if self.player.death_anim.done:
        #     self.save_change()
        #     self.pressed_exit()
        pass

    def get_event(self, event):
        """Don't process events if a player deletion has been confirmed."""
        if self.player.action_state != "dead":
            SelectState.get_event(self, event)

    def pressed_exit(self):
        """Return to options menu."""
        self.done = True
        self.next = "OPTIONS"
'''
