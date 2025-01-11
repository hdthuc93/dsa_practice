#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        r_sum_count_pair = [0, 0]
        l_sum_count_pair = [0, 0]
        n = len(boxes)
        for i in range(n):
            if boxes[i] == '1':
                r_sum_count_pair[0] += i + 1
                r_sum_count_pair[1] += 1

        # print(r_sum_count_pair)
        # print(l_sum_count_pair)
        res = [0] * n
        for i in range(n):
            res[i] = r_sum_count_pair[0] - r_sum_count_pair[1]
            res[i] += l_sum_count_pair[0] + l_sum_count_pair[1]
            if r_sum_count_pair[1]:
                r_sum_count_pair[0] -= r_sum_count_pair[1]
            else:
                r_sum_count_pair[0] = 0
            l_sum_count_pair[0] += l_sum_count_pair[1]

            if boxes[i] == '1':
                l_sum_count_pair[1] += 1
                r_sum_count_pair[1] = max(r_sum_count_pair[1] - 1, 0)

        return res
