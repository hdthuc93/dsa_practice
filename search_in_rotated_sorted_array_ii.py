# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l = 0
        r = len(nums) - 1
        while l + 1 < len(nums) and nums[l+1] == nums[0]:
            l += 1
        while r > 0 and nums[r] == nums[0]:
            r -= 1
        min_idx = l

        if len(nums[min_idx:]) < 3:
            return target in nums[min_idx:]

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1

        zero_idx = l
        if r < min_idx:
            zero_idx = min_idx + 1
            if zero_idx + 1 < len(nums) and nums[zero_idx] > nums[zero_idx + 1]:
                zero_idx += 1
        if zero_idx >= len(nums):
            zero_idx = min_idx

        def binary_search(lst, target):
            l = 0
            r = len(lst) - 1
            while l <= r:
                m = (l + r) // 2
                if lst[m] == target:
                    return m
                elif lst[m] > target:
                    r = m - 1
                else:
                    l = m + 1

            return -1

        idx = -1
        if zero_idx == min_idx or target < nums[0]:
            idx = binary_search(nums[zero_idx:], target)
        else:
            idx = binary_search(nums[:zero_idx], target)

        return idx != -1


if __name__ == '__main__':
    nums = [2,5,0,1,2]
    nums = [0,2,5,6,7,8,9,-1,0,0]
    # nums = [1,1,1,1,2,1]
    # nums = [1,1,1,1,0,1]
    # nums = [5,0,1,2,3]
    # nums = [1]
    # nums = [0,1,2,3,0,0,0]
    nums = [3,1,1]
    nums = [1,3,3]
    nums = [0,0,1,1,2,3]

    target = 3
    print(Solution().search(nums, target))
