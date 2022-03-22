# https://leetcode.com/problems/next-greater-element-iii/


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = []
        m = n
        while m > 0:
            digits.append(m % 10)
            m //= 10

        max_digit = -1
        i = 0
        while i < len(digits):
            if digits[i] >= max_digit:
                max_digit = digits[i]
            else:
                break
            i += 1

        if i >= len(digits):
            return -1

        min_idx = -1
        for j in range(i):
            if digits[j] > digits[i]:
                if min_idx == -1:
                    min_idx = j
                elif digits[j] < digits[min_idx]:
                    min_idx = j

        digits[i], digits[min_idx] = digits[min_idx], digits[i]
        l = sorted(digits[:i])
        l.reverse()
        digits = l + digits[i:]

        new_n = 0
        while len(digits):
            new_n = new_n*10 + digits.pop()

        return new_n if new_n < 2**31 else -1


if __name__ == '__main__':
    n = 5932
    n = 321
    # n = 132
    # n = 52983
    # n = 230421
    # n = 7
    # n = 12222333

    print(Solution().nextGreaterElement(n))
