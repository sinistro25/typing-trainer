import pygame as game
from pygame.locals import MOUSEMOTION
from enum import Enum

# Window dimensions
game.init()
game.mixer.quit()
game.event.set_blocked(MOUSEMOTION)

info = game.display.Info()
HEIGHT = min(960, info.current_h)
WIDTH = min(1440, info.current_w)
# Text alignment
MARGIN = 70
TEXTRECT = (MARGIN, MARGIN, WIDTH-2*MARGIN, HEIGHT-2*MARGIN)
SCORERECT = (MARGIN, HEIGHT-2*MARGIN, WIDTH-2*MARGIN, 2*MARGIN)

# Logging Files
WPMLOGFILE = "log/wpm.txt"
ACCLOGFILE = "log/acc.txt"
KEYLOGFILE = "log/key_latency.pkl"

# Alphabets
ALPHABET = "abcdefghijklmnopqrstuvxwyz"
REDUCEDALPHABET = "bcdjkqtvxz"
DIGITS = "0123456789"


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (4, 80, 24)
    BLUE = (0, 0, 127)
    YELLOW = (255, 255, 0)
    GREY = (127, 127, 127)


# Background Color
BGCOLOR = Color.GREEN

# key_score.py
FIGURESIZE = (25, 10)
KEYSCOREIMG = "key_score.png"
CACHE_EXPIRES = 30

FONT = 'font/FiraCode-Bold.ttf'
FONTSIZE = 50
FONTANTIALIAS = True
