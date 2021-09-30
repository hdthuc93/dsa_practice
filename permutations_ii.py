# https://leetcode.com/problems/permutations-ii/


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def run_backtrack(nums, curr_str, no_dup):
            if len(nums) == 0:
                no_dup.add(curr_str)
                return

            for j in range(len(nums)):
                run_backtrack(nums[:j]+nums[j+1:], '{} {}'.format(curr_str, nums[j]), no_dup)

        no_dup = set()
        for i in range(len(nums)):
            run_backtrack(nums[:i]+nums[i+1:], '{}'.format(nums[i]), no_dup)

        res = []
        for serial in no_dup:
            serial = serial.split(' ')
            res.append(list(map(int, serial)))

        return res

    def permuteUnique2(self, nums: list[int]) -> list[list[int]]:
        def run_backtrack(nums_dict, n, curr, res):
            if len(curr) == n:
                res.append(curr[:])
                return

            for k in nums_dict:
                if nums_dict[k] > 0:
                    nums_dict[k] -= 1
                    curr.append(k)
                    run_backtrack(nums_dict, n, curr, res)
                    curr.pop()
                    nums_dict[k] += 1

        res = []
        nums_dict = {}
        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1
        run_backtrack(nums_dict, len(nums), [], res)
        return res


if __name__ == '__main__':
    nums = [1,1,3]
    print(Solution().permuteUnique2(nums))
