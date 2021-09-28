# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s): return []

        p_alpha_array = [0]*26
        p_size = len(p)
        for c in p:
            p_alpha_array[ord(c)-ord('a')] += 1
        for c in s[:p_size]:
            p_alpha_array[ord(c)-ord('a')] -= 1

        res = []
        for i in range(len(s)-len(p)+1):
            if i-1 >= 0:
                p_alpha_array[ord(s[i-1]) - ord('a')] += 1
                p_alpha_array[ord(s[i+p_size-1]) - ord('a')] -= 1
            if p_alpha_array.count(0) == len(p_alpha_array):
                res.append(i)

        return res


if __name__ == '__main__':
    s = 'abab'
    p = 'ab'
    print(Solution().findAnagrams(s, p))