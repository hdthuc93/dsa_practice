# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
from utils.converter import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
