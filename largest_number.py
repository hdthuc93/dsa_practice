# https://leetcode.com/problems/largest-number/
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if int(nums[j] + nums[i]) > int(nums[i] + nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        res = ''.join(nums)
        while len(res) >= 2 and res[1] == res[0] == '0':
            res = res[1:]

        return res


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    nums = [10,2]
    nums = [0]*10
    print(Solution().largestNumber(nums))
