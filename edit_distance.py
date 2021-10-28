# https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)+1
        n = len(word2)+1
        dp = [[0]*n for _ in range(m)]
        for i in range(m): dp[i][0] = i
        for j in range(n): dp[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        for arr in dp:
            print(arr)

        return dp[-1][-1]


if __name__ == '__main__':
    word1 = 'distance'
    word2 = 'daliance'
    word1 = 'horse'
    word2 = 'ros'
    word1 = "intention"
    word2 = "execution"
    # word1 = 'prosperity'
    # word2 = 'properties'
    # word1 = "teacher"
    # word2 = "botcher"
    # word1 = "distance"
    # word2 = "beholder"
    # word1 = "sea"
    # word2 = "ate"
    # word1 = ""
    # word2 = "abc"
    # word1 = "dinitrophenylhydrazine"
    # word2 = "dimethylhydrazine"
    word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
    word2 = "pneumonoconiosis"
    # word1 = "pneumonoxxxxxxxxxxxxcxxxxxxxxxxxxxxxxconiosis"
    # word2 = "pneumonoconiosis"
    print(Solution().minDistance(word1, word2))
