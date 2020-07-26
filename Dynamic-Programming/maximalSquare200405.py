def maximalSquare(matrix):
    # Approach: for each square compute is maximal square
    # Each Square will have three neighbors: to the right, to the lower right
    # and below.
    # Compute the maximal square as the (n + 1)^2 where n is the minimm maximal sqaure of all three neighboors]]
    # So if there is a square whose three neighboors are maximal each squares of 3 that
    # sqaures maximal value is now 16 (3 + 1)^2

    def maximalSquareHelp(matrix, r, c, H):
        if (r, c) in H:
            return H[(r, c)]

        if r >= len(matrix) or c >= len(matrix[0]):
            # Out of Bounds
            return 0

        if matrix[r][c] == "0":
            H[(r, c)] = 0
            return 0

        H[(r, c)] = min(maximalSquareHelp(matrix, r, c + 1, H),
                        maximalSquareHelp(matrix, r + 1, c, H),
                        maximalSquareHelp(matrix, r + 1, c + 1, H)) + 1

        return H[(r, c)]

    H = {}
    maximalSqRes = 0    

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            res = maximalSquareHelp(matrix, r, c, H)
            if res > maximalSqRes:
                maximalSqRes = res

    #print(H)
    return maximalSqRes ** 2

        
        

