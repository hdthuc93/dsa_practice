# https://leetcode.com/problems/find-substring-with-given-hash-value/


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s_values = [ord(c) - ord('a') + 1 for c in s]
        i = len(s) - 1
        res_index = -1
        val = 0

        while i > -1:
            val = ((val * power) + s_values[i]) % modulo

            if len(s) - i >= k:
                if val % modulo == hashValue:
                    res_index = i
                val -= s_values[i+k-1] * pow(power, k-1, modulo)
            i -= 1

        return s[res_index:res_index+k]


if __name__ == '__main__':
    s = "leetcode"
    power = 7
    modulo = 20
    k = 2
    hashValue = 0


    s = "fbxzaad"
    power = 31
    modulo = 100
    k = 3
    hashValue = 32

    s = "cbmzzngpnfyzoexfnzxhhyvzxibaijgfvaleowaqjllkgoercyiptkugzgcxobn"
    power = 83
    modulo = 56
    k = 27
    hashValue = 23

    print(Solution().subStrHash(s, power, modulo, k, hashValue))
