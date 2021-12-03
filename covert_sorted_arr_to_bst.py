# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        s = [(root, (0, idx-1), (idx+1, len(nums)-1))]
        while len(s) > 0:
            node, left_side, right_side = s.pop()
            if left_side[0] <= left_side[1]:
                idx = (left_side[0] + left_side[1]) // 2
                node.left = TreeNode(nums[idx])
                s.append((node.left, (left_side[0], idx-1), (idx+1, left_side[1])))

            if right_side[0] <= right_side[1]:
                idx = (right_side[0] + right_side[1]) // 2
                node.right = TreeNode(nums[idx])
                s.append((node.right, (right_side[0], idx-1), (idx+1, right_side[1])))

        return root
