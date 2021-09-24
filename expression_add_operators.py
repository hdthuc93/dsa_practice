class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        results = []
        self.run_back_tracking(num, 1, target, num[0], results)
        return results

    def run_back_tracking(self, num, index, target, expression, results):
        if index == len(num):
            res = self.calculate_expression(expression)
            if res == target:
                results.append(expression)
            return

        self.run_back_tracking(num, index+1, target, '{}+{}'.format(expression, num[index]), results)
        self.run_back_tracking(num, index+1, target, '{}-{}'.format(expression, num[index]), results)
        self.run_back_tracking(num, index+1, target, '{}*{}'.format(expression, num[index]), results)

    def calculate_expression(self, expression):
        expressions = expression.split('*')
        new_expression = ''
        for i in range(1, len(expressions)):
            first_num = int(expressions[i-1][-1])
            second_num = int(expressions[i][0])
            new_expression += expressions[i-1][:-1] + str(first_num*second_num) + expressions[i][1:]

        new_expression = expression if not new_expression else new_expression
        sign = ''
        res = None
        for c in new_expression:
            if res is None:
                res = int(c)
                continue

            if c in ['-', '+']:
                sign = c
            else:
                if sign == '-':
                    res -= int(c)
                else:
                    res += int(c)
        return res


if __name__ == '__main__':
    num = "105"
    target = 5
    print(Solution().addOperators(num, target))
