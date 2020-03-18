import random
from config import *
word_file = open("corpi/top10000.txt","r")
words = word_file.read().split("\n")

def words_by_letter(string):
    filtered = []
    for word in words:
        for letter in string:
            if letter in word:
                filtered.append(word)
    return filtered


def digit_generator():
    lst = []
    for i in range(100):
        digit = ""
        for _ in range(5):
            digit += random.choice(DIGITS)
        lst.append(digit)
    return lst