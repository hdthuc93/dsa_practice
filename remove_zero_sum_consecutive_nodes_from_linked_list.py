# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/submissions/


from typing import Optional
from queue import Queue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        s = set()
        first = ListNode()
        first.next = head
        prev_nodes = [[0, first]]
        while node:
            if node.val == 0:
                prev_nodes[-1][1].next = node.next
                node = node.next
                continue

            cur_s = prev_nodes[-1][0] + node.val
            if cur_s == 0:
                s = set()
                prev_nodes[0][1].next = node.next
                prev_nodes = prev_nodes[:1]
            elif cur_s in s:
                for i in range(len(prev_nodes)-1, 0, -1):
                    _sum, n = prev_nodes[i]
                    if _sum == cur_s:
                        n.next = node.next
                        prev_nodes = prev_nodes[:i+1]
                        break
                    s.remove(_sum)
            else:
                prev_nodes.append([cur_s, node])
                s.add(cur_s)
            node = node.next
        if len(prev_nodes) > 1:
            return prev_nodes[1][1]
        return None

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashtable = {}
        first = ListNode()
        first.next = head
        prev_node = first
        node = head
        s = 0
        while node:
            s = s + node.val
            if s == 0:
                hashtable = {}
                first.next = node.next
                prev_node


if __name__ == '__main__':
    nums = [1,2,-3,3,1,-3]
    nums = [1,2,-3,3,-2,-1]
    nums = [1,2,0,-2,0,0,-1,2,3,4]
    # nums = [1,2,3,-3,4]
    # nums = [1,2,3,-3,-2]
    # nums = [5,-3,-4,1,6,-2,-5]
    # nums = [1,2,3,-4,1,5]
    head = ListNode()
    node = head
    for n in nums:
        node.next = ListNode(val=n)
        node = node.next
    res_node = Solution().removeZeroSumSublists(head.next)
    while res_node:
        print(res_node.val)
        res_node = res_node.next
