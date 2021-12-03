# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def traverse(node, max_sum):
            if not node.left and not node.right:
                max_sum = max(max_sum, node.val)
                return [node.val], max_sum, node.val

            l_sides = []
            r_sides = []
            l_sum = r_sum = 0
            if node.left:
                l_sides, max_sum, l_sum = traverse(node.left, max_sum)
            if node.right:
                r_sides, max_sum, r_sum = traverse(node.right, max_sum)

            is_correct = True if l_sides is not None and r_sides is not None else False

            if l_sides and len(l_sides):
                if node.val <= l_sides[-1]:
                    is_correct = False

            if r_sides and len(r_sides):
                if node.val >= r_sides[0]:
                    is_correct = False

            lst = None
            s = 0
            if is_correct:
                s = node.val + l_sum + r_sum
                max_sum = max(max_sum, s)
                lst = []
                if len(l_sides):
                    lst.append(l_sides[0])
                lst.append(node.val)
                if len(r_sides):
                    lst.append(r_sides[-1])
                lst = [lst[0], lst[-1]]

            return lst, max_sum, s

        _, max_sum, _ = traverse(root, -4e4-2)
        return max(max_sum, 0)
