# https://leetcode.com/problems/univalued-binary-tree/


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        d_tree = {}
        def traverse(node):
            if not node.left and not node.right:
                return node.val, 1

            count = 1
            is_uni = True
            left_val, right_val = None, None
            left_count = right_count = 0
            if node.left:
                left_val, left_count = traverse(node.left)
                if left_val != node.val:
                    is_uni = False
            if node.right:
                right_val, right_count = traverse(node.right)
                if right_val != node.val:
                    is_uni = False

            if is_uni:
                count += left_count + right_count
            else:
                if left_val is not None and left_val != -1:
                    d_tree.setdefault(left_val, 0)
                    d_tree[left_val] += left_count
                if right_val is not None and right_val != -1:
                    d_tree.setdefault(right_val, 0)
                    d_tree[right_val] += right_count
                return -1, 0
            return node.val, count

        val, count = traverse(root)
        if val != -1:
            d_tree.setdefault(val, 0)
            d_tree[val] += count
            # print(d_tree)
        else:
            return False

        return len(list(d_tree.keys())) == 1
