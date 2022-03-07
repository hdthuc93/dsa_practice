# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst = list(s)

        l, r = 0, len(s)-1
        while l < len(s) and s_lst[l] == ' ':
            s_lst[l] = ''
            l += 1
        while r >= 0 and s_lst[r] == ' ':
            s_lst[r] = ''
            r -= 1

        while l < r:
            s_lst[l], s_lst[r] = s_lst[r], s_lst[l]
            l += 1
            r -= 1

        l = 0
        while l < len(s_lst):
            if s_lst[l] == '' or s_lst[l] == ' ':
                l += 1
                continue

            r = l + 1
            while r < len(s_lst) and s_lst[r] != ' ':
                r += 1

            i, j = l, r-1
            while i < j:
                s_lst[i], s_lst[j] = s_lst[j], s_lst[i]
                i += 1
                j -= 1

            l = r + 1
            while l < len(s_lst) and s_lst[l] == ' ':
                s_lst[l] = ''
                l += 1

        return ''.join(s_lst)


if __name__ == '__main__':
    s = "the sky is blue"
    s = "   a good   example   "
    print(Solution().reverseWords(s))
