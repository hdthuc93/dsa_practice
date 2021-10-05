# https://leetcode.com/problems/word-break-ii/


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        def dfs(wordDict, dp, index, cur, res):
            if index == len(dp):
                if len(cur):
                    res.append(' '.join(cur))
                return

            w = ''
            for i in range(index, len(dp)):
                w += dp[i]
                if wordDict.get(w):
                    cur.append(w)
                    dfs(wordDict, dp, i+1, cur, res)
                    cur.pop()

        wordDict = {w:1 for w in wordDict}
        dp = ['']
        w = ''
        found = False
        for c in s:
            found = False
            if wordDict.get(w+c):
                found = True
                dp.append(w+c)
                w = ''
                continue
            else:
                last = ''
                for i in range(len(dp)-1, -1, -1):
                    last = dp[i] + last
                    if wordDict.get(last+w+c):
                        found = True
                        dp.append(w+c)
                        break
                if found:
                    w = ''
                    continue
            w += c

        res = []
        if found:
            w = ''
            for i in range(len(dp)):
                w += dp[i]
                if wordDict.get(w):
                    dfs(wordDict, dp, i+1, [w], res)

        return res


if __name__ == '__main__':
    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    print(Solution().wordBreak(s, wordDict))
