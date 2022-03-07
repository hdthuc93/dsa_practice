# https://leetcode.com/problems/path-sum/
from typing import Optional
from utils.converter import TreeNode, list_to_binary_tree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find_target_sum(node, cur_sum, targetSum):
            if node.left:
                if find_target_sum(node.left, cur_sum + node.val, targetSum):
                    return True

            if node.right:
                if find_target_sum(node.right, cur_sum + node.val, targetSum):
                    return True

            if not node.left and not node.right:
                return cur_sum + node.val == targetSum
            return False
        if not root: return False
        return find_target_sum(root, 0, targetSum)


if __name__ == '__main__':
    l = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum = 22
    l = [1,2,3]
    targetSum = 5
    l = [3]
    targetSum = 3

    root = list_to_binary_tree(l)
    print(Solution().hasPathSum(root, targetSum))
