def climbingStaircase(n, k):
    def jumps(elm):
        return elm[0]
    
    def steps(elm):
        return elm[1]
    
    from collections import deque
    q = deque([([], 0), ])
    
    solns = []
    
    while q:
        s = q.pop()
        
        ## AutoSolution
        if steps(s) == n:
            solns.append(jumps(s))
        
        for i in range(k):
            i += 1
            
            if steps(s) + i == n:
                ## we have a solution
                solns.append(jumps(s) + [i, ])
            elif steps(s) + i < n:
                ## We have a partial soln
                q.append((jumps(s) + [i, ] ,steps(s) + i))
                
            
    return list(reversed(solns))

