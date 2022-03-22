# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s_lst = ['z'] * n
        val = 26 * n
        i = 0
        while val > k:
            if val - k >= 26:
                val -= 25
                s_lst[i] = 'a'
            else:
                s_lst[i] = chr(ord('a') + (26 - (val - k) - 1))
                break
            i += 1
        return ''.join(s_lst)


if __name__ == '__main__':
    n = 3
    k = 27
    n = 5
    k = 73
    n = 10000
    k = 26*10000
    print(Solution().getSmallestString(n, k))
