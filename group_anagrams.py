# https://leetcode.com/problems/group-anagrams/


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def reconstruct_str(_str):
            d = {}
            for c in _str:
                d.setdefault(c, 0)
                d[c] += 1
            res = ''
            for c in sorted(list(d.keys())):
                res += c + str(d[c])
            return res

        d_res = {}
        for s in strs:
            new_s = reconstruct_str(s)
            d_res.setdefault(new_s, [])
            d_res[new_s].append(s)

        return [v for _, v in d_res.items()]


if __name__ == '__main__':
    strs = ["a"]
    print(Solution().groupAnagrams(strs))
