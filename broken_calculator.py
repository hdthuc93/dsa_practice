# https://leetcode.com/problems/broken-calculator/


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target < startValue:
            return startValue - target
        val = target
        step = 0
        while val > startValue:
            if val % 2 == 0:
                val = val // 2
            else:
                val += 1
            step += 1

        return step + (startValue - val)


if __name__ == '__main__':
    startValue = 2
    target = 3
    startValue = 5
    target = 8
    startValue = 3
    target = 10**9
    startValue = 10**9
    target = 2
    print(Solution().brokenCalc(startValue, target))
