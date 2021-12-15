# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        s_lst = ['']
        times = []
        rank = 0
        temp = ''
        for c in s:
            if c.isnumeric():
                if temp and temp.isalpha():
                    s_lst[rank] += temp
                    temp = ''
                temp += c
            elif c.isalpha():
                temp += c
            elif c == '[':
                times.append(int(temp))
                temp = ''
                s_lst.append('')
                rank += 1
            else:
                sub_str = s_lst[rank] + temp
                nof_time = times.pop()
                sub_str *= nof_time
                s_lst[rank-1] += sub_str
                s_lst[rank] = ''
                rank -= 1
                temp = ''
        if temp:
            s_lst[0] += temp
        return s_lst[0]


if __name__ == '__main__':
    s = "ab3[2[yz]gh3[k]x]cd"
    print(Solution().decodeString(s))
