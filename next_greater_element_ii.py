# https://leetcode.com/problems/next-greater-element-ii/
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            while len(stack) and stack[-1] <= nums[i]:
                stack.pop()

            res[i] = (stack[-1] if len(stack) else -1)
            stack.append(nums[i])

        res = res[:int(len(nums)/2)]
        return res


if __name__ == '__main__':
    nums = [1,2,1]
    nums = [1,2,3,4,3]
    nums = [5,1,1,1,1]
    print(Solution().nextGreaterElements(nums))
