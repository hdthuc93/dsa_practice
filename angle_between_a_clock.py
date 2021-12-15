# https://leetcode.com/problems/angle-between-hands-of-a-clock/


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_hand = minutes / 5
        ratio = min_hand / 12
        hour_hand = hour + ratio
        angle = abs(hour_hand - min_hand) * 30
        return min(angle, 360-angle)


if __name__ == '__main__':
    hour = 11
    minutes = 34
    print(Solution().angleClock(hour, minutes))
