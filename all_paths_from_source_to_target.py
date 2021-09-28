# https://leetcode.com/problems/all-paths-from-source-to-target/


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        def dfs(graph, i, current_path, visited, res):
            if i == len(graph)-1:
                res.append(current_path[:])
                res[-1].append(i)
                return

            visited[i] = True
            current_path.append(i)
            for j in graph[i]:
                if not visited[j]:
                    dfs(graph, j, current_path, visited, res)

            visited[i] = False
            current_path.pop()

        visited = [False]*len(graph)
        res = []
        dfs(graph, 0, [], visited, res)
        return res



if __name__ == '__main__':
    graph = [[1,3],[2],[3],[]]
    print(Solution().allPathsSourceTarget(graph))
