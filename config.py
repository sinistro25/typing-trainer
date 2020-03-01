from enum import Enum

HEIGHT = 600
WIDTH = 900
MARGIN = 70

TEXTRECT  = (MARGIN,MARGIN,WIDTH-2*MARGIN,HEIGHT-2*MARGIN)
SCORERECT = (MARGIN,HEIGHT-2*MARGIN,WIDTH-2*MARGIN,2*MARGIN)

WPMLOGFILE = "log/wpm.txt"
ACCLOGFILE = "log/acc.txt"
KEYLOGFILE = "log/key_latency.pkl"

ALPHABET = "abcdefghijklmnopqrstuvxwyz"

class Color(Enum):
    RED    = (255,0,0)
    GREEN  = (4,80,24)
    BLUE   = (0,0,127)
    YELLOW = (255,255,0)
  

BGCOLOR = Color.GREEN

