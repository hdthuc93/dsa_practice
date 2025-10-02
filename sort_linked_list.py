# https://leetcode.com/problems/sort-list/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(orig_node, depth) -> ListNode:
            if not orig_node or not orig_node.next:
                return orig_node

            node = orig_node
            fast_node = orig_node.next
            while fast_node and fast_node.next:
                node = node.next
                fast_node = fast_node.next.next

            second_half = node.next
            node.next = None

            left = mergeSort(orig_node, depth+1)
            right = mergeSort(second_half, depth+1)

            # debug
            lnode = left
            lnums = []
            while lnode:
                lnums.append(lnode.val)
                lnode = lnode.next

            rnode = right
            rnums = []
            while rnode:
                rnums.append(rnode.val)
                rnode = rnode.next

            print(depth, lnums, rnums)
            ##############

            # merge
            # if depth == 1:
            #     import pdb; pdb.set_trace()

            new_head = ListNode()
            node = new_head
            while left and right:
                if left.val <= right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
                node = node.next

            node.next = left if left else right

            return new_head.next

        head = mergeSort(head, 1)
        return head


# 4 2 1 3
# 2 4 1 3
# 1 4 2 3
nums = [6,4,8,9,1,7,3,2,10,5]
print(nums)
head = ListNode(val=nums[0])
node = head

for num in nums[1:]:
    node.next = ListNode(val=num)
    node = node.next

head = Solution().sortList(head)
node = head
sorted_nums = []

while node:
    sorted_nums.append(node.val)
    node = node.next

print(sorted_nums)
