from typing import Optional, List
from utils.converter import list_to_linked_list, linked_list_to_list, ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node = head
        prev_node = ListNode(val=101)
        prev_node.next = head
        node = prev_node

        while node:
            next_node = node.next
            is_duplicated = False
            while next_node and next_node.next and \
                  next_node.val == next_node.next.val:
                next_node.next = next_node.next.next
                is_duplicated = True

            if is_duplicated:
                node.next = next_node.next if next_node else None
            else:
                node = node.next

        return prev_node.next


if __name__ == '__main__':
    lst = [1,2,3,3,4,4,5]
    lst = [1,1,1,2,3]
    lst = [1,1,1]
    lst = []
    head = list_to_linked_list(lst)
    print(linked_list_to_list(Solution().deleteDuplicates(head)))
