# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nof_dashes = 0
        root = None
        substring = ''
        is_num = True
        traversal_lst = []
        for c in traversal:
            if c == '-' and is_num:
                traversal_lst.append(int(substring))
                substring = ''
                is_num = False
            elif c != '-' and not is_num:
                traversal_lst.append('-' + str(len(substring)))
                substring = ''
                is_num = True
            substring += c

        traversal_lst.append(int(substring))
        print(traversal_lst)

        ranking_nodes = {}
        for val in traversal_lst:
            if not root:
                root = TreeNode(val)
                ranking_nodes[0] = [val]
                continue

            if isinstance(val, str):
                nof_dashes = int(val[1:])
            else:
                notes = ranking_nodes.get(nof_dashes-1, [])
                for note in reversed(notes):
                    rest_node = self.insert_node(note, val)
                    if rest_node:
                        ranking_nodes.setdefault(nof_dashes, [])
                        ranking_nodes[nof_dashes].append(rest_node)
                    break
                nof_dashes = 0

        return root

    def insert_node(self, node, val):
        if not node.left:
            node.left = TreeNode(val)
            return node.left
        elif not node.right:
            node.right = TreeNode(val)
            return node.right
        return None

if __name__ == '__main__':
    traversal = "1-2--3---4-5--6---7"
    sol = Solution()
    print(sol.recoverFromPreorder(traversal))
