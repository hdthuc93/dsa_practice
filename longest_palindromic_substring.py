# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindrome(j, i):
            while j-1 >= 0 and i+1 < len(s):
                if s[j-1] != s[i+1]:
                    break
                j -= 1
                i += 1
            return j, i

        i = 0
        longest = 1
        longest_substr = s[0]
        while i < len(s):
            i1 = i2 = 0
            if i-1 >= 0 and s[i] == s[i-1]:
                j1, i1 = find_palindrome(i-1, i)
                if longest < i1-j1+1:
                    longest = i1-j1+1
                    longest_substr = s[j1:i1+1]
            if i-2 >= 0 and s[i] == s[i-2]:
                j2, i2 = find_palindrome(i-2, i)
                if longest < i2-j2+1:
                    longest = i2-j2+1
                    longest_substr = s[j2:i2+1]

            if i1 > i and i1 > i2:
                i = i1
            elif i2 > i and i2 > i1:
                i = i2
            else:
                i += 1

        return longest_substr

    def longestPalindrome2(self, s: str) -> str:
        def find_palindrome(lst_indexes, cur_index, longest):
            for j in lst_indexes:
                if j <= cur_index-longest:
                    if s[j:cur_index+1] == s[j:cur_index+1][::-1]:
                        return j
                else:
                    break
            return -1

        d = {}
        longest = 1
        longest_str = s[0]
        for i in range(len(s)):
            if not d.get(s[i]):
                d[s[i]] = [i]
            else:
                prev_index = find_palindrome(d[s[i]], i, longest)
                if prev_index != -1:
                    longest = i - prev_index + 1
                    longest_str = s[prev_index:i+1]
                d[s[i]].append(i)

        return longest_str


if __name__ == '__main__':
    s = 'ababababa'
    print(Solution().longestPalindrome2(s))
