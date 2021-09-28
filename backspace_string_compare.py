# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def excute_remove(s):
            s = list(s)
            l=r=0
            while r < len(s):
                if s[r] not in ['#', '']:
                    l = r
                else:
                    s[r] = ''
                    s[l] = ''
                    while l > 0:
                        if s[l] == '': l -= 1
                        else: break
                r += 1
            return ''.join(s)

        s = excute_remove(s)
        t = excute_remove(t)
        print(s)
        print(t)

        return s == t


if __name__ == '__main__':
    s = 'aaaa#a#b#c#a#s#r#t#y#u###'
    t = 'ad#c'
    print(Solution().backspaceCompare(s, t))