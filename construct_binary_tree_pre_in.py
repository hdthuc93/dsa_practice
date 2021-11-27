# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


from typing import Optional, List
from typing_extensions import ParamSpec


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        d_inorder = {}
        idx = inorder.index(preorder[0])
        d_inorder[preorder[0]] = [(0, idx), (idx+1, len(preorder)), root]

        for i in range(1, len(preorder)):
            new_n = TreeNode(val=preorder[i])
            for j in range(i-1, -1, -1):
                l_range, r_range, n = d_inorder[preorder[j]]
                idx = -1
                for _range, child in zip([l_range, r_range], ['left', 'right']):
                    try:
                        idx = inorder[_range[0]:_range[1]].index(preorder[i])
                        setattr(n, child, new_n)
                        d_inorder[preorder[i]] = [(_range[0], _range[0]+idx), (_range[0]+idx+1, _range[1]), new_n]
                        break
                    except:
                        pass
                if idx != -1:
                    break
        return root
