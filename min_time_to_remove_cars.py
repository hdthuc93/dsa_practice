# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

# TODO
class Solution:
    def minimumTime(self, s: str) -> int:
        size = len(s)
        left_removes = []
        right_removes = [[0, 0] for _ in range(size)]
        prev_idx = -1
        for i in range(size):
            if s[i] == '1':
                left = i - prev_idx
                anywhere = 2
                if i-1 >= 0:
                    left += left_removes[i-1][0]
                    anywhere = min(left_removes[i-1][1] + 2, left_removes[i-1][0] + 2)
                prev_idx = i
                left_removes.append([left, anywhere])
            else:
                if len(left_removes):
                    left_removes.append([left_removes[-1][0], left_removes[-1][1]])
                else:
                    left_removes.append([0, 0])

        prev_idx = size
        for i in range(size-1, -1, -1):
            if s[i] == '1':
                right = prev_idx - i
                anywhere = 2
                if i+1 < size:
                    right += right_removes[i+1][0]
                    anywhere = min(right_removes[i+1][1] + 2, right_removes[i+1][0] + 2)
                prev_idx = i
                right_removes[i] = [right, anywhere]
            else:
                if i+1 < size:
                    right_removes[i] = [right_removes[i+1][0], right_removes[i+1][1]]

        min_remove = min(right_removes[0])
        min_remove = min(min_remove, min(left_removes[-1]))

        for i in range(1, size-1):
            remove = min(left_removes[i]) + min(right_removes[i+1])
            remove = min(remove, min(left_removes[i-1]) + min(right_removes[i]))
            min_remove = min(min_remove, remove)

        return min_remove


if __name__ == '__main__':
    s = ''
    print(Solution().minimumTime(s))
