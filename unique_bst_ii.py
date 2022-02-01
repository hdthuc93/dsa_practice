# https://leetcode.com/problems/unique-binary-search-trees-ii/
from typing import List, Optional
from utils.converter import TreeNode, binary_tree_to_list


# TODO:
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        exists = [1] * (n+1)
        ans = []

        def clone_tree(head):
            new_head = TreeNode(head.val)
            node_stacks = [head]
            new_node_stacks = [new_head]

            while len(node_stacks):
                node = node_stacks.pop()
                new_node = new_node_stacks.pop()
                if node.left:
                    new_node.left = TreeNode(node.left.val)
                    node_stacks.append(node.left)
                    new_node_stacks.append(new_node.left)

                if node.right:
                    new_node.right = TreeNode(node.right.val)
                    node_stacks.append(node.right)
                    new_node_stacks.append(new_node.right)

            return new_head

        def create_tree(head, node, n):
            if sum(exists[1:]) == 0:
                ans.append(clone_tree(head))
                return

            left = node.val-1
            while left > 0:
                if exists[left]:
                    exists[left] = 0
                    node.left = TreeNode(left)
                    create_tree(head, node.left, n)
                    node.left = None
                    exists[left] = 1
                left -= 1

            right = node.val + 1
            while right <= n:
                if exists[right]:
                    exists[right] = 0
                    node.right = TreeNode(right)
                    create_tree(head, node.right, n)
                    node.right = None
                    exists[right] = 1
                right += 1

            # left = node.val-1
            # while left > 0:
            #     if exists[left]:
            #         exists[left] = 0
            #         node.left = TreeNode(left)
            #         right = node.val + 1
            #         while right <= n:
            #             if exists[right]:
            #                 exists[right] = 0
            #                 node.right = TreeNode(right)

        for i in range(1, n+1):
            head = TreeNode(i)
            exists[i] = 0
            create_tree(head, head, n)
            exists[i] = 1

        return ans


if __name__ == '__main__':
    n = 3
    ans = Solution().generateTrees(n)

    for tree_head in ans:
        print(binary_tree_to_list(tree_head))
