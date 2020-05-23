import random
from config import *
word_file = open("corpi/top10000.txt", "r")
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


def array_generator(list_indexes, size=20):
    tmp = []
    for _ in range(size):
        word = random.choice(words)
        index = random.choice(list_indexes)
        tmp.append(f"{word}[{index}]")
    return tmp


def int_comparison_generator(size=20):
    tmp = []
    for _ in range(size):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        op = ""
        if a < b:
            op = random.choice(["<", "<=", "!="])
        elif a == b:
            op = random.choice(["==", "<=", ">="])
        elif a > b:
            op = random.choice([">", ">=", "!="])
        tmp.append(f"{a}{op}{b}")
    return tmp


def assignment_generator(values, size=40):
    tmp = []
    for _ in range(size):
        word = random.choice(words)
        value = random.choice(values)
        tmp.append(f"{word}={value}")
    return tmp


def enclose(array, braces="[{(", antibraces="]})"):
    tmp = []
    for i in range(len(array)):
        x = random.randint(0, len(braces)-1)
        tmp.append(f"{braces[x]}{array[i]}{antibraces[x]}")
    return tmp


def code_generator(size=10):
    tmp = []
    tmp += assignment_generator(array_generator([i for i in range(size)], size=size) +
                                enclose(int_comparison_generator(size=size), "(", ")"))
    tmp += int_comparison_generator(size=size)
    random.shuffle(tmp)
    return tmp[:size]


if __name__ == "__main__":
    code = code_generator(size=10)
    print(code)
    print(len(code))
