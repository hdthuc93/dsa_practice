# https://leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for n in nums:
            d.setdefault(n, 0)
            d[n] += 1

        res = []
        for i in range(len(nums)):
            second = target - nums[i]
            d[nums[i]] -= 1
            if d.get(second, 0) > 0:
                res.append(i)
                for j in range(i+1, len(nums)):
                    if nums[j] == second:
                        res.append(j)
                        break
                break

        return res


if __name__ == '__main__':
    nums = [3,2,4,2,2,4]
    target = 4
    print(Solution().twoSum(nums, target))
