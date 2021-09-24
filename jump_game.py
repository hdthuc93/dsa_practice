# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        jump_to = []
        mem = {}
        for i in range(len(nums)):
            jump_to.append(i+nums[i])

        def find_prev_jump(jump_to, index, target_index, mem):
            last_can_jump = mem.get('{}_{}'.format(index, target_index), None)
            if last_can_jump is not None:
                return last_can_jump

            if target_index == 0:
                return True

            for i in range(index, -1, -1):
                if jump_to[i] >= target_index:
                    res = find_prev_jump(jump_to, i-1, i, mem)
                    mem['{}_{}'.format(i-1, i)] = res
                    if res:
                        return True

            return False

        for i in range(len(jump_to)-2, -1, -1):
            if jump_to[i] >= len(nums)-1:
                res = find_prev_jump(jump_to, i-1, i, mem)
                if res:
                    return res

        return False

    def canJump2(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        can_jump = nums[0]
        n = len(nums)
        for i in range(1, n):
            if can_jump >= n-1:
                return True
            if can_jump < i:
                return False
            can_jump = max(i+nums[i], can_jump)

        return True


if __name__ == '__main__':
    nums = [3,2,0,1,4]
    print(Solution().canJump2(nums))
