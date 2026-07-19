'''
map of all values and their indices
iterate through each key value to check if indices collide

check for empty rows or columns first
'''

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
            current = 0
            while current < len(board) # board will be len 9
            # can you do a for loop that increments by 3?
                for r in range(current, current + 3):
                    if not any(board[r]):
                        return False
                    for i in range(3):
                        # square_map[board[r][i]].append(i)
                        # if len[square_map[board[r][i]]] > 1:
                        #     return False
                        if board[r][i] in square_set:
                            return False
                        square_set.append(board[i])
                current += 3
            return True
        '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current = 0
        while current < len(board): # board will be len 9
            # can you do a for loop that increments by 3?
            square_set = set()
            for r in range(current, current + 3):
                if not any(board[r][:3]):
                    print('false board')
                    return False
                print('not false')
                for i in range(3):
                    # square_map[board[r][i]].append(i)
                    # if len[square_map[board[r][i]]] > 1:
                    #     return False
                    if board[r][i] in square_set:
                        print(square_set)
                        print('xx')
                        return False
                    print('xy')
                    if board[r][i] != '.':
                        square_set.add(board[r][i])
            current += 3
        return True