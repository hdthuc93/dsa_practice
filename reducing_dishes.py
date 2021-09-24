# https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        sum_array = sum(satisfaction)
        all_dishes = 0
        sum_sub_array = [sum_array]
        for i in range(len(satisfaction)):
            val = satisfaction[i]
            all_dishes += (i+1) * val
            # if i == 0:
            #     print(sum_array, val)
            #     sum_sub_array.append(sum_array - val)
            # else:
            last_sum = sum_sub_array[-1]
            sum_sub_array.append(last_sum - val)

        max_val = all_dishes
        # print(satisfaction)
        # print('sum_sub_array', sum_sub_array)
        # print(max_val)
        for sum_sub in sum_sub_array:
            all_dishes -= sum_sub
            # print(all_dishes)
            max_val = max(max_val, all_dishes)

        return max(0, max_val)

    def maxSatisfaction2(self, satisfaction: list[int]) -> int:
        satisfaction.sort(reverse=True)
        sum_arr = max_val = 0
        for val in satisfaction:
            sum_arr += val
            max_val = max(max_val, max_val+sum_arr)

        return max(0, max_val)

if __name__ == '__main__':
    satisfaction = [-2,5,-1,0,3,-3]
    sol = Solution()
    print(sol.maxSatisfaction2(satisfaction=satisfaction))
