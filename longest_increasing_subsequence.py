# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = {1: nums[0]}
        max_len = 1
        for i in range(1, len(nums)):
            j = max_len
            while j > 0:
                if dp[j] < nums[i]:
                    dp[j+1] = nums[i]
                    max_len = max(max_len, j+1)
                    break
                j -= 1
            else:
                if dp[1] > nums[i]:
                    dp[1] = nums[i]

        return max_len


if __name__ == '__main__':
    nums = [4,10,4,3,8,9]
    # nums = [0,1,0,3,2,3]
    # nums = [10,9,2,5,3,7,101,18]
    nums = [7,7,7,7,7,7,7]
    print(Solution().lengthOfLIS(nums))
