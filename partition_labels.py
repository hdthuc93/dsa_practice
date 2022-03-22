# https://leetcode.com/problems/partition-labels/
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d_chars = {}
        for i in range(len(s)):
            if d_chars.get(s[i]):
                d_chars[s[i]][1] = i
            else:
                d_chars[s[i]] = [i, i]

        i = 1
        res = []
        l = 0
        r = d_chars[s[0]][1]
        while i < len(s):
            if d_chars[s[i]][0] > r:
                res.append(r - l + 1)
                l, r = d_chars[s[i]][0], d_chars[s[i]][1]
            else:
                if d_chars[s[i]][1] > r:
                    r = d_chars[s[i]][1]
            i += 1

        res.append(r - l + 1)
        return res


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    s = 'eccbbbbdec'
    print(Solution().partitionLabels(s))
