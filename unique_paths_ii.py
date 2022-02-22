# https://leetcode.com/problems/unique-paths-ii/
from queue import Queue
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        visitted = [[0]*n for _ in range(m)]
        q = Queue()
        q.put((0, 0))
        visitted[0][0] = 1

        while not q.empty():
            i, j = q.get()
            if i+1 < m and obstacleGrid[i+1][j] != 1:
                if visitted[i+1][j] == 0:
                    q.put((i+1, j))
                visitted[i+1][j] += visitted[i][j]

            if j+1 < n and obstacleGrid[i][j+1] != 1:
                if visitted[i][j+1] == 0:
                    q.put((i, j+1))
                visitted[i][j+1] += visitted[i][j]

        return visitted[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]
    # obstacleGrid = [[0,1],[0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
