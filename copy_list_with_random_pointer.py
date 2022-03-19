# https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        def copy_random(head, node, new_head, new_node):
            random_node = node.random
            node = head
            node2 = new_head
            while node:
                if node == random_node:
                    new_node.random = node2
                    break
                node = node.next
                node2 = node2.next

        new_head = Node(head.val)
        new_node = new_head
        node = head.next

        while node:
            new_node.next = Node(node.val)
            node = node.next
            new_node = new_node.next

        new_node = new_head
        node = head
        while node:
            if node.random:
                copy_random(head, node, new_head, new_node)
            node = node.next
            new_node = new_node.next

        return new_head
