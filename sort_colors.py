# https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        two_idx = len(nums) - 1
        i = 0
        while i < len(nums) and zero_idx < two_idx:
            if nums[i] == 0:
                if i > zero_idx:
                    nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                    i -= 1
                zero_idx += 1
            elif nums[i] == 2:
                if i < two_idx:
                    nums[i], nums[two_idx] = nums[two_idx], nums[i]
                    i -= 1
                two_idx -= 1
            i += 1


if __name__ == '__main__':
    nums = [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,1,1,2,2,2,2,2]
    Solution().sortColors(nums)
    print(nums)
