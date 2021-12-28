# https://leetcode.com/problems/non-decreasing-array/


from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        target_idx = -1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if target_idx == -1:
                    target_idx = i - 1
                else:
                    return False

        at_most = False
        for t in range(target_idx, target_idx + 2):
            if t != -1 and not at_most:
                if t == 0 or t == len(nums) - 1:
                    at_most = True
                else:
                    at_most = nums[t-1] <= nums[t+1]

        return at_most


if __name__ == '__main__':
    nums = [115,4,4,15]
    print(Solution().checkPossibility(nums))
