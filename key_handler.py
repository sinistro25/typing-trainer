from config import *
import time

class KeyHandler():
    
    def __init__(self,text):
        self.text = text
        self.colors = [Color.YELLOW.value for _ in text]
        self.pos = 0
        self.time = 0
        self.mispels = 0
    
    def finished(self):
        return self.pos == len(self.text)
    
    def draw_text(self):
        return self.text, self.colors
    
    def draw_score(self):
        score = "  wpm:{:3.0f} | time:{:3.0f}s | acc:{:6.2f}%  ".format(self.wpm(), self.duration(), 100*self.acc())
        return score, [Color.YELLOW.value for _ in score]
    
    def writelog(self):
        with open(WPMLOGFILE,"a") as wpmlog:
            wpmlog.write(str(self.wpm())+"\n")
        with open(ACCLOGFILE,"a") as acclog:
            acclog.write(str(self.acc())+"\n")
    
    def handle(self,key):
        if self.time == 0:
            self.time = time.time() 
        if key == "space":
            key = "_"
        if self.text[self.pos] == key:
            self.colors[self.pos] = Color.BLUE.value
            self.pos += 1
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
        return max(0,l-self.mispels)/l
    