# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        counting_grid =[[0]*n for _ in range(m)]
        counting_grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    counting_grid[i][j] += counting_grid[i-1][j]
                if j-1 >= 0:
                    counting_grid[i][j] += counting_grid[i][j-1]

        return counting_grid[m-1][n-1]


if __name__ == '__main__':
    m = 1
    n = 1
    print(Solution().uniquePaths(m, n))
