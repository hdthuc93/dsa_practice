# https://leetcode.com/problems/remove-invalid-parentheses/
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res_set = set()

        def check_valid(str):
            stack = []
            i = 0
            while i < len(str):
                if str[i] == '(':
                    stack.append(str[i])
                elif str[i] == ')':
                    if len(stack):
                        stack.pop()
                    else:
                        return False
                i += 1
            return len(stack) == 0

        def get_results(c_lst, s, i):
            if i >= len(s):
                if check_valid(c_lst):
                    res_set.add(''.join(c_lst))
                return

            cases = [s[i]]
            if s[i] in ['(', ')']:
                cases = ['', s[i]]

            for c in cases:
                c_lst.append(c)
                get_results(c_lst, s, i+1)
                c_lst.pop()

        get_results([], s, 0)
        res = []
        max_len = -1
        for str in res_set:
            max_len = max(max_len, len(str))
        for str in res_set:
            if len(str) == max_len:
                res.append(str)
        return res



if __name__ == '__main__':
    s = '()())()'
    # s = "(a)())()"
    # s = ")("
    # s = "()())(()"
    s = ")(((()(y((u()(z()()"
    s = "((s(())()(()))(((((("
    print(Solution().removeInvalidParentheses(s))
