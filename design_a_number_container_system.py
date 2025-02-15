# https://leetcode.com/problems/design-a-number-container-system/

import heapq
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self.idx_num = {}
        self.num_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx_num[index] = number
        heapq.heappush(self.num_indices[number], index)

    def find(self, number: int) -> int:
        indices = self.num_indices.get(number, [])
        while indices:
            smallest_idx = heapq.heappop(indices)
            if self.idx_num[smallest_idx] == number:
                heapq.heappush(indices, smallest_idx)
                return smallest_idx

        return -1


# Your NumberContainers object will be instantiated and called as such:
obj = NumberContainers()
obj.change(75, 40)
obj.change(27, 40)
obj.change(22, 14)
obj.change(85, 14)
obj.change(22, 40)
obj.change(18, 34)
obj.change(92, 41)
obj.change(22, 40)
obj.change(75, 40)
obj.change(59, 34)
param_2 = obj.find(40)
print(param_2)
