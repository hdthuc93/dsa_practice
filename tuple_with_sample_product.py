# https://leetcode.com/problems/tuple-with-same-product/description/

from collections import Counter
from functools import reduce
from operator import mul


class Solution1:
    def tupleSameProduct(self, nums: List[int]) -> int:
        c = Counter()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                c[nums[i]*nums[j]] += 1

        res = 0
        for _, v in c.items():
            if v > 1:
                comb = self.combine(v, 2)
                res += (8 * comb)

        return res

    def combine(self, n, r):
        if n == r:
            return 1

        val1 = reduce(mul, range(1, n+1))
        val2 = reduce(mul, range(1, r+1))
        val3 = reduce(mul, range(1, (n-r)+1))

        return int(val1 / (val2 * val3))
