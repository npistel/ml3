import pandas as pd
import csv
import numpy as np
from operator import itemgetter

words_matrix = np.load("words.npy")

words = []
with open("words.txt", "r", encoding="utf-8") as file:
    for line in file:
        words.append(line.strip())

def vec(w):
    return words_matrix[words.index(w)]

def find_closest_word(v, first=0, last=9):
    diff = words_matrix - v
    delta = np.sum(diff * diff, axis=1)
    sort = np.argsort(delta)

    return itemgetter(*sort[first:last])(words)


v = vec("merkel") - vec("deutschland") + vec("italien")
print(find_closest_word(v))

#print(find_closest_word(vec("merkel")))