# https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        node = head
        while node:
            next_node = node.next
            node.next = reverse
            reverse = node
            node = next_node
        return reverse

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(node, reverse, reverse_head):
            if node.next:
                reverse, reverse_head = recursive(node.next, reverse, reverse_head)

            if not reverse_head:
                reverse = node
                reverse_head = reverse
            else:
                reverse.next = node
                reverse = reverse.next
            node.next = None

            return reverse, reverse_head

        reverse_head = None
        if head:
            _, reverse_head = recursive(head, None, None)
        return reverse_head
