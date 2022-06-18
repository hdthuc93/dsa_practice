# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            cnt = 0
            for n in nums:
                if n <= m:
                    cnt += 1

            if cnt <= m:
                l = m + 1
            else:
                r = m - 1

        return l


if __name__ == '__main__':
    nums = [1,3,4,2,2]
    nums = [3,1,2,4,4]
    print(Solution().findDuplicate(nums))
