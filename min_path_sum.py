# https://leetcode.com/problems/minimum-path-sum/
from typing import List
from queue import Queue


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        q = Queue()
        q.put((0, 0))
        visited[0][0] = grid[0][0]

        while not q.empty():
            i, j = q.get()

            if i+1 < m:
                if visited[i+1][j] == 0:
                    q.put((i+1, j))
                    visited[i+1][j] = visited[i][j] + grid[i+1][j]
                visited[i+1][j] = min(visited[i+1][j], visited[i][j] + grid[i+1][j])

            if j+1 < n:
                if visited[i][j+1] == 0:
                    q.put((i, j+1))
                    visited[i][j+1] = visited[i][j] + grid[i][j+1]
                visited[i][j+1] = min(visited[i][j+1], visited[i][j] + grid[i][j+1])

        return visited[-1][-1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]


if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    grid = [[1,2,3],[4,5,6]]
    print(Solution().minPathSum(grid))
