# https://leetcode.com/problems/string-compression/
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        last_char = chars[0]
        last_idx = 0
        repeat = 1
        i = 1
        while i < len(chars):
            c = chars[i]
            if c != last_char:
                last_char = c
                if repeat > 1:
                    repeat_str = list(str(repeat))
                    j = last_idx + 1
                    for n in repeat_str:
                        chars[j] = n
                        j += 1
                    n = i - j
                    while n > 0:
                        chars.pop(j)
                        n -= 1
                    last_idx = last_idx + len(repeat_str) + 1
                    i = last_idx
                    repeat = 1
                else:
                    last_idx = i
            else:
                repeat += 1
            i += 1

        if repeat > 1:
            repeat_str = list(str(repeat))
            j = last_idx + 1
            for n in repeat_str:
                chars[j] = n
                j += 1
            n = i - j
            while n > 0:
                chars.pop(j)
                n -= 1
        print(chars)
        return len(chars)


if __name__ == '__main__':
    chars = ["a","a","b","b",'x',"c","c","c", 'd']
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    # chars = ['z', 'z']
    print(Solution().compress(chars))
