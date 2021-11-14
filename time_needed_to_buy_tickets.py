# https://leetcode.com/problems/time-needed-to-buy-tickets/


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        target = tickets[k]
        time_taken = target * len(tickets)
        remain = 0
        for i in range(len(tickets)):
            if i > k and tickets[i] >= target:
                remain += 1
            if tickets[i] - target < 0:
                time_taken += (tickets[i] - target)
        return time_taken - remain

    def timeRequiredToBuy2(self, tickets: list[int], k: int) -> int:
        from queue import Queue
        q = Queue()
        for i in range(len(tickets)):
            q.put([i, tickets[i]])

        time_taken = 0
        while not q.empty():
            idx, t = q.get()
            t -= 1
            time_taken += 1
            if t != 0:
                q.put([idx, t])
            elif k == idx:
                break
        return time_taken


if __name__ == '__main__':
    tickets = [6,1,3,5,1,1,3]
    k = 2
    print(Solution().timeRequiredToBuy(tickets, k))
