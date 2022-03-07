# https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        t = 0
        for i in range(k):
            prev = nums[i]
            j = i
            while t < n:
                next_j = (j+k) % n
                temp = nums[next_j]
                nums[next_j] = prev
                prev = temp
                j = next_j
                t += 1
                if j == i:
                    break


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 1
    # nums = [1,2,3,4,5,6]
    # k = 4

    # nums = [-1,-100,3,99]
    # k = 10
    Solution().rotate(nums, k)
    print(nums)
