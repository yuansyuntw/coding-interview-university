from collections import defaultdict

class Solution:

    def isBipartite(self, n: int, edges: [int]):
        INIT_LABEL = 0
        groups = [ INIT_LABEL for _ in range(n)]

        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        def dfs(node, label):
            if groups[node] != INIT_LABEL:
                return False

            groups[node] = label
            for neighbor in adjacency[node]:
                if groups[neighbor] == INIT_LABEL:
                    if not dfs(neighbor, label * -1):
                        return False
                else:
                    if groups[neighbor] != label * -1:
                        return False
            return True

        for node in range(0, n):
            if groups[node] == INIT_LABEL:
                if not dfs(node, 1):
                    return False
        return True

# Test Case: https://www.geeksforgeeks.org/bipartite-graph/
solution = Solution()
n = 5
edges = [[0, 1], [0, 3], [1, 2], [1, 3]]
result = solution.isBipartite(n, edges)
print("result: {}".format(result))