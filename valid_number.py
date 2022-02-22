# https://leetcode.com/problems/valid-number/


class Solution:
    def isNumber(self, s: str) -> bool:
        from string import digits
        if 'e' in s and 'E' in s:
            return False

        splitted = [s]
        if 'e' in s:
            splitted = s.split('e')
            if len(splitted) > 2: return False
        if 'E' in s:
            splitted = s.split('E')
            if len(splitted) > 2: return False

        s0 = splitted[0]
        if len(s0) == 0: return False
        has_dot = has_digits = False
        if s0[0] in ['+', '-']:
            pass
        elif s0[0] in digits:
            has_digits = True
        elif s0[0] == '.':
            has_dot = True
        else:
            return False

        for c in s0[1:]:
            if c in digits:
                has_digits = True
            elif c == '.':
                if has_dot:
                    return False
                has_dot = True
            else:
                return False

        if not has_digits: return False

        if len(splitted) == 2:
            s1 = splitted[1]
            has_digits = False
            if s1 == '':
                return False
            if s1[0] in ['+', '-']:
                pass
            elif s1[0] in digits:
                has_digits = True
            else:
                return False

            for c in s1[1:]:
                if c not in digits:
                    return False
                has_digits = True
            if not has_digits: return False

        return True


if __name__ == '__main__':
    s = '1.e'
    lst_s = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    # lst_s = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    # lst_s = ['2e0', '4e+']
    for s in lst_s:
        print(Solution().isNumber(s))
