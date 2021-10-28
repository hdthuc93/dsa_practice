# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        from collections import deque
        if amount == 0:
            return 0

        q = deque()
        for c in coins:
            q.append([c, 1])

        min_coin = -1
        visited = [False]*(10000 + 1)
        while q:
            cur_sum, cur_len = q.popleft()
            if cur_sum == amount:
                min_coin = min(min_coin, cur_len) if min_coin != -1 else cur_len

            for c in coins:
                if c + cur_sum <= amount and not visited[c+cur_sum]:
                    visited[c+cur_sum] = True
                    q.append([c+cur_sum, cur_len+1])

        return min_coin


if __name__ == '__main__':
    coins = [83,186,408,419]
    amount = 6249
    # coins = [3,7,405,436]
    # amount = 8839
    # coins = [3,7,11]
    # amount = 24
    print(Solution().coinChange(coins, amount))
