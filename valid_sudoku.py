# https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(9):
            vals_set = set()
            for j in range(9):
                if board[i][j] in vals_set:
                    return False
                elif board[i][j] != '.':
                    vals_set.add(board[i][j])

        # check col
        for j in range(9):
            vals_set = set()
            for i in range(9):
                if board[i][j] in vals_set:
                    return False
                elif board[i][j] != '.':
                    vals_set.add(board[i][j])

        # check 3x3 grid
        r = 0
        c = 0
        while c < 9:
            vals_set = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] in vals_set:
                        return False
                    elif board[i][j] != '.':
                        vals_set.add(board[i][j])

            r += 3
            if r >= 9:
                r = 0
                c += 3

        return True


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]
    board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]
    print(Solution().isValidSudoku(board))
