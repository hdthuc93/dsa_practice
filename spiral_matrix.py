# https://leetcode.com/problems/spiral-matrix/


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        v_limit = [0, len(matrix)-1]
        h_limit = [0, len(matrix[0])-1]
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        j = -1
        idx = 0
        output = []

        while v_limit[0] <= v_limit[1] and h_limit[0] <= h_limit[1]:
            di, dj = directs[idx]
            i += di
            j += dj
            output.append(matrix[i][j])

            if di != 0:
                if i+di < v_limit[0]:
                    idx = (idx+1) % 4
                    h_limit[0] += 1
                elif i+di > v_limit[1]:
                    idx = (idx+1) % 4
                    h_limit[1] -= 1
            else:
                if j+dj < h_limit[0]:
                    idx = (idx+1) % 4
                    v_limit[1] -= 1
                elif j+dj > h_limit[1]:
                    idx = (idx+1) % 4
                    v_limit[0] += 1

        return output


if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6]]
    print(Solution().spiralOrder(matrix))
