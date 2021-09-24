# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        start_point = ()
        bricks = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_point = (i, j)
                elif grid[i][j] == -1:
                    bricks.append((i, j))

        remain = m*n - len(bricks)
        path = []
        count_res = self.run_back_tracking(start_point, remain, grid, path, 0)

        return count_res

    def run_back_tracking(self, point, remain, grid, path, count_res):
        remain -= 1
        if grid[point[0]][point[1]] == 2:
            if remain == 0:
                print(path, point)
                return count_res + 1
            return count_res

        if grid[point[0]][point[1]] == 0:
            grid[point[0]][point[1]] = 3  # 3 meaning this position is placed
        m = len(grid)
        n = len(grid[0])
        path.append(point)
        four_dims = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for dim in four_dims:
            next_point = (point[0] + dim[0], point[1] + dim[1])
            if next_point[0] < 0 or next_point[0] >= m:
                continue
            if next_point[1] < 0 or next_point[1] >= n:
                continue
            if grid[next_point[0]][next_point[1]] in (-1, 1, 3):
                continue

            count_res = self.run_back_tracking(next_point, remain, grid, path, count_res)

        if grid[point[0]][point[1]] == 3:
            grid[point[0]][point[1]] = 0
        remain += 1
        path.pop()
        return count_res


if __name__ == '__main__':
    grid = [[0,1],[2,0]]
    sol = Solution()
    print(sol.uniquePathsIII(grid=grid))
