# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        array_p = []
        for c in p:
            if c != '*':
                array_p.append(c)
            else:
                array_p[-1] = array_p[-1] + c

        idotaerisk = -1
        iaerisk = -1
        ip = 0
        istring = 0

        while istring < len(s) and ip < len(array_p):
            schar = s[istring]
            pchar = array_p[ip]
            prev_iaerisk = iaerisk
            if len(pchar) == 2:
                if pchar == '.*':
                    idotaerisk = ip
                else:
                    iaerisk = ip

            p1 = pchar[0]
            if p1 == schar or p1 == '.':
                istring += 1
                ip += 1
            elif prev_iaerisk != -1:
                ip = prev_iaerisk + 1
                if array_p[prev_iaerisk][0] == schar:
                    istring += 1

                if prev_iaerisk == iaerisk:
                    iaerisk = -1
                else:
                    iaerisk = prev_iaerisk
            elif idotaerisk != -1:
                ip = idotaerisk + 1
            else:
                break

        print(istring, ip)
        if istring != len(s):
            return False

        if ip != len(array_p):
            while ip < len(array_p):
                if len(array_p[ip]) != 2:
                    return False

        return True

    def has_aerisk_after(self, p, ip):
        return ip + 1 < len(p) and p[ip+1] == '*'


if __name__ == '__main__':
    s = 'aaabbb'
    p = 'a*f*e*b*'
    sol = Solution()
    print(sol.isMatch(s, p))
