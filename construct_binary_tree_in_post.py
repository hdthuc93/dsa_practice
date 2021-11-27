# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


from typing import Optional, List
from typing_extensions import ParamSpec


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder = postorder[::-1]
        root = TreeNode(val=postorder[0])
        d_inorder = {}
        idx = inorder.index(postorder[0])
        d_inorder[postorder[0]] = [inorder[:idx], inorder[idx+1:], root]

        for i in range(1, len(postorder)):
            new_n = TreeNode(val=postorder[i])
            for j in range(i-1, -1, -1):
                l_inorder, r_inorder, n = d_inorder[postorder[j]]
                idx = -1
                for _inorder, child in zip([l_inorder, r_inorder], ['left', 'right']):
                    try:
                        idx = _inorder.index(postorder[i])
                        setattr(n, child, new_n)
                        d_inorder[postorder[i]] = [_inorder[:idx], _inorder[idx+1:], new_n]
                        break
                    except:
                        pass
                if idx != -1:
                    break
        return root
