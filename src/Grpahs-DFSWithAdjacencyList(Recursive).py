from collections import defaultdict

class Solution:

    def testAllPath(self, start: int, edges: [[int]]):
        adjacency = defaultdict(list)
        for s, d in edges:
            adjacency[s].append(d)
        
        visited = set()
        def dfs(i):
            print("visit: {}".format(i))
            for neighbor in adjacency[i]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        visited.add(start)
        dfs(start)

edges = [[1, 2], [1, 3], [3, 4], [2, 5]]
start = 1
solution = Solution()
solution.testAllPath(start, edges)