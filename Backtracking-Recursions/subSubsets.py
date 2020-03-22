#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200322

def sumSubsets(arr, num):

    def sumSubsets_Help(arr, num, soln):
        
        print("New Branch num = " + str(num))

        if num == 0:
            #print("returning")
            return set((soln, ))

        if len(arr) == 0:
            return set()

        solns = set()
        print("soln: " + str(soln) + " num: " + str(num) + " arr: " + str(arr))
        for i, val in enumerate(arr):
            if val <= num:
                # Viable Solution
                #print('Viable')
                solns.union(sumSubsets_Help(arr[i + 1:], num - val, soln + (val,)))
            else:
                #print('Not Viable')
                return solns

        return solns

    #print("Initial In: ", end='')
    #print(arr)
    #print("num = " + str(num) )

    res = sumSubsets_Help(arr, num, ())
    print(res)
    return [[]]

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')




    fptr.write("Result goes here")
    fptr.write('\n')

    fptr.close()
