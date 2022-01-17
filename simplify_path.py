# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for d in path.split('/'):
            if d == '': continue

            if d == '..' and len(s):
                s.pop()
            elif d not in ['.', '..']:
                s.append(d)

        return '/' + '/'.join(s)


if __name__ == '__main__':
    path = '/home/'
    path = '/home//foo/'
    path = '/'
    path = '/Users/Joma/Documents/../Desktop/./../...'
    print(Solution().simplifyPath(path))
