# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == '__main__':
    height = [1,20,7,2]
    print(Solution().maxArea(height))