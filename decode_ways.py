# https://leetcode.com/problems/decode-ways/


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev_c = s[0]
        count = 1
        nof_single = 1

        for c in s[1:]:
            num = int(c)
            if prev_c == '0' and num != 0:
                nof_single = 1
                prev_c = c
                continue

            if 1 <= num <= 6:
                if int(prev_c) <= 2:
                    temp = count
                    count += nof_single
                    nof_single = temp
                else:
                    nof_single = count
            elif 7 <= num <= 9:
                if prev_c == '1':
                    temp = count
                    count += nof_single
                    nof_single = temp
                else:
                    nof_single = count
            else:
                if int(prev_c) == 0 or int(prev_c) > 2:
                    return 0
                count = nof_single

            prev_c = c
        return count

    def numDecodings2(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev_c = s[0]
        dp = [1, 1]
        for c in s[1:]:
            combine = int(prev_c+c)
            if combine%10 == 0:
                if combine > 20:
                    return 0
                dp.append(dp[-2])
            elif 11 <= combine <= 19 or 21 <= combine <= 26:
                dp.append(dp[-1]+dp[-2])
            elif  1 <= combine <= 9 or combine > 26:
                dp.append(dp[-1])
            else:
                return 0
            prev_c = c

        return dp[-1]

if __name__ == '__main__':
    s = '61021'
    print(Solution().numDecodings2(s))
