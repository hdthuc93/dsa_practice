# https://leetcode.com/contest/weekly-contest-278/problems/find-substring-with-given-hash-value/

# TODO:
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s_values = [ord(c) - ord('a') + 1 for c in s]
        power_modulo = [0] * k
        power_modulo[0] = 1

        first = s_values[0] % modulo
        val = 0
        for i in range(1, k):
            power_modulo[i] = (power_modulo[i-1] * power) % modulo
            val += s_values[i] * power * power_modulo[i-1]

        if (val+first) % modulo == hashValue:
            return s[:k]

        # val += power*modulo
        for i in range(k, len(s)):
            # val -= first
            val = val // power
            val += (s_values[i] * power * power_modulo[k-2])
            if val % modulo == hashValue:
                return s[i-k+1:i+1]

            # first = s_values[i-k+1] % modulo
            val -= s_values[i-k+1]
            # val += power*modulo

        return ''


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
