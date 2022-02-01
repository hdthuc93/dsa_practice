# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        nof_moves = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                last_c = stack[-1] if len(stack) else ''
                if last_c == '(':
                    stack.pop()
                else:
                    nof_moves += 1

        return nof_moves + len(stack)


if __name__ == '__main__':
    s = '())((('
    print(Solution().minAddToMakeValid(s))
