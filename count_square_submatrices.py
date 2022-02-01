# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
from typing import List
from collections import Counter
from itertools import chain


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count_squares = 0
        m = len(matrix)
        n = len(matrix[0])
        squares = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    count_squares += 1
                    squares.append([i, i, j, j])

        dim = 2
        while len(squares):
            new_squares = []
            for i0, i1, j0, j1 in squares:
                i1 += 1
                j1 += 1
                if i1 >= m or j1 >= n:
                    continue

                l1 = matrix[i1][j0:j1+1]
                l2 = [matrix[_i][j1] for _i in range(i0, i1+1)]
                if sum(l1) == sum(l2) == dim:
                    new_squares.append((i0, i1, j0, j1))
                    count_squares += 1

            squares = new_squares
            dim += 1
        return count_squares

    def countSquares2(self, matrix: List[List[int]]) -> int:
        count_squares = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    count = 0
                    if i-1 >= 0:
                        matrix[i][j] += matrix[i-1][j]
                        count += 1
                    if j-1 >= 0:
                        matrix[i][j] += matrix[i][j-1]
                        count += 1
                    if count == 2:
                        matrix[i][j] -= matrix[i-1][j-1]

        counters = dict(Counter(chain(*matrix)))
        if counters.get(0):
            del counters[0]

        vals = list(counters.keys())
        vals.sort()
        sizes = [0] * 301
        size = 1
        for v in vals:
            if v == 0: continue
            if v >= (size+1)**2:
                # sizes[size] += counters[v]
                size += 1
            sizes[size] += counters[v]

        print(matrix)
        print(sizes)

        cur_sum = 0
        for i in range(len(sizes)-1, 0, -1):
            new_sum = cur_sum + sizes[i]
            sizes[i] += cur_sum
            cur_sum = new_sum
        print(sizes)
        # for i in range(1, len(sizes)):
        #     if sizes[i] == 0: continue

        #     count += sizes[i]
        #     j = i-1
        #     while j > 0:
        #         count += sizes[i] * (i-j+1)**2
        #         j -= 1

        return sum(sizes)


if __name__ == '__main__':
    matrix = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
    ]
    # matrix = [
    #     [0,1,1,1],
    #     [1,1,1,1],
    #     [0,1,1,1]
    # ]
    matrix = [
        [1]*5,
        [1]*5,
        [1]*5,
        [1]*5,
        [1]*5,
    ]
    print(Solution().countSquares(matrix))
    print(Solution().countSquares2(matrix))
