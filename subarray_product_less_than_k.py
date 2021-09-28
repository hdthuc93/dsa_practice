# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        l = r = 0
        product = 1
        count = 0

        while l < len(nums) and r < len(nums):
            if product*nums[r] < k:
                product *= nums[r]
                r += 1
                count = count + (r-l)
            else:
                product /= nums[l]
                product = 1 if product < 1 else product
                l += 1
                if l > r:
                    r = l

        return count


if __name__ == '__main__':
    nums = [10,5,2,6,99,7,2,4,6]
    # nums = [1,2,3]
    nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    k = 19
    print(Solution().numSubarrayProductLessThanK(nums, k))