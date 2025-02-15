# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

from queue import Queue


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def run_bfs_in_num(num_square_str, num):
            q = Queue()
            q.put((int(num_square_str[0]), 0, 0))

            while not q.empty():
                # print(q)
                val, sum_val, idx = q.get()
                # print(val, sum_val, idx)
                if val + sum_val > num:
                    continue
                if idx + 1 == len(num_square_str):
                    if val + sum_val == num:
                        return True
                    continue

                if idx + 1 < len(num_square_str):
                    q.put((val*10 + int(num_square_str[idx+1]), sum_val, idx+1))
                    q.put((int(num_square_str[idx+1]), sum_val + val, idx+1))

            return False

        res = 0
        for num in range(1, n+1):
            if run_bfs_in_num(str(num**2), num):
                res += num**2

        return res


sol = Solution()
import time
start = time.time()
for i in range(1, 200):
    sol.punishmentNumber(i)
print(time.time() - start)

# print(sol.punishmentNumber(1000))
# print(sol.punishmentNumber(1000))
# print(sol.punishmentNumber(1))
