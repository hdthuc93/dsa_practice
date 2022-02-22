# https://leetcode.com/problems/increasing-triplet-subsequence/
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min0 = nums[0]
        min1 = None
        for n in nums[1:]:
            if n < min0:
                min0 = n
            elif n > min0:
                if min1 is None or n < min1:
                    min1 = n
                elif n > min1:
                    return True
        return False

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    nums = [5,4,3,2,1]
    nums = [2,1,5,0,4,6]
    nums = [20,100,10,12,5,13]
    nums = [0,0,0,0,-1,0,0,0,100000000]
    print(Solution().increasingTriplet(nums))
