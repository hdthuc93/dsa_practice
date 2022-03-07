# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
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

    def findAnagrams(self, s: str, p: str) -> List[int]:

        len_p = len(p)
        counter_p = Counter(p)
        counter_s = Counter(s[:len_p-1])

        res = []
        for i in range(len_p-1, len(s)):
            counter_s.setdefault(s[i], 0)
            counter_s[s[i]] += 1
            match = True
            for k, amount in counter_p.items():
                if amount != counter_s.get(k, 0):
                    match = False
                    break

            if match:
                res.append(i-len_p+1)

            counter_s[s[i-len_p+1]] = max(counter_s[s[i-len_p+1]] - 1, 0)

        return res


if __name__ == '__main__':
    s = 'abab'
    p = 'ab'
    print(Solution().findAnagrams(s, p))
