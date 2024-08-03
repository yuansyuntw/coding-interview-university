from collections import defaultdict

class Solution:

    def testAllPath(self, start: int, edges: [[int]], n: int):
        N = n + 1
        matrix = [[0 for _ in range(N)] for _ in range(N)]
        for s, d in edges:
            matrix[s][d] = 1
        
        visited = set()
        def dfs(i):
            print("visit: {}".format(i))
            for neighbor in range(1, N):
                if neighbor != i and matrix[i][neighbor] and neighbor not in visited:
                    dfs(neighbor)
        visited.add(start)
        dfs(start)

n = 5
edges = [[1, 2], [1, 3], [3, 4], [2, 5]]
start = 1
solution = Solution()
solution.testAllPath(start, edges, n)