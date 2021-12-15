# https://techiedelight.com/practice/?problem=TruncateBinaryTree


from queue import Queue


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data	# data field
        self.left = left	# pointer to the left child
        self.right = right	# pointer to the right child


class Solution:
    def truncate(self, root: Node) -> Node:
        # Write your code here...
        if not root:
            return None

        head = Node()
        head.left = root
        q = Queue()
        q.put([root, head])

        while not q.empty():
            node, parent = q.get()
            if node.left and node.right:
                q.put([node.left, node])
                q.put([node.right, node])
            elif node.left:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                q.put([node.left, parent])
            elif node.right:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                q.put([node.right, parent])
        return head.left


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)

    root.left.left = Node(3)
    root.left.left.left = Node(5)

    root.right.left = Node(4)
    node = root.right.left
    node.left = Node(6)
    node.right = Node(7)

    new_root = Solution().truncate(root)
    print(new_root.data)
    print(new_root.left.data)
    print(new_root.right.data)

    print(new_root.left.left)
    print(new_root.left.right)

    print(new_root.right.left.data)
    print(new_root.right.right.data)
