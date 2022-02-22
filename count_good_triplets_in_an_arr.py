# https://leetcode.com/problems/count-good-triplets-in-an-array/
from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from bisect import insort, bisect_left, bisect_right
        res = 0
        n = len(nums1)
        d_indices_2 = {}
        for i in range(n):
            d_indices_2[nums2[i]] = i

        indices = []
        for i in range(n):
            indices.append(d_indices_2[nums1[i]])

        l_count, r_count = [], []
        l, r = [], []
        for i in range(n):
            l_count.append(bisect_left(l, indices[i]))
            insort(l, indices[i])

        for i in range(n-1, -1, -1):
            r_count.append(len(r) - bisect_right(r, indices[i]))
            insort(r, indices[i])

        for i in range(n):
            res += l_count[i] * r_count[n-i-1]

        return res


if __name__ == '__main__':
    nums1 = [2,0,1,3]
    nums2 = [0,1,2,3]
    nums1 = [4,0,1,3,2]
    nums2 = [4,1,0,2,3]
    print(Solution().goodTriplets(nums1, nums2))
