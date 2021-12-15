# https://leetcode.com/problems/intersection-of-two-linked-lists/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = n = 0
        node = headA
        while node:
            m += 1
            node = node.next
        node = headB
        while node:
            n += 1
            node = node.next

        nodeA = headA
        nodeB = headB
        if m > n:
            i = 0
            while m - i > n:
                nodeA = nodeA.next
                i += 1
        elif m < n:
            i = 0
            while n - i > m:
                nodeB = nodeB.next
                i += 1

        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        return None
