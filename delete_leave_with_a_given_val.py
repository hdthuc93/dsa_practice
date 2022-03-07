# https://leetcode.com/problems/delete-leaves-with-a-given-value/
from typing import Optional
from utils.converter import TreeNode, list_to_binary_tree, binary_tree_to_list


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def run_remove(node, target):
            remove_left = remove_right = False
            if node.left:
                remove_left = run_remove(node.left, target)
                if remove_left:
                    node.left = None
            if node.right:
                remove_right = run_remove(node.right, target)
                if remove_right:
                    node.right = None

            if not node.left and not node.right and node.val == target:
                return True

            return False

        if run_remove(root, target):
            return None

        return root


if __name__ == '__main__':
    l = [1,2,3,2,None,2,4]
    target = 2
    l = [1,3,3,3,2]
    target = 3
    l = [1,2,None,2,None,2]
    target = 2

    root = list_to_binary_tree(l)
    res = Solution().removeLeafNodes(root, target)
    print(binary_tree_to_list(res))
