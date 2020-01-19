#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200118


import os
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
