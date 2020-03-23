#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200322

def sumSubsets(arr, num):

    def sumSubsets_Help(arr, num, soln):

        if num == 0:
            return [soln, ]

        solns = []
        for i, val in enumerate(arr):
            if val <= num:

                solns += sumSubsets_Help(arr[i + 1:], num - val, soln + (val,))
                solns = sorted(list(set(solns)))
            else:
                return solns
        print("Main Return: " + str(solns))
        return solns

    res = sumSubsets_Help(arr, num, ())
    return list(map(list, res))

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = list_string_to_list(input())
    num = int(input())

    fptr.write(str(sumSubsets(arr, num)))
    fptr.write('\n')

    fptr.close()
