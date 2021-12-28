# https://practice.geeksforgeeks.org/problems/circle-of-strings4530/1


class Solution:
    def isCircle(self, N, A):
        if len(A)  <= 1:
            return 0

        edges = {}
        graph = {}
        for idx, w in enumerate(A):
            if len(w) > 1:
                graph.setdefault(ord(w[0]) - ord('a'), [])
                graph[ord(w[0]) - ord('a')].append(ord(w[-1]) - ord('a'))
                edges.setdefault(w[0]+w[-1], [])
                edges[w[0]+w[-1]].append(idx)

        s = [ord(A[0][0]) - ord('a')]
        c = []
        while len(s):
            v = s[-1]
            if not graph.get(v) or not len(graph[v]):
                c.append(s.pop())
            else:
                adjacents = graph[v]
                u = adjacents.pop()
                s.append(u)

        print(c)
        print(edges)
        visited = [False] * len(A)
        for i in range(1, len(c)):
            w0 = chr(ord('a') + c[i-1])
            w1 = chr(ord('a') + c[i])
            lst_idx = edges.get(w0+w1, [])
            if len(lst_idx):
                idx = edges[w0+w1].pop()
                visited[idx] = True
        print(visited)

        return 1 if c[0] == c[-1] and all(visited) else 0


if __name__ == '__main__':
    A = ["ab" , "bc", "cd", "da"]
    # 'eggs', 'karat', 'apple', 'snack', 'tuna'
    N = len(A)
    print(Solution().isCircle(N, A))
