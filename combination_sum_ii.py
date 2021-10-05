# https://leetcode.com/problems/combination-sum-ii/


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(candidates_dict, candidates, i, cur_sum, target, l, res):
            if cur_sum >= target:
                if cur_sum == target:
                    res.append(l[:])
                return

            for j in range(i, len(candidates)):
                n = candidates[j]
                if candidates_dict[n] > 0:
                    l.append(n)
                    candidates_dict[n] -= 1
                    dfs(candidates_dict, candidates, j, cur_sum+n, target, l, res)
                    l.pop()
                    candidates_dict[n] += 1

        res = []
        candidates_dict = {}
        for n in candidates:
            candidates_dict[n] = candidates_dict.get(n, 0) + 1
        candidates = list(candidates_dict.keys())
        dfs(candidates_dict, candidates, 0, 0, target, [], res)
        return res

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(candidates, i, cur_sum, target, l, res):
            if cur_sum >= target:
                if cur_sum == target:
                    res.append(l[:])
                return

            for j in range(i+1, len(candidates)):
                l.append(candidates[j])
                dfs(candidates, j, cur_sum+candidates[j], target, l, res)
                l.pop()

        res = []
        candidates.sort()
        dfs(candidates, -1, 0, target, [], res)
        return res


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
