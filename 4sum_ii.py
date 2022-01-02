# https://leetcode.com/problems/4sum-ii/
from typing import List
from collections import Counter


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        group0 = {}
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        counter3 = Counter(nums3)
        counter4 = Counter(nums4)
        res = 0

        for n1 in counter1.keys():
            for n2 in counter2.keys():
                s = n1 + n2
                group0.setdefault(s, 0)
                group0[s] += (counter1[n1] * counter2[n2])

        for n3 in counter3.keys():
            for n4 in counter4.keys():
                res += group0.get(-(n3 + n4), 0) * (counter3[n3] * counter4[n4])

        return res


if __name__ == '__main__':
    nums1 = [1,2,1]
    nums2 = [-2,-1,-2]
    nums3 = [-1,2,-1]
    nums4 = [0,2,0]
    print(Solution().fourSumCount(nums1, nums2, nums3, nums4))
