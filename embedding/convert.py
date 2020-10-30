import pandas as pd
import csv
import numpy as np

words = pd.read_csv("vectors.txt", sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE, dtype={"Index": str})

words_matrix = words.to_numpy()

np.save("words.npy", words_matrix)
with open("words.txt", "w", encoding="utf-8") as file:
    i = 0
    for index, row in words.iterrows():
        if i == 5835:
            index = "null"
        if i == 18618:
            index = "nan"
            
        file.write(index)
        file.write("\n")
        i += 1
