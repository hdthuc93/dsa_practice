# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        new_lst = [intervals[0]]
        for n1, n2 in intervals[1:]:
            last_tup = new_lst[-1]
            if last_tup[0] <= n1 <= last_tup[1]:
                min_val = min(n1, n2, last_tup[0], last_tup[1])
                max_val = max(n1, n2, last_tup[0], last_tup[1])
                new_lst[-1] = (min_val, max_val)
            else:
                new_lst.append((n1, n2))

        return new_lst


if __name__ == '__main__':
    intervals = []
    print(Solution().merge(intervals))
