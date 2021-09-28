# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def run_dfs(board, i, j, sign):
            stack = [(i, j)]
            while len(stack):
                i, j = stack.pop()
                board[i][j] = sign

                if i-1 > 0 and board[i-1][j] == 'O':
                    stack.append((i-1, j))
                if j-1 > 0 and board[i][j-1] == 'O':
                    stack.append((i, j-1))
                if i+1 < len(board) and board[i+1][j] == 'O':
                    stack.append((i+1, j))
                if j+1 < len(board[i]) and board[i][j+1] == 'O':
                    stack.append((i, j+1))

        for i in [0, len(board)-1]:
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    run_dfs(board, i, j, 'o')

        for i in range(1, len(board)-1):
            for j in [0, len(board[i])-1]:
                if board[i][j] == 'O':
                    run_dfs(board, i, j, 'o')

        for i in range(1, len(board)-1):
            for j in range(1, len(board[i])-1):
                if board[i][j] == 'O':
                    run_dfs(board, i, j, 'X')

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'o':
                    board[i][j] = 'O'

        print([b for b in board])


if __name__ == '__main__':
    board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    print(Solution().solve(board))
