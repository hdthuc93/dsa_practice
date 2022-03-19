# https://leetcode.com/problems/convert-to-base-2/


class Solution:
    def baseNeg2(self, n: int) -> str:
        res = ''
        n = -n
        while n != 0:
            res += str(abs(n % -2))
            n = (n // -2)

        return res[::-1]


if __name__ == '__main__':
    n = 10**9
    print(Solution().baseNeg2(n))
