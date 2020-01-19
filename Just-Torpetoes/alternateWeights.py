#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200118

from cs_utils import list_string_to_list
import os

def alternatingSums(a):
    teamA = 0
    teamB = 0
    for i, weight in enumerate(a):
        if i % 2 == 0:
            teamA += weight
        else:
            teamB += weight
            
    return [teamA, teamB]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list_string_to_list(input())    

    fptr.write(str(alternatingSums(a)))
    fptr.write('\n')

    fptr.close()
