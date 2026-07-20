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

        '''
        sub_square = [[board[i] for i in board[r]] for r in board]
            for r in range(len(sub_square)): # len should be 3
                for i, cell in enumerate(r):
                    sub_square[cell].append(i)

        l = 0
        for row in range(l, l + 3):
            square = []
            square

            square_set = set()
            starting_row = 0
            while starting_row < len(board) # board will be len 9
            # can you do a for loop that increments by 3?
                for r in range(starting_row, starting_row + 3):
                    if not any(board[r]):
                        return False
                    for i in range(3):
                        # square_map[board[r][i]].append(i)
                        # if len[square_map[board[r][i]]] > 1:
                        #     return False
                        if board[r][i] in square_set:
                            return False
                        square_set.append(board[i])
                starting_row += 3
            return True
        '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        starting_row = 0
        starting_column = 0
        r_uniques = defaultdict(set)
        c_uniques = defaultdict(set)

        def my_any(iterable):
            for val in iterable:
                if val != '.' and val:
                    return True
            return False
        while starting_column < len(board):
            while starting_row < len(board): # board will be len 9
                # can you do a for loop that increments by 3?
                square_set = set()
                for r in range(starting_row, starting_row + 3):
                    # if not my_any(board[r]):
                    #     print('false board')
                    #     print(square_set, r, starting_column)
                    #     return False
                    # print('not false')
                    for c in range(starting_column, starting_column + 3):
                        # square_map[board[r][i]].append(i)
                        # if len[square_map[board[r][i]]] > 1:
                        #     return False
                        cell = board[r][c]
                        if board[r][c] in square_set or cell in r_uniques[r] or cell in c_uniques[c]:
                            print(square_set)
                            print('xx')
                            return False
                        # print('xy')
                        if board[r][c] != '.':
                            square_set.add(board[r][c])
                            r_uniques[r].add(board[r][c])
                            c_uniques[c].add(board[r][c])
                starting_row += 3
            # print(starting_column)
            starting_column += 3
            starting_row = 0
        return True