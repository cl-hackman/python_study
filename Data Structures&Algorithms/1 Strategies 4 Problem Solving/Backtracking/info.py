# Read the "backtracking.pdf"
'''
Backtracking -> retrace one's steps (if we reach a state where we conclude that this specific option does not give the required solution)
It checks errors that can arise from Brute Force operations.
It's a technique saying keep doing this, once you get stuck, go back one step and start again from there.
Use this if you're given a problem where you have to make certain choices whereby every choice you make limits the number
of future choices you can make: 
How to place 8 queens on a chess board (8*8) without each queen attacking one another? when you you put the 1st queen on the board, you're now
limited to 7 choices or ways 
'''
# Below is an example of finding all possible order of arrangements of a given set of letters. When we choose a pair we apply backtracking to verify if that exact pair
# has already been created or not. If not already created, the pair is added to the answer list else it is ignored.


def permute(list, s):
    if list == 1:   # Back Case: we want a pair for the elements so if 1, we return s or anything like None, -1
        return s
    else:
        return [y + x for y in permute(1, s) for x in permute(list - 1, s)]


print(permute(1, ["a", "b", "c"]))
print(permute(2, ["a", "b", "c"]))

# From the pdf


class NQueens:
    def __init__(self, n):
        self.n = n      # attribute the parameter so we can use it throughout all the methods
        # chess board is 8 x 8 where 8 = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end='')
                else:
                    print(" - ", end='')

    def is_place_safe(self, row_index, col_index):
        for i in range(self.n):
            # from line 28, rows = 0 so if a row = 1, then that row is not empty so return False
            if self.chess_table[row_index][i] == 1:
                return False

        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:   # Base Case
                break
            if self.chess_table[i][j] == 1:
                return False    # backtracking
            j = j - 1   # limiting the number of choices

        j = col_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False    # backtracking
            j = j - 1

        return True

    def solve(self, col_index):
        if col_index == self.n:
            return True

        for row_index in range(self.n):
            if self.is_place_safe(row_index, col_index):
                self.chess_table[row_index][col_index] = 1
                if self.solve(col_index+1):
                    return True  # backtracking
                self.chess_table[row_index][col_index] = 0

        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("No solution exists for the problem")


queens = NQueens(8)
queens.solve_NQueens()
