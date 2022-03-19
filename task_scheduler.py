# https://leetcode.com/problems/task-scheduler/
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import Counter
        counter_tasks = Counter(tasks)
        d_times = {0: []}
        for k, v in counter_tasks.items():
            heapq.heappush(d_times[0], (-v, k))

        t = 0
        i = 0
        # max_key = 0
        while i > t + n + 1:
            hq = []
            if d_times.get(t):
                hq = d_times[t]
            elif d_times.get(i):
                hq = d_times[i]
            else:
                i += 1

            remain = heapq.heappop(hq)
            remain = -remain

            t += 1

        return t

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counts = Counter(tasks)
        longest = None
        for key in counts:
            if longest == None:
                longest = key
            elif counts[key] > counts[longest]:
                longest = key

        l_c = counts[longest]

        time = l_c
        gap = (l_c - 1) * n

        for key in counts:
            if key != longest:
                time += counts[key]
                gap -= min(l_c - 1, counts[key])

        if gap > 0:
            time += gap

        return time


if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B","C","C","C","D","D","D"]
    n = 2
    # tasks = ["A","A","A","B","B","B"]
    # n = 0
    # tasks = ["A","A","A","A","A","A","B","C","D","E","F","G", "B", "B", "C"]
    # n = 2
    # tasks = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'E']
    # n = 2
    # tasks = ["A","A","A","B","B","B"]
    # n = 2
    print(Solution().leastInterval2(tasks, n))
