# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List, NoReturn


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d_nums = {}
        longest = 0

        for n in nums:
            d_nums.setdefault(n, 1)

        for n in d_nums.keys():
            l = 1
            if d_nums[n] == 0:
                continue

            m = n - 1
            while d_nums.get(m, 0):
                d_nums[m] = 0
                m -= 1
                l += 1
            m = n + 1
            while d_nums.get(m, 0):
                d_nums[m] = 0
                m += 1
                l += 1

            longest = max(longest, l)

        return longest


if __name__ == '__main__':
    nums = []
    print(Solution().longestConsecutive(nums))
