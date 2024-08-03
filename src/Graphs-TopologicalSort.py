from collections import defaultdict

class Solution:

    def topologocalSorting(self, edges, n) -> [int]:
        visited = set()
        visiting = set()
        result = []

        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False # Cycling

            visiting.add(node)
            for neighbor in adjacency[node]:
                if not dfs(neighbor):
                    return False # Cycling
            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True

        for node in range(0, n):
            if not dfs(node):
                print("detect cycling")
                return []
        return list(reversed(result))


# Test case: https://yuminlee2.medium.com/topological-sort-cf9f8e43af6a
soluton = Solution()
edges = [[0, 2], [0 ,1], [0,4], [2, 4], [1, 4], [2, 3], [1,3], [3, 4]]
n = 5
result = soluton.topologocalSorting(edges, n)
print(result)
 