# https://leetcode.com/problems/max-points-on-a-line/


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        d_lines = {}
        def calc_ab(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            ab = ()
            if x1 == x2:
                ab = (x1, None)
            elif y1 == y2:
                ab = (None, y1)
            else:
                a = (y1-y2) / (x1-x2)
                b = y1 - a*x1
                ab = (a, b)

            d_lines.setdefault(ab, set())
            d_lines[ab].add(tuple(p1))
            d_lines[ab].add(tuple(p2))

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                calc_ab(points[i], points[j])

        count_points = 0
        for _, s in d_lines.items():
            count_points = max(count_points, len(list(s)))

        return count_points


if __name__ == '__main__':
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(Solution().maxPoints(points))
