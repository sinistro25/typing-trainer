import sys
import pygame as pg
import time

from pygame.locals import *
from config        import *
from text          import TextGenerator, drawText
from key_handler   import KeyHandler  

pg.init()

DSURF = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Typing Experience")

font = pg.font.Font('font/FiraCode-Bold.ttf', 32) 

def gen_set():
    text_gen = TextGenerator() 
    text   = "_".join(text_gen.gen())
    return KeyHandler(text)

handler = gen_set()

while True:
    
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == KEYDOWN and not handler.finished():
            key = pg.key.name(event.key)
            if key == "escape":
                handler = gen_set()
            else:
                handler.handle(key)
    DSURF.fill(BGCOLOR.value)
    
    drawText(DSURF, *handler.draw_text(), TEXTRECT , font)
    drawText(DSURF,*handler.draw_score(), SCORERECT, font)
    
    pg.display.update()
