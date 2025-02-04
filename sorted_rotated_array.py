# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/


class Solution:
    def check(self, nums: List[int]) -> bool:
        state = 'l1'
        for i in range(1, len(nums)):
            if state == 'l1':
                if nums[i] < nums[i-1]:
                    state = 'l2'
            elif state == 'l2':
                if nums[i] < nums[i-1]:
                    return False

        return not (state == 'l2' and nums[-1] > nums[0])
