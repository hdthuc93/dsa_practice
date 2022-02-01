# https://leetcode.com/problems/all-possible-full-binary-trees/
from typing import List, Optional
from utils.converter import TreeNode, binary_tree_to_list


# TODO:
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []

        def clone_tree(node, new_node, target_node, return_node, leaves):
            if target_node == node:
                return_node.append(new_node)

            if not (node.left and node.right):
                leaves.append(new_node)
                return

            if node.left:
                new_node.left = TreeNode(0)
                clone_tree(node.left, new_node.left, target_node, return_node, leaves)
            if node.right:
                new_node.right = TreeNode(0)
                clone_tree(node.right, new_node.right, target_node, return_node, leaves)

        root = TreeNode(0)
        res = [(root, root)]
        i = 3
        while i <= n:
            new_res = []
            res_set = set()
            for head, node in res:
                clone = TreeNode(0)
                new_node = []
                new_leaves = []
                clone_tree(head, clone, node, new_node, new_leaves)
                new_node = new_node[0]
                # new_res.append((clone, new_node))

                new_node.left = TreeNode(0)
                new_node.right = TreeNode(0)

                tree_tup = tuple(binary_tree_to_list(clone))
                # print(i, tree_tup)
                if tree_tup not in res_set:
                    res_set.add(tree_tup)
                    for _node in [new_node.left, new_node.right]:
                        new_res.append((clone, _node))
                    for _node in new_leaves:
                        if _node == new_node: continue
                        new_res.append((clone, _node))

            # print(len(new_res))
            # print(res_set)
            res = new_res

            i += 2

        new_res = []
        res_set = set()
        # print('res', res)
        # for r, _ in res:
        #     print(i, binary_tree_to_list(r))
        for r, _ in res:
            tree_tup = tuple(binary_tree_to_list(r))
            # print(tree_tup)
            if tree_tup not in res_set:
                res_set.add(tree_tup)
                new_res.append(r)
        return new_res


if __name__ == '__main__':
    n = 19
    res = Solution().allPossibleFBT(n)
    print(len(res))
    # for r in res:
    #     print(binary_tree_to_list(r))

