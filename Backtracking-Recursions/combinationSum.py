#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200325

def combinationSum(a, summ):
    def combinationSumHelp(a, summ, viable):
        if summ == 0:
            return (viable, )

        solns = []
        for i, num in enumerate(a):
            if num <= summ:
                solns += combinationSumHelp(a[i:], summ - num, viable + (num, ))

        return solns

    def collapse(soln):
        return  "(" + " ".join(map(str, soln)) + ")"

    res = combinationSumHelp(sorted(a), summ, ())

    if res:
        return "".join(map(collapse, sorted(list(set(res)))))
    else:
        return "Empty"
    

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list_string_to_list(input())
    summ = int(input())

    fptr.write(combinationSum(a, summ))
    fptr.write('\n')

    fptr.close()
