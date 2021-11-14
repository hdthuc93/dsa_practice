# https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])


if __name__ == '__main__':
    nums = [2,-2,3,0,-1]
    print(Solution().maximumProduct(nums))
