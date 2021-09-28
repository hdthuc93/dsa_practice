# https://leetcode.com/problems/number-of-provinces/


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def run_dfs(isConnected, i, is_owned):
            is_owned[i] = 1
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and is_owned[j] == 0:
                    run_dfs(isConnected, j, is_owned)

        is_owned = [0]*len(isConnected)
        nof_provinces = 0
        for i in range(len(isConnected)):
            if is_owned[i] == 0:
                run_dfs(isConnected, i, is_owned)
                nof_provinces += 1

        return nof_provinces


if __name__ == '__main__':
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))
