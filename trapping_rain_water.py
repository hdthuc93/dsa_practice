# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 1:
            return 0

        water = 0
        ground = 0
        higher_lst = [[0, height[0]]]
        for i in range(1, len(height)):
            if len(higher_lst) and higher_lst[-1][1] < height[i]:
                ground = higher_lst[-1][1]
                higher_lst.pop()
                while len(higher_lst):
                    idx, h = higher_lst[-1]
                    min_h = min(h, height[i])
                    water += (min_h-ground)*(i-idx-1)
                    if h <= height[i]:
                        ground = min_h
                        higher_lst.pop()
                    else:
                        break
            higher_lst.append([i, height[i]])
        return water


if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    print(Solution().trap(height))
