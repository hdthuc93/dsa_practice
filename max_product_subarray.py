# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_res = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        init = False

        for i in range(1, len(nums)):
            if init:
                max_prod = nums[i]
                min_prod = nums[i]
                max_res = max(max_res, max_prod)
                init = False
                continue

            if nums[i] == 0:
                init = True
                max_res = max(max_res, 0)
                continue

            prev_min = min_prod
            prev_max = max_prod
            max_prod = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            min_prod = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            # print(nums[i], '=====' ,min_prod, max_prod)
            max_res = max(max_res, max_prod)

        return max_res
