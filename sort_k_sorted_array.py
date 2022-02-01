# https://techiedelight.com/practice/?problem=SortKSortedArray
from typing import List
import heapq


class Solution:
    def sortKSortedArray(self, nums: List[int], k: int) -> None:
        hq = []
        for i in range(k):
            heapq.heappush(hq, nums[i])

        for i in range(k, len(nums)):
            heapq.heappush(hq, nums[i])
            nums[i-k] = heapq.heappop(hq)

        for i in range(len(nums)-k, len(nums)):
            nums[i] = heapq.heappop(hq)

if __name__ == '__main__':
    nums = [3, 2, 6, 5, 4]
    k = 2
    Solution().sortKSortedArray(nums, k)
    print(nums)
