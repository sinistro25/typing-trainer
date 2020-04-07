from config import *
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pygame as pg
import lru

def score():
    return softmax(15*calculate_avg_deviation())

def calculate_avg(N=100):
    avg = []
    # Tries to read typing data, if it fails, defaults to a list with a zero
    # for every letter on the alphabet
    try:
        with open(KEYLOGFILE,"rb") as keylog:
            data = pickle.load(keylog)
    except FileNotFoundError:
        data = {key:[0] for key in ALPHABET}
    
    for key in ALPHABET:
        if key in data:
            key_data = data[key]
        else:
            key_data = [0]
        key_data = key_data[max(0,len(key_data)-N):]
        avg.append(np.mean(key_data))
    avg = np.array(avg)
    return avg


def calculate_avg_deviation(N=100):
    avg = calculate_avg(N)
    return avg - avg.mean()

def softmax(array):
    tmp = np.exp(array)
    return tmp / tmp.sum()

def save_score():
    fig = plt.figure(figsize=FIGURESIZE)
    fig.suptitle("Typer Stats")
    ax = fig.add_subplot(311)
    ax1 = fig.add_subplot(312)
    ax2 = fig.add_subplot(313)
    ax.bar(list(ALPHABET),calculate_avg())
    ax.set_ylabel("Avg latency (ms)")
    ax1.bar(list(ALPHABET),calculate_avg_deviation())
    ax1.set_ylabel("Avg latency deviation (ms)")
    ax2.bar(list(ALPHABET),score())
    ax2.set_ylabel("Relative difficulty")
    fig.savefig(KEYSCOREIMG)
    plt.close(fig)
    
@lru.lru_cache(maxsize=1,expires=CACHE_EXPIRES)
def get_score_img():
    save_score()
    return pg.image.load(KEYSCOREIMG)

