# https://leetcode.com/problems/partition-list/
from typing import Optional
from utils.converter import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None

        node = head
        s0 = []
        s1 = []
        while node:
            if node.val < x:
                s0.append(node)
            else:
                s1.append(node)
            node = node.next

        s = s0 + s1
        new_head = s[0]
        for i in range(1, len(s)):
            s[i-1].next = s[i]
        s[-1].next = None
        return new_head

    def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_lst = ListNode()
        large_lst = ListNode()
        small, large = small_lst, large_lst
        node = head
        while node:
            if node.val < x:
                small.next = node
                small = small.next
            else:
                large.next = node
                large = large.next
            node = node.next

        large.next = None
        small.next = large_lst.next
        return small_lst.next


if __name__ == '__main__':
    l = [1,4,3,2,5,2]
    x = 3
    # l = [2,1]
    # x = 2

    head = list_to_linked_list(l)
    res = Solution().partition2(head, x)
    print(linked_list_to_list(res))
