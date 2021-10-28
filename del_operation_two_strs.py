# https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)
        n = len(word1)
        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                in_front = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0
                before = dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                if word1[j] == word2[i]:
                    dp[i][j] = before + 1
                else:
                    dp[i][j] = max(in_front, left)

        return (m-dp[-1][-1]) + (n-dp[-1][-1])


if __name__ == '__main__':
    word1 = 'park'
    word2 = 'spake'
    print(Solution().minDistance(word1, word2))
