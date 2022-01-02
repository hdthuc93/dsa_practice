# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional
from utils.converter import ListNode, list_to_linked_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node0 = head
        node1 = head
        n = 0
        while node0:
            n += 1
            node0 = node0.next

        target = n//2 if n%2 else n//2 - 1
        node0 = head
        while target > 0:
            target -= 1
            node0 = node0.next

        if n % 2 == 0:
            temp = node0
            node0 = node0.next
            temp.next = None

        prev_node = node0
        node0 = node0.next
        prev_node.next = None
        while node0:
            next_node = node0.next
            node0.next = prev_node
            prev_node = node0
            node0 = next_node

        node0 = prev_node
        target = n//2 if n%2 else n//2 - 1
        while target >= 0:
            if node0.val != node1.val:
                return False
            node0 = node0.next
            node1 = node1.next
            target -= 1
        return True


if __name__ == '__main__':
    head = [1,2,3,2,1]
    head = [1,2,2,1]
    head = [1,3,2,4,3,2,1]
    # head = [1,2]
    head = list_to_linked_list(head)
    print(Solution().isPalindrome(head))
