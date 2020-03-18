from config import *
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pygame as pg
import lru
with open(KEYLOGFILE,"rb") as keylog:
    data = pickle.load(keylog)

def score():
    return softmax(15*calculate_avg_deviation())

def calculate_avg_deviation(N=100):
    avg = []
    for key in ALPHABET:
        key_data = data[key]
        key_data = key_data[max(0,len(key_data)-N):]
        avg.append(np.mean(key_data))
    avg = np.array(avg)
    return avg - avg.mean()


def softmax(array):
    tmp = np.exp(array)
    return tmp / tmp.sum()

def save_score():
    fig = plt.figure(figsize=FIGURESIZE)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.bar(list(ALPHABET),calculate_avg_deviation())
    ax2.bar(list(ALPHABET),score())
    fig.savefig("key_score.png")
    plt.close(fig)
    
@lru.lru_cache(maxsize=1,expires=CACHE_EXPIRES)
def get_score_img():
    save_score()
    return pg.image.load(KEYSCOREIMG)

