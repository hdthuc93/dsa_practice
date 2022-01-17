# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        last_len = 1
        nof_one = 0
        res = [0, 1]
        j = 0
        for i in range(2, n+1):
            if 2**last_len == i:
                nof_one = 1
                last_len += 1
                j = 0
            else:
                nof_one = 1 + res[j]
            res.append(nof_one)
            j += 1

        return res


if __name__ == '__main__':
    n = 0
    print(Solution().countBits(n))
