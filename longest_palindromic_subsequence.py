# https://leetcode.com/problems/longest-palindromic-subsequence/


from typing import Match


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

    def longestPalindromeSubseq2(self, s: str) -> int:
        caches = {}

        def run_lcs(s, i, j):
            if i > j:
                return 0
            if i == j:
                return 1

            if caches.get((i, j)):
                return caches[(i, j)]

            res = 0
            if s[i] == s[j]:
                res = run_lcs(s, i+1, j-1) + 2
            else:
                res = max(run_lcs(s, i+1, j), run_lcs(s, i, j-1))
            caches[(i, j)] = res

            return res

        res = run_lcs(s, 0, len(s) - 1)
        return res


if __name__ == '__main__':
    s = "cbbd"
    print(Solution().longestPalindromeSubseq(s))
