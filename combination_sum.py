# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(candidates, i, cur_sum, target, l, res):
            if cur_sum >= target:
                if cur_sum == target:
                    res.append(l[:])
                return

            for j in range(i, len(candidates)):
                l.append(candidates[j])
                dfs(candidates, j, cur_sum+candidates[j], target, l, res)
                l.pop()

        res = []
        dfs(candidates, 0, 0, target, [], res)
        return res


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))
