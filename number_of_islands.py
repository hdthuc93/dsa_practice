# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def run_dfs(grid, i, j):
            grid[i][j] = '0'
            if i > 0 and grid[i-1][j] == '1':
                run_dfs(grid, i-1, j)
            if j > 0 and grid[i][j-1] == '1':
                run_dfs(grid, i, j-1)
            if i+1 < len(grid) and grid[i+1][j] == '1':
                run_dfs(grid, i+1, j)
            if j+1 < len(grid[0]) and grid[i][j+1] == '1':
                run_dfs(grid, i, j+1)

        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        nof_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    run_dfs(grid, i, j)
                    nof_island += 1
        return nof_island


if __name__ == '__main__':
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
    print(Solution().numIslands(grid))
