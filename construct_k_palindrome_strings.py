# https://leetcode.com/problems/construct-k-palindrome-strings/
from collections import Counter


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        if n == k:
            return True

        char_counter = Counter(s)
        remain_palindromes_count = k
        for i in range(k):
            for ch in char_counter.keys():
                if char_counter[ch] >= 2:
                    char_counter[ch] -= 2
                    remain_palindromes_count -= 1
                    break

        even_palindromes_count = k - remain_palindromes_count
        for i in range(remain_palindromes_count):
            for ch in char_counter.keys():
                if char_counter[ch] > 0:
                    char_counter[ch] -= 1
                    remain_palindromes_count -= 1
                    break

        if remain_palindromes_count > 0 and even_palindromes_count > remain_palindromes_count:
            even_palindromes_count -= remain_palindromes_count
            remain_palindromes_count = 0

        odd_count_in_char = 0
        for num_count in char_counter.values():
            if num_count % 2 == 1:
                odd_count_in_char += 1

        return remain_palindromes_count == 0 and odd_count_in_char <= even_palindromes_count

    def canConstruct2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        char_counter = Counter(s)
        odd_count = 0
        for ch in char_counter.keys():
            if char_counter[ch] % 2 == 1:
                odd_count += 1

        return len(s) >= k and odd_count <= k
