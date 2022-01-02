# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }

        nums = []
        n = len(s)
        i = 0
        while i < n:
            if i + 1 < n and symbols.get(s[i] + s[i+1]):
                nums.append(symbols.get(s[i] + s[i+1]))
                i += 1
            else:
                nums.append(symbols[s[i]])
            i += 1

        return sum(nums)


if __name__ == '__main__':
    s = 'LVIII'
    s = 'III'
    s = 'MCMX'
    s = 'MCMXCIV'
    print(Solution().romanToInt(s))
