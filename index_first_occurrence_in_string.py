# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack) and len(haystack) - i >= len(needle):
            j = 0
            ii = i
            while j < len(needle) and haystack[ii] == needle[j]:
                j += 1
                ii += 1
            if j == len(needle):
                return i

            i += 1

        return -1
