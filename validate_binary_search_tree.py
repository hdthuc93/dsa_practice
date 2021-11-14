# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_parent(node, l_lst, r_lst):
            for lval in l_lst:
                if node.val <= lval:
                    return False

            for rval in r_lst:
                if node.val >= rval:
                    return False

            if node.left:
                r_lst.append(node.val)
                res = check_parent(node.left, l_lst, r_lst)
                if not res:
                    return False
                r_lst.pop()
            if node.right:
                l_lst.append(node.val)
                res = check_parent(node.right, l_lst, r_lst)
                if not res:
                    return False
                l_lst.pop()

            return True

        return check_parent(root, [], [])


if __name__ == '__main__':
    pass
