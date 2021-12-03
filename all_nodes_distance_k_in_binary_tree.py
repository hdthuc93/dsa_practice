# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


from typing import List
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dist = {}
        res_vals = []
        def found_target(node):
            if node.val == target.val:
                return True, 0

            if node.left:
                found, d = found_target(node.left)
                if found:
                    dist[node.val] = d + 1
                    return True, d + 1

            if node.right:
                found, d = found_target(node.right)
                if found:
                    dist[node.val] = d + 1
                    return True, d + 1

            return False, 0

        found, d = found_target(root)
        if not found:
            return []

        dist[root.val] = d
        q = Queue()
        q.put([root, dist[root.val]])
        print(dist)
        while not q.empty():
            node, d = q.get()
            if node.val == target.val:
                d = 0

            if d == k:
                res_vals.append(node.val)

            if node.left:
                q.put([node.left, dist.get(node.left.val, d+1)])
            if node.right:
                q.put([node.right, dist.get(node.right.val, d+1)])

        return res_vals
