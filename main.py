import sys
import pygame as pg
import time
from enum import Enum,auto

from pygame.locals import *
from config        import *
from text          import TextGenerator, drawText
import text
from key_handler   import KeyHandler
from key_score import save_score, get_score_img


class Scene(Enum):
    MENU    = auto()
    TYPING  = auto()
    SCORE   = auto()


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
                return Scene.MENU
                
    DSURF.fill(BGCOLOR.value)
    
    drawText(DSURF, *handler.draw_text(), TEXTRECT , font)
    drawText(DSURF, *handler.draw_score(), SCORERECT, font)
    
    pg.display.update()
    
    return Scene.TYPING

def key_score_scene(DSURF):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return Scene.MENU
    image = get_score_img()
    DSURF.blit(image,(0,0,WIDTH,HEIGHT))
    pg.display.update()
    return Scene.SCORE


def menu_scene(DSURF):
    global current_mode
    global scene
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                current_mode = (current_mode+3)%4
            elif event.key == K_RIGHT:
                current_mode = (current_mode+1)%4
            elif event.key == K_DOWN:
                current_mode = (current_mode+2)%4
            elif event.key == K_UP:
                current_mode = (current_mode+2)%4
            elif event.key == K_RETURN:
                return Scene.TYPING,list(text.Kind)[current_mode]
            elif event.key == K_BACKQUOTE:
                return Scene.SCORE, None
            
    font = pg.font.Font('font/FiraCode-Bold.ttf', 32) 
    padding = 30
    DSURF.fill(BGCOLOR.value)
    
    MENU1 = (WIDTH / 2 - font.size("Uniform")[0]-padding,HEIGHT/2 -font.size("Uniform")[1]-padding,100,100)
    MENU2 = (WIDTH / 2 + padding,HEIGHT/2 - font.size("Weighted")[1]-padding,100,100)
    MENU3 = (WIDTH / 2 - (font.size("Uniform")[0]+font.size("Digits")[0])/2-padding,HEIGHT/2 + padding,100,100)
    MENU4 = (WIDTH / 2 + (font.size("Reduced")[0]-font.size("Digits")[0])/2 + padding,HEIGHT/2 + padding,100,100)
    
    
    text1 = font.render("Uniform",False,Color.YELLOW.value if current_mode != 0 else Color.RED.value)
    text2 = font.render("Weighted",False,Color.YELLOW.value if current_mode != 1 else Color.RED.value)
    text3 = font.render("Digits",False,Color.YELLOW.value if current_mode != 2 else Color.RED.value)
    text4 = font.render("Reduced",False,Color.YELLOW.value if current_mode != 3 else Color.RED.value)
    
    DSURF.blit(text1,MENU1)
    DSURF.blit(text2,MENU2)
    DSURF.blit(text3,MENU3)
    DSURF.blit(text4,MENU4)
    pg.display.update()
    
    return Scene.MENU,None

if __name__ == '__main__':
    pg.init()

    DSURF = pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Typing Experience")

    font = pg.font.Font('font/FiraCode-Bold.ttf', 32) 
    scene = Scene.MENU
    kind = None

    current_mode = 0

    while True:
        if scene == Scene.MENU:
            scene,kind = menu_scene(DSURF)
            if kind is not None:
                handler = gen_set(kind)
        elif scene == Scene.TYPING:
            scene = typing_scene(DSURF,kind)
        elif scene == Scene.SCORE:
            scene = key_score_scene(DSURF)

        
