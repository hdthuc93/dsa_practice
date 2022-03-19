# https://leetcode.com/problems/add-two-numbers/
from typing import Optional
from utils.converter import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        remain = 0
        head = ListNode()
        node = head
        while node1 and node2:
            node.next = ListNode()
            node = node.next

            node.val = node1.val + node2.val + remain
            remain = node.val // 10
            node.val = node.val % 10

            node1 = node1.next
            node2 = node2.next

        while node1:
            node.next = ListNode()
            node = node.next

            node.val = node1.val + remain
            remain = node.val // 10
            node.val = node.val % 10

            node1 = node1.next

        while node2:
            node.next = ListNode()
            node = node.next

            node.val = node2.val + remain
            remain = node.val // 10
            node.val = node.val % 10

            node2 = node2.next

        if remain > 0:
            node.next = ListNode(val=remain)

        return head.next


if __name__ == '__main__':
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    l_res = Solution().addTwoNumbers(list_to_linked_list(l1), list_to_linked_list(l2))
    print(linked_list_to_list(l_res))
