# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]
        directs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def dfs(i, j, k):
            if k == len(word)-1:
                return True

            visited[i][j] = True
            for di, dj in directs:
                if 0 <= i+di < m and 0 <= j+dj < n:
                    if not visited[i+di][j+dj] and board[i+di][j+dj] == word[k+1]:
                        if dfs(i+di, j+dj, k+1):
                            return True
            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False

    def exist2(self, board: list[list[str]], word: str) -> bool:
        directs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        m = len(board)
        n = len(board[0])
        word_dict = {}
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                word_dict[c] = word_dict.get(c, set())
                if i-1 >= 0:
                    word_dict[c].add(board[i-1][j])
                if i+1 < m:
                    word_dict[c].add(board[i+1][j])
                if j-1 >= 0:
                    word_dict[c].add(board[i][j-1])
                if j+1 < n:
                    word_dict[c].add(board[i][j+1])

        for i in range(len(word)-1):
            if not (word_dict.get(word[i]) and word[i+1] in word_dict[word[i]]):
                return False

        return True


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    print(Solution().exist(board, word))
    print(Solution().exist2(board, word))
