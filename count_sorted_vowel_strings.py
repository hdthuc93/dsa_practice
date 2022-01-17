# https://leetcode.com/problems/count-sorted-vowel-strings/


class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels_count = [1,1,1,1,1]
        i = 1

        while i < n:
            next_count = [1] * 5
            cur_sum = 0
            for j in range(1, 5):
                cur_sum += vowels_count[j-1]
                next_count[j] = cur_sum + vowels_count[j]
            vowels_count = next_count
            i += 1

        return sum(vowels_count)


if __name__ == '__main__':
    n = 1
    print(Solution().countVowelStrings(n))
