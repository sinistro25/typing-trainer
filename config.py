from enum import Enum

# Window dimensions
HEIGHT  = 600
WIDTH   = 900

# Text alignment
MARGIN  = 70
TEXTRECT  = (MARGIN,MARGIN,WIDTH-2*MARGIN,HEIGHT-2*MARGIN)
SCORERECT = (MARGIN,HEIGHT-2*MARGIN,WIDTH-2*MARGIN,2*MARGIN)

# Logging Files
WPMLOGFILE = "log/wpm.txt"
ACCLOGFILE = "log/acc.txt"
KEYLOGFILE = "log/key_latency.pkl"

# Alphabets
ALPHABET    = "abcdefghijklmnopqrstuvxwyz"
DIGITS      = "0123456789"


class Color(Enum):
    RED    = (255,0,0)
    GREEN  = (4,80,24)
    BLUE   = (0,0,127)
    YELLOW = (255,255,0)
  
# Background Color
BGCOLOR = Color.GREEN

# key_score.py 
FIGURESIZE      = (9,6)
KEYSCOREIMG     = "key_score.png"
CACHE_EXPIRES   = 30