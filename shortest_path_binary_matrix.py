# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from queue import Queue


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        q = Queue()
        q.put((0, 0))
        directs = [[-1,-1], [0,-1], [-1,0], [-1,1], [1,-1], [0,1], [1,0], [1,1]]
        visited = [[0]*len(grid) for _ in range(len(grid))]
        visited[0][0] = 1
        while not q.empty():
            r, c = q.get()

            for i, j in directs:
                if 0 <= r+i < len(grid) and 0 <= c+j < len(grid):
                    if visited[r+i][c+j] == 0 and grid[r+i][c+j] == 0:
                        visited[r+i][c+j] = visited[r][c] + 1
                        q.put((r+i, c+j))
                        if r+i == c+j == len(grid)-1:
                            return visited[r+i][c+j]

        return -1


if __name__ == '__main__':
    grid = [[1,0,0],[1,1,0],[1,1,0]]
    print(Solution().shortestPathBinaryMatrix(grid))
