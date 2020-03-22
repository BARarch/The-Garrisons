#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200322

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')




    fptr.write("Result goes here")
    fptr.write('\n')

    fptr.close()
