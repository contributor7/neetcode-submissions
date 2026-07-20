'''
map of all values and their indices
iterate through each key value to check if indices collide

check for empty rows or columns first

REVISED PLAN:
can make a map for each 3x3 and check it, then move on
if the index count is more than once (excluding '') then
dup and dont need to check diagonal
so make one map per 3x3 this way diagonals are considered
must check empty for each sub_square as well since you
can have a missing value in one square but not in entire
square at same time, so need to check each square
'''

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_uniques = defaultdict(set)
        c_uniques = defaultdict(set)
        n = len(board) # board will be len 9

        for starting_column in range(0, n, 3):
            for starting_row in range(0, n, 3):
                square_set = set()
                for r in range(starting_row, starting_row + 3):
                    for c in range(starting_column, starting_column + 3):
                        cell = board[r][c]
                        if cell == '.':
                            continue
                        if (cell in square_set
                            or cell in r_uniques[r]
                            or cell in c_uniques[c] ):
                                return False
                        square_set.add(cell)
                        r_uniques[r].add(cell)
                        c_uniques[c].add(cell)
            starting_row = 0 # reset to top row before starting column += 3
        return True