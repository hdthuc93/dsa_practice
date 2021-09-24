# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: list[int]) -> int:
        def searching(nums, l, r):
            if r - l <= 1:
                return min(nums[l], nums[r])

            m = (l+r)//2
            if nums[m] > nums[l]:
                return searching(nums, m, r)
            elif nums[m] < nums[r]:
                return searching(nums, l, m)

        if nums[0] > nums[-1]:
            return searching(nums, 0, len(nums)-1)
        return nums[0]


if __name__ == '__main__':
    nums = [4,-1,2]
    print(Solution().findMin(nums))
