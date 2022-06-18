# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_d = {
            1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
            4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'
        }
        stones = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        roman = ''
        while num > 0:
            i = len(stones) - 1
            while i >= 0 and num < stones[i]:
                i -= 1
            roman += roman_d[stones[i]]
            num -= stones[i]

        return roman


if __name__ == '__main__':
    num = 1994
    print(Solution().intToRoman(num))
