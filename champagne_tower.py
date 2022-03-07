# https://leetcode.com/problems/champagne-tower/


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (r+1) for r in range(query_row+1)]
        dp[0] = [poured]

        for i in range(query_row+1):
            for j in range(i+1):
                if dp[i][j] > 1:
                    if i + 1 <= query_row:
                        dp[i+1][j] += (dp[i][j] - 1) / 2
                        dp[i+1][j+1] += (dp[i][j] - 1) / 2
                    dp[i][j] = 1

        return dp[query_row][query_glass]


if __name__ == '__main__':
    poured = 2
    query_row = 1
    query_glass = 1

    poured = 100
    query_row = 10
    query_glass = 8
    print(Solution().champagneTower(poured, query_row, query_glass))
