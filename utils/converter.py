from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_binary_tree(lst):
    if not (lst and isinstance(lst, list) and len(lst)):
        return None

    root = TreeNode(lst[0])
    node = root

    q = Queue()
    q.put(node)

    for i in range(1, len(lst), 2):
        parent = q.get()
        if lst[i]:
            new_node = TreeNode(lst[i])
            parent.left = new_node
            q.put(new_node)
        if i+1 < len(lst) and lst[i+1]:
            new_node = TreeNode(lst[i+1])
            parent.right = new_node
            q.put(new_node)

    return root


def list_to_linked_list(lst):
    if not (lst and isinstance(lst, list) and len(lst)):
        return None

    head = ListNode()
    node = head
    for n in lst:
        new_node = ListNode(n)
        node.next = new_node
        node = node.next

    return head.next
