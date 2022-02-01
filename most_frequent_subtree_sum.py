# https://leetcode.com/problems/most-frequent-subtree-sum/
from typing import Optional, List
from utils.converter import TreeNode, list_to_binary_tree


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        d_sum = {}

        def traverse(node):
            sum_left = sum_right = None
            if node.left:
                sum_left = traverse(node.left)
            if node.right:
                sum_right = traverse(node.right)

            cur_sum = node.val
            if sum_left is not None:
                cur_sum += sum_left
            if sum_right is not None:
                cur_sum += sum_right

            d_sum.setdefault(cur_sum, 0)
            d_sum[cur_sum] += 1
            return cur_sum

        traverse(root)
        print(d_sum)
        max_count = max(d_sum.values())
        res = []
        for k, v in d_sum.items():
            if v == max_count:
                res.append(k)

        return res


if __name__ == '__main__':
    root = [5,2,-5]

    root = list_to_binary_tree(root)
    print(Solution().findFrequentTreeSum(root))
