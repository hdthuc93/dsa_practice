# https://leetcode.com/problems/maximum-earnings-from-taxi/description/

from typing import List
from bisect import bisect_right


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        ends = []
        dp = []
        # print("rides", rides)
        for start, end, tip in rides:
            earn = end - start + tip
            idx = bisect_right(ends, start) - 1
            if idx >= 0:
                earn += dp[idx]

            if dp:
                earn = max(dp[-1], earn)

            if not ends or ends[-1] != end:
                ends.append(end)
                dp.append(earn)
            else:
                dp[-1] = earn

            # print("ends", ends)
            # print("dp", dp)
            # print()
        return dp[-1] if dp else 0
