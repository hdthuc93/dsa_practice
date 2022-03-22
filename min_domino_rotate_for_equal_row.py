# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        rotate_on_tops = {}
        rotate_on_bottoms = {}
        rotate_on_tops.setdefault(tops[0], 0)
        rotate_on_bottoms.setdefault(bottoms[0], 0)

        if bottoms[0] != tops[0]:
            rotate_on_tops.setdefault(bottoms[0], 1)
            rotate_on_bottoms.setdefault(tops[0], 1)

        for i in range(1, len(tops)):
            if tops[i] != bottoms[i] and bottoms[i] in rotate_on_tops:
                rotate_on_tops[bottoms[i]] += 1
            for val in list(rotate_on_tops.keys()):
                if val != tops[i] and val != bottoms[i]:
                    rotate_on_tops.pop(val)

            if tops[i] != bottoms[i] and tops[i] in rotate_on_bottoms:
                rotate_on_bottoms[tops[i]] += 1
            for val in list(rotate_on_bottoms.keys()):
                if val != tops[i] and val != bottoms[i]:
                    rotate_on_bottoms.pop(val)

            if not rotate_on_tops:
                return -1

        min_rotate = 2 * 10**4 + 1
        for val in rotate_on_tops.keys():
            min_rotate = min([min_rotate, rotate_on_tops[val], rotate_on_bottoms[val]])

        return min_rotate if min_rotate < 2 * 10**4 + 1 else -1


if __name__ == '__main__':
    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]
    # tops = [2,1,1,3,2,1,2,2,1]
    # bottoms = [3,2,3,1,3,2,3,3,2]
    # tops = [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,2,1,2,2,1,1,2,2,2,2,2,1,1,2,2,2,2,1,2,1,1,2,1,1,1,1,2,1,2,2,2,1,2,1,2,2,1,2,1,2]
    # bottoms = [2,1,1,1,2,1,2,1,2,2,1,1,1,2,1,2,2,1,2,2,2,1,2,2,1,1,1,2,1,2,2,1,2,1,1,2,1,1,1,2,1,2,2,2,2,1,2,1,1,2,1,2,2,1,2,1,1,2,2,1,2,1,1,2]
    print(Solution().minDominoRotations(tops, bottoms))
