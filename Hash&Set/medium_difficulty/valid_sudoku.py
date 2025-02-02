from typing import List


class Solution:
    # Question: 36

    # 7ms Beats 39.90%
    # Time Complexity: O(1)  
    # Space Complexity: O(1)

    # Only using O(81) becuase the board is 9X9

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #row
        for i in range(9):
            row_set = set()
            for j in range(9):
                item = board[i][j]
                if item in row_set:
                    return False
                elif item != '.':
                    row_set.add(item)
            
        # col
        for i in range(9):
            col_set = set()
            for j in range(9):
                item = board[j][i]
                if item in col_set:
                    return False
                elif item != '.':
                    col_set.add(item)
                    
        # box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        item = board[box_row + i][box_col + j]
                        if item != '.':
                            if item in box_set:
                                return False
                            box_set.add(item)

        return True