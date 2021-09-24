class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        repeating_words = [0]*26
        for c in letters:
            repeating_words[ord(c)-ord('a')] += 1

        max_score = 0
        self.score_list = score
        self.words = words
        for i in range(len(words)):
            max_score = max(max_score, self.find_max(i, repeating_words))
        return max_score

    def find_max(self, index, letters):
        score = 0
        temp_letters = letters[:]
        for c in self.words[index]:
            char_index = ord(c) - ord('a')
            if temp_letters[char_index] > 0:
                temp_letters[char_index] -= 1
                score += self.score_lst[char_index]
            else:
                return 0

        sub_score = 0
        for i in range(index+1, len(self.words)):
            sub_score = max(sub_score, self.find_max(i, temp_letters))

        return score+sub_score


if __name__ == '__main__':
    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]

    sol = Solution()
    print(Solution().maxScoreWords(words, letters, score))
