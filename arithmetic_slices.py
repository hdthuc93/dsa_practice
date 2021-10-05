# https://leetcode.com/problems/arithmetic-slices/


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        diff = nums[1] - nums[0]
        prev_n = nums[1]
        cur_count = count = res = 0
        for i in range(2, len(nums)):
            n = nums[i]
            if n - prev_n != diff:
                res += count
                diff = n - prev_n
                cur_count = count = 0
            else:
                cur_count += 1
                count += cur_count
            prev_n = n

        res += count

        return res


if __name__ == '__main__':
    nums = [1,2,3,4,5,2,3,1,7,7,7,7]
    # nums = [1,2,3,4]
    print(Solution().numberOfArithmeticSlices(nums))
