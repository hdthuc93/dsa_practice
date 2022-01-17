from collections import Counter


class Solution:
    def isValid(self, board):
        counter = Counter(board)

        if abs(counter['X'] - counter['O']) > 1:
            return False

        x_win = o_win = False
        for i in range(3):
            if board[i] == board[i+3] == board[i+6]:
                if board[i] == 'X':
                    x_win = True
                else:
                    o_win = True
        for i in [0, 3, 6]:
            if board[i] == board[i+1] == board[i+2]:
                if board[i] == 'X':
                    x_win = True
                else:
                    o_win = True

        if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
            if board[4] == 'X':
                x_win = True
            else:
                o_win = True

        if o_win and counter['X'] > counter['O']:
            return False
        if x_win and o_win:
            return False
        return True

if __name__ == '__main__':
    board = ['X', 'X', 'X', 'O', 'X', 'O', 'O', 'O', 'X']
    print(Solution().isValid(board))
