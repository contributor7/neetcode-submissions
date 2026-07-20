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
        squares = defaultdict(set)

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '.':
                    continue
                if (cell in squares[(r // 3, c // 3)]
                    or cell in r_uniques[r]
                    or cell in c_uniques[c]):
                        return False
                squares[(r // 3, c // 3)].add(cell)
                r_uniques[r].add(cell)
                c_uniques[c].add(cell)
        return True