import sys
import pygame as pg
import time
from enum import Enum,auto

from pygame.locals import *
from config        import *
from text          import TextGenerator
import text
from key_handler   import KeyHandler
from key_score import save_score, get_score_img
import scenes
from scenes import Scene
def gen_set(kind):
    text_gen = TextGenerator(kind=kind) 
    text   = "_".join(text_gen.gen())
    return KeyHandler(text)



if __name__ == '__main__':
    pg.init()
    pg.mixer.quit()
    pg.event.set_blocked(MOUSEMOTION)
    
    DSURF = pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Typing Experience")

    font = pg.font.Font('font/FiraCode-Bold.ttf', 32) 
    
    # Fake event to trigger first update of the screen
    pg.event.post(pg.event.Event(MOUSEMOTION))
    
    ctx = {"current_mode":0,
           "kind": None,
           "scene": Scene.MENU,
           "surface": DSURF,
           "handler": None,
           "font":font}

    while True:
        if ctx["kind"] is not None:
            ctx["handler"] = gen_set(ctx["kind"])
            ctx["kind"] = None
        if ctx["scene"] == Scene.MENU:
            scenes.menu(ctx)         
        elif ctx["scene"] == Scene.TYPING:
            scenes.typing(ctx)
        elif ctx["scene"] == Scene.SCORE:
            scenes.key_score(ctx)
            

        
