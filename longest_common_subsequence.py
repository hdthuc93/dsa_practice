# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def find_longest(t1, t2):
            d1 = {}
            for i in range(len(t1)):
                d1.setdefault(t1[i], [])
                d1[t1[i]].append(i)

            dp = []
            arr = []
            last_index = [-1]
            max_len = 0
            for c in t2:
                if d1.get(c):
                    found = False
                    for d1i in d1[c]:
                        if len(dp) and d1i > dp[-1]:
                            found = True
                            dp.append(d1i)
                            break
                        if d1i > last_index[-1]:
                            found = True
                            last_index.append(d1i)
                            break

                    if not found:
                        for d1i in d1[c]:
                            if len(dp) > 1 and d1i > dp[-2]:
                                found = True
                                dp[-1] = d1i
                                break
                            if  len(last_index) > 1 and d1i > last_index[-2]:
                                found = True
                                last_index[-1] = d1i
                                break
                        if not found:
                            if len(last_index)-1 > max_len:
                                dp.append(last_index[-1])
                                max_len = len(last_index)-1
                                last_index = [d1[c][0]]

            print(dp)
            print(d1)
            print(max_len)
            # for arr in dp:
            #     max_len = max(max_len, len(arr))
            return max_len

        len1 = find_longest(text1, text2)
        len2 = find_longest(text2, text1)
        return max(len1, len2)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if text1[j] == text2[i]:
                    if i-1 >= 0 and j-1 >= 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i-1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j-1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])

        print('', ', '.join([c for c in text1]))
        for idx, arr in enumerate(dp):
            print(arr, text2[idx])

        return dp[-1][-1]


if __name__ == '__main__':
    text2 = 'oxcpqrsvw'
    text1 = 'shmtulqrypy'
    # text1 = 'ahhhhhhhbiiiiiiic'
    # text2 = 'qqqqallllbhhhhcooooo'
    # text1 = 'abc'
    # text2 = 'abc'
    text1 = 'papmretkborsrurgtina'
    text2 = 'nsnupotstmnkfcfavaxgl'
    # text1 = 'yyyyayybyycyyyayybyycyydyy'
    # text2 = 'iiiassbiiciid'
    # text1 = "yzebsbuxmtcfmtodclszgh"
    # text2 = "ejevmhcvshclydqrulwbyha"
    # emcdlh
    # text1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # text2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    print(Solution().longestCommonSubsequence2(text1, text2))
