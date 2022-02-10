# https://leetcode.com/problems/coin-change-2/
from typing import List
from queue import Queue
import heapq


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[amount]


if __name__ == '__main__':
    amount = 10
    coins = [1,2,5]
    # amount = 3
    # coins = [2]
    # amount = 10
    # coins = [10]
    amount = 500
    coins = [3,5,7,8,9,10,11]
    print(Solution().change(amount, coins))
