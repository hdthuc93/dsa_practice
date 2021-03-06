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
        m = len(board)
        n = len(board[0])
        word_dict = {}

        for i in range(m):
            for j in range(n):
                word_dict.setdefault(board[i][j], set())
                word_dict[board[i][j]].add((i, j))

        if word[0] not in word_dict:
            return False
        last_c = word[0]
        for c in word[1:]:
            if c not in word_dict:
                return False

            found = False
            for i, j in word_dict.get(c, set()):
                if (i - 1, j) in word_dict[last_c]:
                    word_dict[last_c].remove((i - 1, j))
                    found = True
                    break
                if (i + 1, j) in word_dict[last_c]:
                    word_dict[last_c].remove((i + 1, j))
                    found = True
                    break
                if (i, j - 1) in word_dict[last_c]:
                    word_dict[last_c].remove((i, j - 1))
                    found = True
                    break
                if (i, j + 1) in word_dict[last_c]:
                    word_dict[last_c].remove((i, j + 1))
                    found = True
                    break
            if not found:
                return False
            last_c = c
        return True


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
    print(Solution().exist2(board, word))
