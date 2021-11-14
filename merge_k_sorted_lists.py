# https://leetcode.com/problems/merge-k-sorted-lists/


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        root = ListNode()
        node = root
        dn = {}
        hq = []

        # init queue
        for l in lists:
            if l:
                dn.setdefault(l.val, [])
                heapq.heappush(hq, l.val)
                dn[l.val].append(l)

        while len(hq):
            v = heapq.heappop(hq)
            n = dn[v].pop()
            node.next = n
            n = n.next
            if n:
                dn.setdefault(n.val, [])
                heapq.heappush(hq, n.val)
                dn[n.val].append(n)

        return root.next


if __name__ == '__main__':
    pass
