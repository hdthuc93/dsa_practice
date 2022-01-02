# https://leetcode.com/problems/reorganize-string/
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_d = {}
        for c in s:
            char_d.setdefault(c, 0)
            char_d[c] += 1

        q = []
        i = 0
        for char, count in char_d.items():
            heapq.heappush(q, (-count, i, char))

        max_num = ''
        while len(q):
            count, idx, char = heapq.heappop(q)
            if count == 0:
                continue

            if max_num and max_num[-1] == char:
                return ''

            max_num += char
            count += 1
            heapq.heappush(q, (count, idx+1, char))

        return max_num


if __name__ == '__main__':
    s = 'aaab'
    print(Solution().reorganizeString(s))
