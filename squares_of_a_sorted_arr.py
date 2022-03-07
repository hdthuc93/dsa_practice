# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            if nums[i] >= 0: break
            i += 1

        j = i - 1
        while j >= 0 and i < len(nums):
            if nums[j]**2 < nums[i]**2:
                res.append(nums[j]**2)
                j -= 1
            else:
                res.append(nums[i]**2)
                i += 1

        while i < len(nums):
            res.append(nums[i]**2)
            i += 1
        while j >= 0:
            res.append(nums[j]**2)
            j -= 1

        return res


if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    nums = [-7,-3,2,3,11]
    nums = [-5, -3, -1, 0, 1, 4, 5]
    nums = [-2]
    nums = [5]
    print(Solution().sortedSquares(nums))
