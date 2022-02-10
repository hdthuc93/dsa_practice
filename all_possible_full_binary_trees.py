# https://leetcode.com/problems/all-possible-full-binary-trees/
from platform import node
from typing import List, Optional
from utils.converter import TreeNode, binary_tree_to_list


# TODO:
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []

        res = []

        def clone_tree(head):
            new_head = TreeNode(0)
            candidates = [[head, new_head]]
            while len(candidates):
                node, new_node = candidates.pop()
                if node.left:
                    new_node.left = TreeNode(0)
                    candidates.append([node.left, new_node.left])
                if node.right:
                    new_node.right = TreeNode(0)
                    candidates.append([node.right, new_node.right])
            return new_head

        def gen_tree(head, possibles, remain):
            if remain == 0:
                new_head = clone_tree(head)
                res.append(new_head)
                return

            while len(possibles):
                node = possibles.pop()
                node.left = TreeNode(0)
                node.right = TreeNode(0)
                new_possibles = possibles[:]
                new_possibles.append(node.left)
                new_possibles.append(node.right)
                gen_tree(head, new_possibles, remain-2)
                node.left = None
                node.right = None

        root = TreeNode(0)
        gen_tree(root, [root], n-1)
        return res


if __name__ == '__main__':
    n = 9
    res = Solution().allPossibleFBT(n)
    print(len(res))
    for r in res:
        print(binary_tree_to_list(r))

