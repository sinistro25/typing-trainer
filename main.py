import sys
import time
from enum import Enum,auto

import pygame as game
from pygame.locals import *

from config        import *
import text
from text          import TextGenerator
from key_handler   import KeyHandler
from key_score import save_score, get_score_img
import scenes
from scenes import Scene

def gen_set(kind):
    text_gen = TextGenerator(kind=kind) 
    text   = "_".join(text_gen.gen())
    return KeyHandler(text)

if __name__ == '__main__':
    game.init()
    game.mixer.quit()
    game.event.set_blocked(MOUSEMOTION)
    
    screen = game.display.set_mode((WIDTH,HEIGHT))
    game.display.set_caption("Typing Experience")

    font = game.font.Font('font/FiraCode-Bold.ttf', 32) 
    
    # Fake event to trigger first update of the screen
    game.event.post(game.event.Event(KEYDOWN,key=0))
    
    ctx = {"current_mode":0,
           "kind": None,
           "scene": Scene.MENU,
           "surface": screen,
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