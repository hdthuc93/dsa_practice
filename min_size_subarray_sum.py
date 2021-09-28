# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = r = 0
        min_range = len(nums)+1
        current_sum = 0
        while r < len(nums):
            if current_sum >= target:
                min_range = min(min_range, (r-l))
                current_sum -= nums[l]
                l += 1
                if l > r:
                    r = l
            else:
                current_sum += nums[r]
                r += 1

        while l < len(nums):
            if current_sum >= target:
                min_range = min(min_range, (len(nums)-l))
                current_sum -= nums[l]
            else:
                break
            l += 1

        min_range = 0 if min_range > len(nums) else min_range
        return min_range


if __name__ == '__main__':
    target = 15
    nums = [5,1,3,5,10,7,4,9,2,8]

    print(Solution().minSubArrayLen(target, nums))
