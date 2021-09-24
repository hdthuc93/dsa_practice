# https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: list[int]) -> int:
        furthest = 0
        n = len(nums)
        jumps = [1e6]*n
        jumps[0] = 0
        for i in range(n):
            if furthest >= n-1:
                break
            if i+nums[i] < furthest:
                continue
            prev_furthest = furthest
            furthest = i + nums[i]
            for j in range(prev_furthest+1, min(furthest+1, n)):
                jumps[j] = min(jumps[j], jumps[i]+1)
        return jumps[-1]


if __name__ == '__main__':
    # nums = [2,1,3,2,1,5,0,8]
    # nums = [3,4,3,2,5,4,3]
    # nums = [2,3,1,1,4]
    # nums = [4,1]
    # nums = [2,1,1,1,1]
    nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    print(Solution().jump(nums))
