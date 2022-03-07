# https://leetcode.com/problems/swap-nodes-in-pairs/
from typing import Optional
from utils.converter import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head

        head, node = prev, head
        while node and node.next:
            node_next = node.next
            node.next = node_next.next
            node_next.next = node
            prev.next = node_next
            prev = node
            node = node.next

        return head.next


if __name__ == '__main__':
    l = [1]
    l = [1,2]
    head = list_to_linked_list(l)
    res = Solution().swapPairs(head)
    print(linked_list_to_list(res))
