import sys
import pygame as pg
from vector import Vector
from button import Button
from os.path import exists

movement = {pg.K_LEFT: Vector(-1, 0),   # dictionary to map keys to Vector velocities
            pg.K_RIGHT: Vector(1, 0),
            pg.K_UP: Vector(0, -1),
            pg.K_DOWN: Vector(0, 1)
            }
  
def check_keydown_events(event, settings, ship):
    key = event.key
    if key == pg.K_SPACE: 
        ship.shooting = True
    elif key in movement.keys(): 
        ship.vel += settings.ship_speed_factor * movement[key]

def check_keyup_events(event, ship):
    key = event.key
    if key == pg.K_SPACE: ship.shooting = False
    elif key == pg.K_ESCAPE: 
        ship.vel = Vector()   # Note: Escape key stops the ship

def check_events(settings, ship):
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN: check_keydown_events(event=event, settings=settings, ship=ship)
        elif event.type == pg.KEYUP: 
            check_keyup_events(event=event, ship=ship)

def clamp(posn, rect, settings):
    left, top = posn.x, posn.y
    width, height = rect.width, rect.height
    left = max(0, min(left, settings.screen_width - width))
    top = max(0, min(top, settings.screen_height - height))
    return Vector(x=left, y=top), pg.Rect(left, top, width, height)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("images/font.ttf", size)

def get_highscore():
        f_exists = exists('highscore.txt')
        if f_exists:
            with open('highscore.txt', 'r') as f:
                highscore = f.readline()
            return highscore
        return 0

def start_screen():
        pg.init()
        SCREEN = pg.display.set_mode((1280, 900))
        pg.display.set_caption("Menu")
        BG = pg.image.load("images/Background.png")
        while True:
            SCREEN.blit(BG, (0, 0))
            MENU_MOUSE_POS = pg.mouse.get_pos()
            MENU_TEXT = get_font(60).render("SPACE INVADERS", True, "#00FF00")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 50))
            HIGHSCORE_TEXT = get_font(60).render("HIGHSCORE:" + get_highscore(), True, "#00FF00")
            HIGHSCORE_RECT = MENU_TEXT.get_rect(center=(640, 800))
            SCREEN.blit(pg.image.load('images/alien__00.png'), (460, 100))
            ALIEN0_TEXT = get_font(30).render("= 50", True, "#00FF00")
            ALIEN0_RECT = MENU_TEXT.get_rect(center=(1050, 200))
            SCREEN.blit(ALIEN0_TEXT, ALIEN0_RECT)
            SCREEN.blit(pg.image.load('images/alien__10.png'), (460, 200))
            ALIEN1_TEXT = get_font(30).render("= 50", True, "#00FF00")
            ALIEN1_RECT = MENU_TEXT.get_rect(center=(1050, 300))
            SCREEN.blit(ALIEN1_TEXT, ALIEN1_RECT)
            SCREEN.blit(pg.image.load('images/alien__20.png'), (460, 300))
            ALIEN2_TEXT = get_font(30).render("= 50", True, "#00FF00")
            ALIEN2_RECT = MENU_TEXT.get_rect(center=(1050, 400))
            SCREEN.blit(ALIEN2_TEXT, ALIEN2_RECT)
            SCREEN.blit(pg.image.load('images/alien__30.png'), (460, 400))
            ALIEN3_TEXT = get_font(30).render("= ???", True, "#00FF00")
            ALIEN3_RECT = MENU_TEXT.get_rect(center=(1050, 500))
            SCREEN.blit(ALIEN3_TEXT, ALIEN3_RECT)
            PLAY_BUTTON = Button(image=pg.image.load("images/Play Rect.png"), pos=(640, 600), 
                                text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
            SCREEN.blit(MENU_TEXT, MENU_RECT)
            SCREEN.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)
            for button in [PLAY_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        return
            pg.display.update()
