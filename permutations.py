# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        def run_recurrsion(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    arr.append(nums[i])
                    run_recurrsion(arr)
                    arr.pop()
                    visited[i] = False

        run_recurrsion([])
        return res


if __name__ == '__main__':
    nums = [1]
    print(Solution().permute(nums))
