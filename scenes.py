import sys
from enum import Enum,auto

import pygame as pg
from pygame.locals import *
from config import *

import text
from key_score import get_score_img

class Scene(Enum):
    MENU    = auto()
    TYPING  = auto()
    SCORE   = auto()


def typing(ctx):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            key = pg.key.name(event.key)
            if "shift" in key:
                continue
            if not ctx["handler"].finished():
                if KMOD_SHIFT & event.mod:
                    key = key.upper()
                ctx["handler"].handle(key)
            if key == "escape":
                ctx["scene"],ctx["kind"] = Scene.MENU, None
                
    ctx["surface"].fill(BGCOLOR.value)
    font = ctx["font"]
    text.draw(ctx["surface"], *ctx["handler"].draw_text(), TEXTRECT , font)
    text.draw(ctx["surface"], *ctx["handler"].draw_score(), SCORERECT, font)
    
    pg.display.update()
    
    return Scene.TYPING

def key_score(ctx):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                ctx["scene"] = Scene.MENU
                return
    image = get_score_img()
    ctx["surface"].blit(image,(0,0,WIDTH,HEIGHT))
    pg.display.update()


def menu(ctx):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                ctx["current_mode"] = (ctx["current_mode"]+3)%4
            elif event.key == K_RIGHT:
                ctx["current_mode"] = (ctx["current_mode"]+1)%4
            elif event.key == K_DOWN:
                ctx["current_mode"] = (ctx["current_mode"]+2)%4
            elif event.key == K_UP:
                ctx["current_mode"] = (ctx["current_mode"]+2)%4
            elif event.key == K_RETURN:
                ctx["scene"], ctx["kind"] = Scene.TYPING,list(text.Kind)[ctx["current_mode"]]
                return
            elif event.key == K_BACKQUOTE:
                ctx["scene"] = Scene.SCORE
                return
            
    font = ctx["font"]
    padding = 30
    ctx["surface"].fill(BGCOLOR.value)
    
    MENU1 = (WIDTH / 2 - font.size("Uniform")[0]-padding,HEIGHT/2 -font.size("Uniform")[1]-padding,100,100)
    MENU2 = (WIDTH / 2 + padding,HEIGHT/2 - font.size("Weighted")[1]-padding,100,100)
    MENU3 = (WIDTH / 2 - (font.size("Uniform")[0]+font.size("Digits")[0])/2-padding,HEIGHT/2 + padding,100,100)
    MENU4 = (WIDTH / 2 + (font.size("Reduced")[0]-font.size("Digits")[0])/2 + padding,HEIGHT/2 + padding,100,100)
    
    
    text1 = font.render("Uniform",False,Color.YELLOW.value if ctx["current_mode"] != 0 else Color.RED.value)
    text2 = font.render("Weighted",False,Color.YELLOW.value if ctx["current_mode"] != 1 else Color.RED.value)
    text3 = font.render("Digits",False,Color.YELLOW.value if ctx["current_mode"] != 2 else Color.RED.value)
    text4 = font.render("Reduced",False,Color.YELLOW.value if ctx["current_mode"] != 3 else Color.RED.value)
    
    ctx["surface"].blit(text1,MENU1)
    ctx["surface"].blit(text2,MENU2)
    ctx["surface"].blit(text3,MENU3)
    ctx["surface"].blit(text4,MENU4)
    pg.display.update()
    
    ctx["scene"] =  Scene.MENU
