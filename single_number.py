# https://leetcode.com/problems/single-number/


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)

        return list(s)[0]


if __name__ == '__main__':
    nums = [2]
    print(Solution().singleNumber(nums))
