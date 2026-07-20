'''
map of all values and their indices
iterate through each key value to check if indices collide

check for empty rows or columns first
'''

from collections import defaultdict

class Solution:
    def testisValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            if not any(r):
                return False
        for c in zip(*board):
            if not any(c):
                return False

        c_map = {}
        r_map = {}
        # for r in board:
        #     for cell in r:
        #         r_map[cell] = r_map.get(cell, 0) + 1

        # for c in board:

        def map_indices(my_list, my_map):
            for i, el in enumerate(my_list):
                print(i, el)
                my_map[el].append(i)

        for r in board:
            map_indices(r, r_map)
        for c in zip(*board):
            map_indices(c, c_map)

        def check_dups(my_map):
            for key in my_map:
                if len(my_map[key]) > 1:
                    return False
        # does not work since duplicates
        # outside of 3x3 is fine
        
        check_dups(r_map)
        check_dups(c_map)

        # missing case is when there are 
        # duplicates in diagonal of a 3x3 specifically
        
        # can make a map for each 3x3 and check it, then move on
        # if the index count is more than once (excluding '') then
        # dup and dont need to check diagonal
        # so make one map per 3x3 this way diagonals are considered
        # must check empty for each sub_square as well since you
        # can have a missing value in one square but not in entire
        # square at same time, so need to check each square
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_uniques = defaultdict(set)
        c_uniques = defaultdict(set)

        def my_any(iterable):
            for val in iterable:
                if val != '.' and val:
                    return True
            return False
        for starting_column in range(0,len(board), 3):
            for starting_row in range(0, len(board),3): # board will be len 9
                square_set = set()
                for r in range(starting_row, starting_row + 3):
                    for c in range(starting_column, starting_column + 3):
                        cell = board[r][c]
                        if board[r][c] in square_set or cell in r_uniques[r] or cell in c_uniques[c]:
                            return False
                        if board[r][c] != '.':
                            square_set.add(board[r][c])
                            r_uniques[r].add(board[r][c])
                            c_uniques[c].add(board[r][c])
            starting_row = 0
        return True