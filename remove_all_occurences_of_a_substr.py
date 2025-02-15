# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(s) <= len(part) and s != part:
            return s

        new_s = s
        start = 0
        end = len(part) - 1
        # import pdb; pdb.set_trace()
        while end < len(new_s):
            if new_s[start:end+1] == part:
                new_s = new_s[:start] + new_s[end+1:]
                start = max(0, start - len(part))
                end = start + len(part) - 1
                continue

            start += 1
            end += 1

        return new_s


s = "kpygkivtlqoockpygkivtlqoocssnextkqzjpycbylkaondsskpygkpygkivtlqoocssnextkqzjpkpygkivtlqoocssnextkqzjpycbylkaondsycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"
part = "kpygkivtlqoocssnextkqzjpycbylkaonds"

sol = Solution()
print(sol.removeOccurrences(s, part))
