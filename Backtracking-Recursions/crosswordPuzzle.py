#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200118


import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):

    ## To Test Transpose            
    #print("Original")
    #print_crossword(crossword)
    #print()
    #print("Transposed")
    #print_crossword(transpose(crossword))
    #print()

    # To Test Fit word
    #print(fit_word("XXare", 'are'))

    def print_crossword(crossword):
        for row in crossword:
            print(row)

    def encode(crossword):
        return list(map(list, crossword))

    def decode(C):
        return list(map("".join(), C))

    def transpose_endcoded(C):
        Ci = [(x for x in row) for row in C]
        return [list(map(next, Ci)) for i in C[0]]

    def transpose(crossword):
        Ci = [(x for x in row) for row in crossword]
        return [''.join(list(map(next, Ci))) for i in crossword[0]]

    def fit_word(row, word):
        for i, letter in enumerate(row):
            if word == '':
                if letter == '-':
                    return None  # The feild it too wide
            #print(i, end='\t')
            #print(letter)
            elif letter == "-" or letter == word[0]:
                row = row[:i] + word[0] + row[i + 1:]
                word = word[1:]

        if word == '':
            return row
        else:
            return None

    def try_word(crossword, word):
        ## Run until the first success
        ## If not return None

        for i, row in enumerate(crossword):
            res = fit_word(row, word)
            if res:
                return crossword[:i] + [res, ] + crossword[i + 1:]

        for i, row in enumerate(transpose(crossword)):
            res = fit_word(row, word)
            if res:
                return transpose(transpose(crossword)[:i] + [res, ] + transpose(crossword)[i + 1:])

        return None

    def crosswordPuzzle_Help(crossword, words):           
        if words == []:
            return crossword
        
        if crossword == None:
            return None

        #print_crossword(crossword)
        #print(words)

        wordSet = words[:]
        for word in words:
            wordSet.remove(word)
            res = crosswordPuzzle_Help(try_word(crossword, word), wordSet)
            if res:
                return res
            wordSet = words[:]
            #print("Bactrack To:")
            #print_crossword(crossword)
            #print(words)
            #print() 


        return None

    return crosswordPuzzle_Help(crossword, words.split(";"))

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
