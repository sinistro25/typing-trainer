from config import *
import time
import pickle


class KeyHandler():

    def __init__(self, text):
        self.text = text
        self.colors = [Color.YELLOW.value for _ in text]
        self.pos = 0
        self.time = 0
        self.time_last_click = 0
        self.mispels = 0

        try:
            self.key_deltas = pickle.load(open(KEYLOGFILE, "rb"))
        except FileNotFoundError:
            self.key_deltas = {}

    def finished(self):
        return self.pos == len(self.text)

    def draw_text(self):
        return self.text, self.colors

    def draw_score(self):
        score = "  wpm:{:3.0f} | time:{:3.0f}s | acc:{:6.2f}%  ".format(
            self.wpm(), self.duration(), 100*self.acc())
        return score, [Color.YELLOW.value for _ in score]

    def writelog(self):
        with open(WPMLOGFILE, "a+") as wpmlog:
            wpmlog.write(str(self.wpm())+"\n")
        with open(ACCLOGFILE, "a+") as acclog:
            acclog.write(str(self.acc())+"\n")
        with open(KEYLOGFILE, "wb+") as keylog:
            pickle.dump(self.key_deltas, keylog)

    def handle(self, key):
        if self.time == 0:
            self.time = time.time()
            self.time_last_click = time.time()
        if key == "space":
            key = "_"
        if self.text[self.pos] == key:
            self.colors[self.pos] = Color.BLUE.value
            self.pos += 1

            new_click_time = time.time()
            delta = new_click_time - self.time_last_click
            self.time_last_click = new_click_time
            if key in self.key_deltas:
                self.key_deltas[key].append(delta)
            else:
                self.key_deltas[key] = [delta]

            if self.finished():
                self.time = time.time() - self.time
                self.writelog()
        else:
            self.mispels += 1
            self.colors[self.pos] = Color.RED.value

    def duration(self):
        if self.finished() or self.time == 0:
            return self.time
        else:
            return time.time() - self.time

    def wpm(self):
        duration = self.duration()
        if duration == 0:
            return 0
        return (60*self.pos) / (5*duration)

    def acc(self):
        l = len(self.text)
        return max(0, l-self.mispels)/l

    def shift_key(self, c):
        m = {
            "0": ")",
            "1": "!",
            "2": "@",
            "3": "#",
            "4": "$",
            "5": "%",
            "6": "^",
            "7": "&",
            "8": "*",
            "9": "(",
            "[": "{",
            "]": "}",
            ",": "<",
            ".": ">",
            "=": "+",
            ";": ":",
            "'": "\"",
            "\\": "|",
        }
        if c in m:
            return m[c]
        else:
            return c.upper()
