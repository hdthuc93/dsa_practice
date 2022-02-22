# https://practice.geeksforgeeks.org/problems/anagram-palindrome4720/1/#


class Solution:
    def isPossible(self, S):
        # code here
        d_chars = {}
        for c in S:
            d_chars.setdefault(c, 0)
            d_chars[c] += 1

        odd = 0
        for _, v in d_chars.items():
            if v % 2 != 0:
                odd += 1

        if odd > 1:
            return False
        return True


if __name__ == '__main__':
    s = 'geeksogeeks'
    s = 'geeksforgeeks'
    print(Solution().isPossible(s))
