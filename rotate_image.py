# https://leetcode.com/problems/rotate-image/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from queue import Queue
        n = len(matrix)
        m = n
        k = 0

        while k < m:
            q = Queue()
            for i in range(m-1, k, -1):
                q.put(matrix[i][k])

            for j in range(k, m):
                q.put(matrix[k][j])
                matrix[k][j] = q.get()

            for i in range(k+1, m):
                q.put(matrix[i][m-1])
                matrix[i][m-1] = q.get()

            for j in range(m-2, k-1, -1):
                q.put(matrix[m-1][j])
                matrix[m-1][j] = q.get()

            for i in range(m-2, k, -1):
                matrix[i][k] = q.get()
            k += 1
            m -= 1


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(matrix)
    for m in matrix:
        print(m)
