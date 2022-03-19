# https://leetcode.com/problems/rotate-list/
from typing import Optional
from utils.converter import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        from collections import deque
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        if n > 0:
            k %= n

        node = head
        q = deque()
        i = 0
        while node:
            q.append(node.val)
            if i >= k:
                node.val = q.popleft()
            i += 1
            node = node.next

        node = head
        while q:
            node.val = q.popleft()
            node = node.next

        return head

    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        if n > 0:
            k %= n

        if k == 0: return head

        new_head = None
        node = head
        for _ in range(n-k):
            node = node.next
        new_head = node
        res_node = head

        while node and node.next:
            node = node.next
        node.next = head

        while res_node and res_node.next:
            if res_node.next == new_head:
                res_node.next = None
                break
            res_node = res_node.next

        return new_head


if __name__ == '__main__':
    head = [1,2,3,4,5]
    k = 1
    # head = [0,1,2]
    # k = 444442
    head = []
    k = 444442
    head = [1]
    k = 1

    res = Solution().rotateRight2(list_to_linked_list(head), k)
    print(linked_list_to_list(res))
