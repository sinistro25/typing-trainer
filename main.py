import sys
import time
import traceback
import signal
from enum import Enum, auto

import pygame as game
from pygame.locals import *

import scenes
import text
from config import *
from key_handler import KeyHandler
from key_score import get_score_img, save_score
from scenes import Scene
from text import TextGenerator


def gen_set(kind):
    text_gen = TextGenerator(kind=kind)
    text = "_".join(text_gen.gen())
    return KeyHandler(text)


def sigterm_handler(_x, _trace):
    raise KeyboardInterrupt


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, sigterm_handler)

    screen = game.display.set_mode((WIDTH, HEIGHT))
    game.display.set_caption("Typing Trainer")

    font = game.font.Font(FONT, FONTSIZE)

    # Fake event to trigger first update of the screen
    game.event.post(game.event.Event(KEYDOWN, key=0))

    ctx = {"current_mode": 0,
           "kind": None,
           "scene": Scene.MENU,
           "surface": screen,
           "handler": None,
           "font": font}
    try:
        while True:
            if ctx["kind"] is not None:
                ctx["handler"] = gen_set(ctx["kind"])
            ctx["kind"] = None

            scenes.update(ctx)
    except Exception:
        print("\n\n\nA CRITICAL Error has occurred")
        traceback.print_exc()
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n\nUser requested interruption")
        print("Exiting...")
        sys.exit(0)
