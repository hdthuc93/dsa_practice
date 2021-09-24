# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        dp0 = [nums[0], 0, nums[0]+nums[2]]
        dp1 = [0, nums[1], 0]

        for i in range(3, len(nums)):
            dp0.append(max(dp0[i-3], dp0[i-2]) + nums[i])
            dp1.append(max(dp1[i-3], dp1[i-2]) + nums[i])

        dp0[-1] = max(dp0[-1] - nums[-1], dp0[-1] - nums[0])

        dp = dp0[-3:]
        dp.extend(dp1[-3:])
        max_money = max(dp)
        print(dp0)
        print(dp1)
        return max_money


if __name__ == '__main__':
    # nums = [2,1,2,6,1,8,10,10]
    nums = [1,2,3,1]
    print(Solution().rob(nums))
