# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/


from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        r = 0
        max_val = nums[0]
        for i in range(len(nums)):
            if max_val <= nums[i]:
                max_val = nums[i]
            else:
                r = i

        l = len(nums) - 1
        min_val = nums[l]
        for i in range(len(nums)-1, -1, -1):
            if min_val >= nums[i]:
                min_val = nums[i]
            else:
                l = i

        print(l, r)

        return max(r - l + 1, 0)


if __name__ == '__main__':
    nums = [1,2,3,3,3]
    print(Solution().findUnsortedSubarray(nums))
