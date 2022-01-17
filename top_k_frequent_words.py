# https://leetcode.com/problems/top-k-frequent-words/
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        freq_words = {}
        max_freq = 0
        res = []
        for w, c in counter.items():
            freq_words.setdefault(c, [])
            freq_words[c].append(w)
            max_freq = max(max_freq, c)

        while max_freq > 0 and k > 0:
            if not freq_words.get(max_freq):
                max_freq -= 1
                continue

            words = freq_words[max_freq]
            words.sort()
            for w in words:
                if k == 0: break
                res.append(w)
                k -= 1
            max_freq -= 1

        return res


if __name__ == '__main__':
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    print(Solution().topKFrequent(words, k))
