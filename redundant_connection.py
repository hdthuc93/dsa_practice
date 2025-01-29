# https://leetcode.com/problems/redundant-connection/?envType=daily-question&envId=2025-01-29


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adjacent_nodes = defaultdict(set)
        for n0, n1 in edges:
            adjacent_nodes[n0].add(n1)
            adjacent_nodes[n1].add(n0)

        n = len(edges)
        visited = [0] * (len(edges)+1)
        n_nodes = [1]
        visited[1] = 1
        
        def exe_dfs(node, prev_node, paths):
            if visited[node] == 2:
                circle = []
                paths.pop()
                while len(paths):
                    t_node = paths.pop()
                    circle.append(t_node)
                    if t_node == node:
                        return circle

            n_nodes = adjacent_nodes[node]

            for n_node in n_nodes:
                if n_node == prev_node:
                    continue

                visited[n_node] += 1
                paths.append(n_node)
                circle = exe_dfs(n_node, node, paths)
                if len(circle):
                    return circle
                paths.pop()

            return []

        circle = exe_dfs(1, 0, [1])
        circle = set(circle)

        for a, b in edges[::-1]:
            if a in circle and b in circle:
                return [a, b]

        return []
        
