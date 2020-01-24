#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200118


import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):

    def encode(crossword):
        return list(map(list(), crossword))

    def decode(C):
        return list(map("".join(), C))

    def transpose(C):
        Ct = []

        for row in C:
            for col in row:
                

    return words.strip().split(';')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
