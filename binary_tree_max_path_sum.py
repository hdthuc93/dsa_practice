# https://leetcode.com/problems/binary-tree-maximum-path-sum/
from typing import Optional
from utils.converter import list_to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def find_max(node):
            if not node.left and not node.right:
                return node.val, node.val

            sum_left = sum_right = -1
            max_left = max_right = -1e10

            if node.left:
                sum_left, max_left = find_max(node.left)
            if node.right:
                sum_right, max_right = find_max(node.right)

            cur_sum = max([node.val, sum_left + node.val, sum_right + node.val])
            cur_max = max([cur_sum, max_left, max_right, node.val + sum_right + sum_left])

            return cur_sum, cur_max

        _, max_val = find_max(root)
        return max_val


if __name__ == '__main__':
    root = [1,2,3]
    root = [3]
    # root = [-10,9,20,None,None,15,7]
    root = [10, 2, 10, 20, 1, None, -25, None, None, None, None, 3, 4]
    root = list_to_binary_tree(root)
    print(Solution().maxPathSum(root))
