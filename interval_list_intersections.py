# https://leetcode.com/problems/interval-list-intersections/


class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][1]:
                if secondList[j][0] <= firstList[i][1]:
                    res.append([max(firstList[i][0], secondList[j][0]), firstList[i][1]])
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                if secondList[j][1] >= firstList[i][0]:
                    res.append([max(firstList[i][0], secondList[j][0]), secondList[j][1]])
                j += 1
            else:
                res.append([max(firstList[i][0], secondList[j][0]), secondList[j][1]])
                i += 1
                j += 1
        return res


if __name__ == '__main__':
    firt_list = [[3,5],[9,20],[21,24]]
    second_list = [[4,5],[7,10],[11,12],[14,15],[16,21]]
    print(Solution().intervalIntersection(firt_list, second_list))