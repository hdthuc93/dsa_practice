# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def get_2_max_val_in_dict(d):
            max_k0 = None
            for k, v in d.items():
                if not max_k0 or v >= d[max_k0]:
                    max_k0 = k

            max_k1 = None
            for k, v in d.items():
                if k != max_k0 and (not max_k1 or v >= d[max_k1]):
                    max_k1 = k
            return max_k0, max_k1

        if len(nums) == 1: return 0
        d_odd = {}
        d_even = {}
        max_odd = []
        max_even = []

        for i, num in enumerate(nums):
            if i % 2 == 0:
                d_even.setdefault(num, 0)
                d_even[num] += 1
            else:
                d_odd.setdefault(num, 0)
                d_odd[num] += 1

        for k, v in d_even.items():
            if not len(max_even):
                max_even.append(k)
            elif d_even[max_even[-1]] <= v:
                max_even.append(k)

        for k, v in d_odd.items():
            if not len(max_odd):
                max_odd.append(k)
            elif d_odd[max_odd[-1]] <= v:
                max_odd.append(k)

        nof_even = nof_odd = len(nums)//2
        if len(nums) % 2 != 0:
            nof_even += 1

        max_even_0, max_even_1 = get_2_max_val_in_dict(d_even)
        max_odd_0, max_odd_1 = get_2_max_val_in_dict(d_odd)
        if max_odd_0 != max_even_0:
            return (nof_even - d_even[max_even_0]) + (nof_odd - d_odd[max_odd_0])

        opt1 = 0
        r0 = max_even_0
        r1 = max_odd_1 if max_odd_1 else r0 - 1
        for i in range(len(nums)):
            if i % 2 == 0:
                if nums[i] != r0:
                    opt1 += 1
            else:
                if nums[i] != r1:
                    opt1 += 1

        opt2 = 0
        r1 = max_odd_0
        r0 = max_even_1 if max_even_1 else r1 - 1
        for i in range(len(nums)):
            if i % 2 == 0:
                if nums[i] != r0:
                    opt2 += 1
            else:
                if nums[i] != r1:
                    opt2 += 1

        return min(opt1, opt2)



if __name__ == '__main__':
    nums = [1,2,2,2,2]
    # nums = [3,1,3,2,4,3]
    # nums = [69,91,47,74,75,94,22,100,43,50,82,47,40,51,90,27,98,85,47,14,55,82,52,9,65,90,86,45,52,52,95,40,85,3,46,77,16,59,32,22,41,87,89,78,59,78,34,26,71,9,82,68,80,74,100,6,10,53,84,80,7,87,3,82,26,26,14,37,26,58,96,73,41,2,79,43,56,74,30,71,6,100,72,93,83,40,28,79,24]
    # nums = [1]
    # nums = [1,2]
    # nums = [1,1]
    # nums = [2,2,2,2]
    # nums = [3,3,3,4,3,3,3]
    # nums = [1,2,1,2,1,2]
    print(Solution().minimumOperations(nums))
