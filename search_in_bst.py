# https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional
from utils.converter import TreeNode, list_to_binary_tree


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ceil = [10000002]
        floor = [0]

        def run_search(node):
            if node.val == val:
                ceil[0] = val
                floor[0] = val
                return node
            elif node.val > val:
                ceil[0] = min(ceil[0], node.val)
                if node.left:
                    left_node = run_search(node.left)
                    if left_node:
                        return left_node
            else:
                floor[0] = max(floor[0], node.val)
                if node.right:
                    right_node = run_search(node.right)
                    if right_node:
                        return right_node

            return None

        node = run_search(root)
        print(floor[0], ceil[0])
        return node


if __name__ == '__main__':
    root = [4,2,7,1,3]
    val = 2
    root = [8,4,12,2,6,10,14]
    val = 5

    root = list_to_binary_tree(root)
    print(Solution().searchBST(root, val))
