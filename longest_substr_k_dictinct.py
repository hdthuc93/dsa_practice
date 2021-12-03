# https://techiedelight.com/practice/?problem=LongestDistinctSubstring
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/


class Solution:
    def findLongestSubstring(self, s: str, k: int) -> str:
        # Write your code here...
        l = r = 0
        max_sub_str = ''
        d_chars = {}

        while r < len(s):
            c = s[r]
            if d_chars.get(c, None):
                d_chars[c] += 1
            else:
                if len(list(d_chars.keys())) == k:
                    substr = s[l:r]
                    if len(max_sub_str) < len(substr):
                        max_sub_str = substr
                    while l < r:
                        d_chars[s[l]] -= 1
                        if d_chars[s[l]] == 0:
                            d_chars.pop(s[l], None)
                            l += 1
                            break
                        l += 1
                d_chars[c] = 1
            r += 1
        substr = s[l:]
        if len(max_sub_str) < len(substr):
            max_sub_str = substr
        return max_sub_str


if __name__ == '__main__':
    s = 'aabbbaaaabbbbbbba'
    k = 1
    print(Solution().findLongestSubstring(s, k))
