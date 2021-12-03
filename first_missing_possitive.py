# https://leetcode.com/problems/first-missing-positive/


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing_table = [0]*(500001)
        for num in nums:
            if num <= 0 or num >= 500001:
                continue

            missing_table[num] += 1

        for i in range(1, 500001):
            if missing_table[i] == 0:
                return i

        return 500001

    def firstMissingPositive1(self, nums: List[int]) -> int:
        nums = set(nums)
        n = 1
        while n < 500001:
            if n not in nums:
                return n
            n += 1
        return 500001


if __name__ == '__main__':
    nums = [1,2,0]
    print(Solution().firstMissingPositive1(nums))
