# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from typing import Optional
from utils.converter import TreeNode, list_to_binary_tree
from queue import Queue


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_lvls = {1:0}
        q = Queue()
        q.put((1, root))
        while not q.empty():
            lvl, node = q.get()
            sum_lvls.setdefault(lvl, 0)
            sum_lvls[lvl] += node.val
            if node.left:
                q.put((lvl + 1, node.left))
            if node.right:
                q.put((lvl + 1, node.right))

        max_sum = sum_lvls[1]
        smallest_lvl = 1
        lvl = 1
        while lvl in sum_lvls:
            if sum_lvls[lvl] > max_sum:
                max_sum = sum_lvls[lvl]
                smallest_lvl = lvl
            lvl += 1
        return smallest_lvl

    def maxLevelSum2(self, root: Optional[TreeNode]) -> int:
        sum_lvls = []
        def traverse(node, lvl):
            if not node: return
            if lvl >= len(sum_lvls):
                sum_lvls.append(0)
            sum_lvls[lvl] += node.val
            traverse(node.left, lvl + 1)
            traverse(node.right, lvl + 1)

        traverse(root, 0)
        return sum_lvls.index(max(sum_lvls)) + 1


if __name__ == '__main__':
    root = [1,7,0,7,-8,None,None]
    # root = [989,None,10250,98693,-89388,None,None,None,-32127]
    root = [13]
    root = list_to_binary_tree(root)
    print(Solution().maxLevelSum2(root))
