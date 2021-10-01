# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def run_backtracking(i, cur, lparentheses):
            if i == 2*n:
                if lparentheses == 0:
                    res.append(cur)
                return

            if lparentheses > 0:
                run_backtracking(i+1, cur+')', lparentheses-1)
            run_backtracking(i+1, cur+'(', lparentheses+1)

        run_backtracking(0, '', 0)
        return res


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
