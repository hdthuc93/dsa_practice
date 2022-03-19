# https://leetcode.com/problems/validate-stack-sequences/
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for n in pushed:
            stack.append(n)
            while j < len(popped) and len(stack) and popped[j] == stack[-1]:
                stack.pop()
                j += 1

        while j < len(popped):
            if not len(stack) or popped[j] != stack[-1]:
                return False
            stack.pop()
            j += 1

        return True


if __name__ == '__main__':
    pushed = [1,2,3,4,5]
    popped = [4,3,2,1,5]

    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print(Solution().validateStackSequences(pushed, popped))
