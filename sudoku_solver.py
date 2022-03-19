# https://leetcode.com/problems/sudoku-solver/


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        grids_set = [set() for _ in range(9)]

        for i in range(9):
            vals_set = rows_set[i]
            for j in range(9):
                if board[i][j] != '.':
                    vals_set.add(board[i][j])

        for j in range(9):
            vals_set = cols_set[j]
            for i in range(9):
                if board[i][j] != '.':
                    vals_set.add(board[i][j])

        r = 0
        c = 0
        k = 0
        while r < 9:
            vals_set = grids_set[k]
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] != '.':
                        vals_set.add(board[i][j])
            k += 1
            c += 3
            if c >= 9:
                c = 0
                r += 3

        def run_recurrent(i, j):
            while i < 9:
                found = False
                while j < 9:
                    if board[i][j] == '.':
                        found = True
                        break
                    j += 1
                if found: break
                i += 1
                j = 0

            if i >= 9: return True

            ig = -1
            if 0 <= i < 3:
                ig = 0
            elif 3 <= i < 6:
                ig = 3
            else:
                ig = 6

            if 3 <= j < 6:
                ig += 1
            elif 6 <= j < 9:
                ig += 2

            for v in range(1, 10):
                if str(v) not in rows_set[i] and str(v) not in cols_set[j] and \
                   str(v) not in grids_set[ig]:
                    if i == 8 and j == 6 and v == 1:
                        print()
                    board[i][j] = str(v)
                    rows_set[i].add(str(v))
                    cols_set[j].add(str(v))
                    grids_set[ig].add(str(v))
                    next_j = j + 1
                    next_i = i
                    if next_j == 9:
                        next_j = 0
                        next_i += 1
                    if next_i >= 9:
                        return True

                    if run_recurrent(next_i, next_j):
                        return True

                    board[i][j] = '.'
                    rows_set[i].remove(str(v))
                    cols_set[j].remove(str(v))
                    grids_set[ig].remove(str(v))

            return False

        print(run_recurrent(0, 0))


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    print(board)
