# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = ListNode()
        first.next = head
        n1 = first
        n2 = head
        step = 0
        while n2:
            step += 1
            if step > n:
                n1 = n1.next
                step -= 1
            if not n2.next:
                after = n1.next
                n1.next = after.next if after else None
                break
            n2 = n2.next

        return first.next
