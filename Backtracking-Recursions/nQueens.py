def nQueens(n):
    # What is a viable solution for each colunm and colunm value
    # What is the rejection criteria, how do we implement it?
    def nQueensHelp(n, viable, right, up, down):
        # That prune set has three components right, up, and down
        if len(viable) == n:
            return [viable, ]
        solns = []
        viables = {x for x in range(1, n + 1)} - (right | up | down) 
        for x in viables:
            solns += nQueensHelp(   n, 
                                    viable + [x, ], 
                                    right | {x}, 
                                    {y - 1 for y in up} | {x - 1}, 
                                    {y + 1 for y in down} | {x + 1}) 
        return solns

    return list(sorted(nQueensHelp(n, [], {0}, {0}, {n + 1})))