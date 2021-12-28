# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List
from collections import deque


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_s = nums[0]
        total = 1 if nums[0] == k else 0
        d = {cur_s: 1}
        for i in range(1, len(nums)):
            cur_s += nums[i]
            if cur_s == k:
                total += 1

            before_sum = cur_s - k
            total += d.get(before_sum, 0)

            d.setdefault(cur_s, 0)
            d[cur_s] += 1

        return total


if __name__ == '__main__':
    nums = [-1, -1, 1, -1, -2, -1, 3]
    k = 0
    print(Solution().subarraySum(nums, k))
