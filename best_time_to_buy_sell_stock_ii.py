# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[r-1]:
                min_price = 1e5
                while l < r-1:
                    min_price = min(prices[l], min_price)
                    l += 1
                if min_price != 1e5:
                    sum_profit += (prices[r-1] - min_price)
                l = r
            r += 1

        min_price = 1e5
        while l < r-1:
            min_price = min(prices[l], min_price)
            l += 1
        if min_price != 1e5:
            sum_profit += (prices[r-1] - min_price)

        return sum_profit
