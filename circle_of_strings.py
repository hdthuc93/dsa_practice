# https://practice.geeksforgeeks.org/problems/circle-of-strings4530/1


class Solution:
    def isCircle(self, N, A):
        if len(A)  <= 1:
            return 0

        # prefixes = {}
        graph = {}
        for w in A:
            if len(w) > 1:
                graph.setdefault(ord(w[0]) - ord('a'), [])
                graph[ord(w[0]) - ord('a')].append(ord(w[-1]) - ord('a'))

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
        # visited = [False] * len(A)
        # for i in c:
        #     visited[i] = True
        # return 1 if all(visited) else 0


if __name__ == '__main__':
    A = ['aa', 'aa', 'af']
    # 'eggs', 'karat', 'apple', 'snack', 'tuna'
    N = len(A)
    print(Solution().isCircle(N, A))
