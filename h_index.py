# https://leetcode.com/problems/h-index/


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_score = 0
        citations.sort(reverse=True)
        for c in citations:
            if c > h_score:
                h_score += 1
            else:
                break
        return h_score

    def hIndex2(self, citations: List[int]) -> int:
        c_index = [0] * 1001
        for c in citations:
            c_index[c] += 1

        h_score = 0
        for n in range(1000, -1, -1):
            if c_index[n] > 0 and n > h_score:
                h_score += c_index[n]
                h_score = min(h_score, n)
        return h_score



if __name__ == '__main__':
    citations = [3,0,6,1,5]
    # citations = [3, 5, 0, 1, 3]
    # citations = [25, 8, 5, 4, 3]
    # citations = [1,3,1]
    print(Solution().hIndex(citations))
    print(Solution().hIndex2(citations))
