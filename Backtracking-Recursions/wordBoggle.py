#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200325
def wordBoggle(board, words):
    def neighbors_of_pos(pos):
        yield((pos[0] - 1, pos[1] - 1))
        yield((pos[0], pos[1] - 1))
        yield((pos[0] + 1, pos[1] - 1))

        yield((pos[0] - 1, pos[1]))
        yield((pos[0] + 1, pos[1]))

        yield((pos[0] - 1, pos[1] + 1))
        yield((pos[0], pos[1] + 1))
        yield((pos[0] + 1, pos[1] + 1))

    def first_letter(board, word):
        # Search whole board from Viable Solution
        if word == "":
            return True
        #print("First Letter: " + word[0])
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    print("First Letter: " + word[0] + " " +str((i, j)))
                    soln = remaining_letters(board, word[1:], neighbors_of_pos((i,j)), {(i, j): word[0]})
                    if soln:
                        return True
        return False

    def remaining_letters(board, word, neighbors, visited):
        # Search only Neighbors for Viable Solution       
        if word == "":
            return True
        print("Next Letter: " + word[0])
        for i, j in neighbors:
            if (i, j) not in visited:
                if i >= 0 and i < len(board):
                    if j >= 0 and j < len(board[0]):
                        if board[i][j] == word[0]:
                            visited[(i, j)] = word[0]
                            print("Next Letter: " + word[0] + " " +str((i, j)))
                            soln = remaining_letters(board, word[1:], neighbors_of_pos((i, j)), visited)
                            if soln:
                                return True
                            else:
                                del visited[(i,j)]
        print(visited)
        return False

    def test_word(word):
        return first_letter(board, word)
        
    return sorted(list(filter(test_word, words)))

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board = list_string_to_list(input())
    words = list_string_to_list(input())

    fptr.write(str(wordBoggle(board, words)))
    fptr.write('\n')

    fptr.close()
