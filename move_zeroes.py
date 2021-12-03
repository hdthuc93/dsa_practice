# https://leetcode.com/problems/move-zeroes/


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[next_zero] = nums[next_zero], nums[i]
                next_zero += 1
