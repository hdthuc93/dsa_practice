# https://leetcode.com/problems/3sum/


from collections import Counter


class Solution:
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        c = Counter(nums)
        non_dup = sorted(list(c.keys()))
        res = []

        for i, val in enumerate(non_dup):
            if val > 0: break
            for j in range(i+1, len(non_dup)):
                target = -(val+non_dup[j])
                if target < non_dup[j]: break
                if target == val or target == non_dup[j]:
                    continue
                if target in c:
                    res.append([val, non_dup[j], target])

        for k, dup in c.items():
            if dup < 2: continue
            target = -2*k
            if target in c:
                res.append([k, k, target])

        return res

    def threeSum3(self, nums: list[int]) -> list[list[int]]:
        def binary_search(nums, l, r, target):
            if l > r:
                return -1
            if l == r:
                return l if nums[l] == target else -1

            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return binary_search(nums, l, m-1, target)
            return binary_search(nums, m+1, r, target)

        nums.sort()
        res = []
        prev_val = 1e5+1
        for i, val in enumerate(nums):
            if val > 0: break
            if prev_val == val: continue
            prev_val = val
            j = i+1
            while j < len(nums):
                jval = nums[j]
                target = -(val+jval)
                if target < nums[j]: break
                r = binary_search(nums, j+1, len(nums)-1, target)
                if r != -1:
                    res.append([val, jval, nums[r]])
                while j < len(nums) and jval == nums[j]: j += 1

        return res

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        prev_val = 1e5+1
        for i, val in enumerate(nums):
            if val > 0: break
            if prev_val == val: continue
            prev_val = val
            l = i+1
            r = len(nums)-1

            while l < r:
                lval = nums[l]
                rval = nums[r]
                three_sum = val + lval + rval
                if three_sum == 0:
                    res.append([val, lval, rval])

                if three_sum > 0:
                    while r >= 0 and rval == nums[r]:
                        r -= 1
                else:
                    while l < len(nums) and lval == nums[l]:
                        l += 1

        return res


if __name__ == '__main__':
    nums = [-1,-1,-1,0,0,1,1,1,2,2,2,-2,-2,-2]
    # nums = [-1,0,1,2,-1,-4]
    # nums = [0,0,0]

    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(Solution().threeSum3(nums))
