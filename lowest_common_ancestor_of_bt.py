# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
from utils.converter import list_to_binary_tree, TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [None]
        target = [p.val, q.val]
        def traverse(node):
            l_val = r_val = -1
            if node.left:
                l_val = traverse(node.left)
            if node.right:
                r_val = traverse(node.right)

            if l_val in target and r_val in target:
                res[0] = node
            elif node.val in target and (l_val in target or r_val in target):
                res[0] = node
                return -1
            elif l_val in target:
                return l_val
            elif r_val in target:
                return r_val

            if node.val in target:
                return node.val

            return -1

        traverse(root)
        return res[0]


if __name__ == '__main__':
    # root = [3,5,1,6,2,0,8,None,None,7,4]
    # p = 5
    # q = 4
    root = [1,2]
    p = 1
    q = 2
    root = list_to_binary_tree(root)
    print(Solution().lowestCommonAncestor(root, TreeNode(p), TreeNode(q)).val)
