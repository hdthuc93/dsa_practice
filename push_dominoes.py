# https://leetcode.com/problems/push-dominoes/


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pushes = []
        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                pushes.append(i)

        new_s = ''
        idx = 0
        before = -1
        after = pushes[0] if len(pushes) else None
        for i in range(len(dominoes)):
            s = dominoes[i]
            if dominoes[i] == '.':
                if before != -1 and after != -1 and dominoes[before] == 'R' and dominoes[after] == 'L':
                    if abs(i-before) > abs(i-after):
                        s = 'L'
                    elif abs(i-before) < abs(i-after):
                        s = 'R'
                elif before != -1 and dominoes[before] == 'R':
                    s = 'R'
                elif after != -1 and dominoes[after] == 'L':
                    s = 'L'
            else:
                idx += 1
                before = after
                after = pushes[idx] if idx < len(pushes) else -1

            new_s += s

        return new_s


if __name__ == '__main__':
    dominoes = 'R.'
    print(Solution().pushDominoes(dominoes))
