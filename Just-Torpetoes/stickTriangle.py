#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200118

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    from collections import deque

    S = deque(sorted(sticks))
    A = S.pop()
    B = S.pop()
    C = S.pop()

    if B + C > A:
        return [C, B, A]

    while S:
        A = B
        B = C
        C = S.pop()

        if B + C > A:
            return [C, B, A]

    return [-1, ]
     


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
