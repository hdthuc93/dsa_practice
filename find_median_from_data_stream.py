# https://leetcode.com/problems/find-median-from-data-stream/


import heapq


class MedianFinder:

    def __init__(self):
        self.left_sides = []
        self.right_sides = []
        self.medians = []
        self.len = 0

    def addNum(self, num: int) -> None:
        if len(self.medians) < 2:
            self.medians.append(num)
            self.medians.sort()
        else:
            if num < self.medians[0]:
                heapq.heappush(self.left_sides, -num)
            elif num > self.medians[1]:
                heapq.heappush(self.right_sides, num)
            else:
                heapq.heappush(self.left_sides, -self.medians[0])
                self.medians = [num, self.medians[1]]

        if len(self.left_sides) - len(self.right_sides) > 1:
            n = -heapq.heappop(self.left_sides)
            heapq.heappush(self.right_sides, self.medians[1])
            self.medians = [n, self.medians[0]]
        elif len(self.right_sides) - len(self.left_sides) > 0:
            n = heapq.heappop(self.right_sides)
            heapq.heappush(self.left_sides, -self.medians[0])
            self.medians = [self.medians[1], n]

        self.len += 1

    def findMedian(self) -> float:
        if self.len % 2 == 0:
            return sum(self.medians)/2
        return self.medians[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
