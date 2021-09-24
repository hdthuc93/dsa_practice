# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3838/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        result = []
        if not root:
            return result

        stack = [{'node': root, 'lst': [], 'sum': 0}]

        while len(stack) != 0:
            item = stack.pop()
            node = item.get('node')

            current_sum = item.get('sum') + node.val
            lst = item.get('lst')[:]
            lst.append(node.val)

            if node.left:
                stack.append({'node': node.left, 'lst': lst[:], 'sum': current_sum})
            if node.right:
                stack.append({'node': node.right, 'lst': lst[:], 'sum': current_sum})

            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(lst[:])

        return result

    def pathSum1(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        result = []
        node = root
        current_sum = 0
        self.run(result, [], current_sum, targetSum, node)
        return result

    def run(self, result, current_lst, current_sum, targetSum, node):
        current_lst.append(node.val)
        current_sum += node.val

        if node.left:
            self.run(result, current_lst[:], current_sum, targetSum, node.left)

        if node.right:
            self.run(result, current_lst[:], current_sum, targetSum, node.right)

        if not node.left and not node.right:
            if current_sum == targetSum:
                result.append(current_lst[:])
