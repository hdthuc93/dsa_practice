# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if c == ')':
                    if len(stack) and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif c == '}':
                    if len(stack) and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    if len(stack) and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        return True


if __name__ == '__main__':
    s = '([)]'
    print(Solution().isValid(s))
