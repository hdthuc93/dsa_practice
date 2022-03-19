# https://leetcode.com/problems/remove-duplicate-letters/


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {}
        for i in range(len(s)):
            last_idx[s[i]] = i

        ch_set = set()
        s_lst = []

        for i in range(len(s)):
            c = s[i]
            if c not in ch_set:
                while len(s_lst) and c < s_lst[-1] and last_idx[s_lst[-1]] > i:
                    ch_set.remove(s_lst.pop())
                s_lst.append(c)
                ch_set.add(c)

        return ''.join(s_lst)




if __name__ == '__main__':
    s = "bcbac"
    # s = 'cbacdcbc'
    s = "mitnlruhznjfyzmtmfnstsxwktxlboxutbic"
    s = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s))
