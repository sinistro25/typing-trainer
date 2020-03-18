import sys
import pygame as pg
import time
from enum import Enum,auto

from pygame.locals import *
from config        import *
from text          import TextGenerator, drawText
import text
from key_handler   import KeyHandler


class Scene(Enum):
    MENU    = auto()
    TYPING  = auto()


def gen_set(kind):
    text_gen = TextGenerator(kind=kind) 
    text   = "_".join(text_gen.gen())
    return KeyHandler(text)


def typing_scene(DSURF, kind):
    global handler
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            key = pg.key.name(event.key)
            if "shift" in key:
                continue
            if not handler.finished():
                if KMOD_SHIFT & event.mod:
                    key = key.upper()
                handler.handle(key)
            if key == "escape":
                handler = gen_set(kind)
                
    DSURF.fill(BGCOLOR.value)
    
    drawText(DSURF, *handler.draw_text(), TEXTRECT , font)
    drawText(DSURF, *handler.draw_score(), SCORERECT, font)
    
    pg.display.update()

def menu_scene(DSURF):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
            
    font = pg.font.Font('font/FiraCode-Bold.ttf', 32) 
    padding = 30
    DSURF.fill(BGCOLOR.value)
    
    MENU1 = (WIDTH / 2 - font.size("Uniform")[0]-padding,HEIGHT/2 -font.size("Uniform")[1]-padding,100,100)
    MENU2 = (WIDTH / 2 + padding,HEIGHT/2 - font.size("Weighted")[1]-padding,100,100)
    MENU3 = (WIDTH / 2 - (font.size("Uniform")[0]+font.size("Digits")[0])/2-padding,HEIGHT/2 + padding,100,100)
    MENU4 = (WIDTH / 2 + (font.size("Reduced")[0]-font.size("Digits")[0])/2 + padding,HEIGHT/2 + padding,100,100)
    
    
    text1 = font.render("Uniform",False,Color.YELLOW.value)
    text2 = font.render("Weighted",False,Color.YELLOW.value)
    text3 = font.render("Digits",False,Color.YELLOW.value)
    text4 = font.render("Reduced",False,Color.YELLOW.value)
    DSURF.blit(text1,MENU1)
    DSURF.blit(text2,MENU2)
    DSURF.blit(text3,MENU3)
    DSURF.blit(text4,MENU4)
    pg.display.update()

if __name__ == '__main__':
    pg.init()

    DSURF = pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Typing Experience")

    font = pg.font.Font('font/FiraCode-Bold.ttf', 32) 
    scene = Scene.MENU
    kind = text.Kind.UNIFORM

    handler = gen_set(kind)

    while True:
        if scene == Scene.MENU:
            menu_scene(DSURF)
        elif scene == Scene.TYPING:
            typing_scene(DSURF,kind)
        
