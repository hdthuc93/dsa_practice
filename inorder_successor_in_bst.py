# https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1/#
from utils.converter import list_to_binary_tree


class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        def run_inorder_successor(node, x, reached_x):
            if node.left:
                left, reached_x = run_inorder_successor(node.left, x, reached_x)
                if reached_x:
                    if left:
                        return left, reached_x
                    elif node.val > x:
                        return node, reached_x

            if node.val == x:
                reached_x = True

            if node.right:
                right, reached_x = run_inorder_successor(node.right, x, reached_x)
                if reached_x:
                    if right:
                        return right, reached_x
                    elif node.val > x:
                        return node, reached_x

            if reached_x and not node.left and not node.right and node.val != x:
                return node, reached_x

            return None, reached_x

        res_node, _ = run_inorder_successor(root, x, False)
        return res_node


if __name__ == '__main__':
    l = [2, 1, 3]
    x = 2

    l = [20, 8, 22, 4, 12, None, None, None, None, 10, 14]
    x = 12

    root = list_to_binary_tree(l)
    res_node = Solution().inorderSuccessor(root, x)
    print(res_node.val)
