# https://leetcode.com/problems/delete-and-earn/
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        nums_counter = Counter(nums)
        num_keys = list(nums_counter.keys())
        min_num = min(num_keys)
        max_num = max(num_keys)

        points = 0
        point_arr = []
        prev_num = -1
        for n in range(min_num, max_num+1):
            if not nums_counter.get(n): continue

            if n - prev_num == 1:
                val_1 = val_2 = n * nums_counter[n]
                val_1 = val_1 + point_arr[-2] if len(point_arr) >= 2 else val_1
                val_2 = val_2 + point_arr[-3] if len(point_arr) >= 3 else val_2
                point_arr.append(max(val_1, val_2))
            else:
                if len(point_arr):
                    points += max(point_arr)
                point_arr = [n * nums_counter[n]]
            prev_num = n

        points += max(point_arr)
        return points


if __name__ == '__main__':
    nums = [3,4,2]
    # nums = [2,2,3,3,3,4]
    # nums = [1,2,2,2,2,3,3]
    # nums = [8,7,3,8,1,4,10,10,10,2]
    # nums = [1,8,5,9,6,9,4,1,7,3,3,6,3,3,8,2,6,3,2,2,1,2,9,8,7,1,1,10,6,7,3,9,6,10,5,4,10,1,6,7,4,7,4,1,9,5,1,5,7,5]
    # nums = [79,1,95,8,57,52,87,32,45,40,77,85,53,9,15,55,20,29,72,71,64,48,25,44,55,9,82,53,89,64,60,20,80,57,62,88,54,100,89,45,81,67,84,75,37,10,68,35,40,85,52,50,67,68,11,90,28,74,82,96,37,75,36,32,73,29,99,71,88,98,90,47,91,12,13,64,13,82,52,31,22,14,29,51,1,60,55,93,95,31,33,60,78,80,33,73,84,82,54,23]
    # nums = [9,8,7,6,6]
    print(Solution().deleteAndEarn(nums))
