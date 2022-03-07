# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/


class Solution:
    def countOrders(self, n: int) -> int:
        count = 1

        for i in range(1, n+1):
            i = i*2 - 1
            val = (i+1) * (i//2)
            if i % 2 == 1:
                val += i//2 + 1

            count = (count * val) % (10**9 + 7)

        return count


if __name__ == '__main__':
    n = 500
    print(Solution().countOrders(n))
