# https://leetcode.com/problems/split-array-largest-sum/
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        sum_lst = []
        visited = [False] * len(nums)
        for i, n in enumerate(nums[:m-1]):
            sum_lst.append((n, i))
            visited[i] = True

        sum_lst.append((sum(nums[m-1:]), m-1))
        visited[m-1] = True
        max_sum = sum(nums)
        while True:
            max_idx = 0
            for i in range(1, len(sum_lst)):
                if sum_lst[max_idx][0] < sum_lst[i][0]:
                    max_idx = i
                elif sum_lst[max_idx][0] == sum_lst[i][0] and sum_lst[i][1] + 1 < len(nums) and not visited[sum_lst[i][1] + 1]:
                    max_idx = i

            cur_sum, idx = sum_lst[max_idx]
            max_sum = min(max_sum, cur_sum)
            if max_idx == 0 or idx + 1 >= len(nums) or visited[idx+1]:
                break

            cur_sum -= nums[idx]
            visited[idx] = False
            visited[idx + 1] = True
            sum_lst[max_idx] = (cur_sum, idx + 1)
            sum_lst[max_idx-1] = (sum_lst[max_idx-1][0] + nums[idx], sum_lst[max_idx-1][1])

        return max_sum

if __name__ == '__main__':
    nums = [7,2,5,10,8]
    m = 3
    # nums = [1,2,3,4,5]
    # m = 2
    # nums = [1,4,4]
    # m = 3
    print(Solution().splitArray(nums, m))
