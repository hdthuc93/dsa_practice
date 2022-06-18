# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/


class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split('+')
        i, j = 0, len(num2)
        min_res = [int(num1) + int(num2)]
        idx = [(i, j)]
        checked = set()
        checked.add((i, j))

        def recursion(exp1, exp2, i1, i2):
            n1 = exp1[:i1] if i1 > 0 else 1
            n2 = exp2[i2:] if i2 < len(exp2) else 1
            r = int(n1) * (int(exp1[i1:]) + int(exp2[:i2])) * int(n2)

            if r < min_res[0]:
                min_res[0] = r
                idx[0] = (i1, i2)

            if i1 + 1 < len(exp1) and (i1+1, i2) not in checked:
                checked.add((i1+1, i2))
                recursion(exp1, exp2, i1 + 1, i2)

            if i2 - 1 > 0 and (i1, i2-1) not in checked:
                checked.add((i1, i2-1))
                recursion(exp1, exp2, i1, i2-1)

        recursion(num1, num2, 0, len(num2))
        i, j = idx[0]
        return '{}({}+{}){}'.format(num1[:i], num1[i:], num2[:j], num2[j:])


if __name__ == '__main__':
    expression = '12+34'
    expression = '247+38'
    expression = '999+999'
    expression = "99999999+9"
    print(Solution().minimizeResult(expression))
