# https://leetcode.com/problems/two-city-scheduling/
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for a, b in costs:
            diff.append((a-b, [a, b]))

        diff.sort(key=lambda it: (it[0], it[1][0], it[1][1]))
        sum_costs = sum([ele[1][0] for ele in diff[:len(costs)//2]])
        sum_costs += sum([ele[1][1] for ele in diff[len(costs)//2:]])
        return sum_costs


if __name__ == '__main__':
    costs = [[10,20],[30,200],[400,50],[30,20]]
    # costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    print(Solution().twoCitySchedCost(costs))
