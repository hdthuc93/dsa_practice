# https://leetcode.com/problems/restore-ip-addresses/
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def run_recurrence(i, arr_ip):
            if len(arr_ip) == 4:
                if i == len(s):
                    res.append('.'.join(arr_ip))
                return

            ele = ''
            while i < len(s):
                ele += s[i]
                if len(ele) > 1 and ele[0] == '0':
                    i += 1
                    continue
                if int(ele) > 255:
                     break

                arr_ip.append(ele)
                run_recurrence(i+1, arr_ip)
                arr_ip.pop()
                i += 1

        run_recurrence(0, [])
        return res


if __name__ == '__main__':
    s = '101023'
    print(Solution().restoreIpAddresses(s))
