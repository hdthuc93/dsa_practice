# https://leetcode.com/problems/count-number-of-bad-pairs

from typing import List
import bisect
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        minus_idx_num = []
        res_indices = defaultdict(list)

        for i, num in enumerate(nums):
            res = i - num
            minus_idx_num.append(res)
            res_indices[res].append(i)
        print(res_indices)
        good_guys = 0
        for i, res in enumerate(minus_idx_num):
            # import pdb; pdb.set_trace()
            indices = res_indices[res]
            idx = bisect.bisect_left(indices, i)
            if idx + 1 < len(indices):
                good_guys += len(indices) - (idx + 1)

        print(good_guys)
        total = sum(range(len(nums)))
        print(total)
        return total - good_guys

sol = Solution()
print(sol.countBadPairs([4,1,3,3]))
print(sol.countBadPairs([1,2,3,4,5]))
