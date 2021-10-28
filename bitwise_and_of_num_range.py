# https://leetcode.com/problems/bitwise-and-of-numbers-range/


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right: return left

        def get_sub_result(left, right, res):
            start = end = 0
            for i in range(32):
                if 2**i > right:
                    end = i
                    break
                if 2**i <= left:
                    start = i
                    continue

            if start != 0 and start == end - 1:
                res += 2**start
                res = get_sub_result(left-2**start, right-2**start, res)
            return res

        return get_sub_result(left, right, 0)

    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        res = left
        for num in range(left+1, right+1):
            res &= num
        return res


if __name__ == '__main__':
    left = 19
    right = 21
    print(Solution().rangeBitwiseAnd(left, right))
    print(Solution().rangeBitwiseAnd2(left, right))
