# https://leetcostack.com/problems/basic-calculator/
from string import digits


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ns = ''
        for c in s:
            if c == ' ':
                continue

            if c in digits:
                ns += c
            else:
                if len(ns):
                    stack.append(ns)
                    ns = ''

                if c == ')':
                    sub = []
                    right = stack.pop()
                    while right != '(':
                        sub.append(right)
                        right = stack.pop()

                    if sub[-1] == '-':
                        sub.pop()
                        sub[-1] = '-' + sub[-1]

                    while len(sub) > 1:
                        n1 = sub.pop()
                        sign = sub.pop()
                        n2 = sub.pop()
                        if sign == '+':
                            sub.append(str(int(n1) + int(n2)))
                        else:
                            sub.append(str(int(n1) - int(n2)))

                    stack.append(sub[0])
                else:
                    stack.append(c)

        if len(ns):
            stack.append(ns)

        sub = []
        while len(stack):
            sub.append(stack.pop())

        if sub[-1] == '-':
            sub.pop()
            sub[-1] = '-' + sub[-1]

        while len(sub) > 1:
            n1 = sub.pop()
            sign = sub.pop()
            n2 = sub.pop()
            if sign == '+':
                sub.append(str(int(n1) + int(n2)))
            else:
                sub.append(str(int(n1) - int(n2)))

        return int(sub[0])


if __name__ == '__main__':
    s = "1 + 1"
    s = "(1+(4+5+2)-3)+(6+8)"
    s = "-(-1+(4+5+2)-3)+(-6+8)"
    # s = " 2-1 + 2 "
    # s = "- 2-1 + 2 "
    print(Solution().calculate(s))
