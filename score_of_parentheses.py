# https://leetcode.com/problems/score-of-parentheses/


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        scores_lvl = {}
        lvl = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
                lvl += 1
                scores_lvl.setdefault(lvl, [])
            else:
                stack.pop()
                if len(scores_lvl.get(lvl+1, [])):
                    scores_lvl[lvl].append(sum(scores_lvl[lvl+1])*2)
                    scores_lvl[lvl + 1] = []
                else:
                    scores_lvl[lvl].append(1)
                lvl -= 1


        return sum(scores_lvl[1])


if __name__ == '__main__':
    s = '(()()(()))'
    s = '(((()))(()))'
    s = '()()()'
    print(Solution().scoreOfParentheses(s))
