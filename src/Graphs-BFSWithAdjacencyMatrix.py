from collections  import defaultdict
from collections import deque

class Solution:

    def testAllPath(self, start: int, edges: [[int]], n: int):
        N = n + 1
        matrix = [[0 for _ in range(N)] for _ in range(N)]
        for s, d in edges:
            matrix[s][d] = 1

        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            print("visit: {}".format(node))
            for neighbor in range(1, N):
                if neighbor != node and matrix[node][neighbor] and neighbor not in visited:
                    queue.append(neighbor)

n = 5
edges = [[1, 2], [1, 3], [3, 4], [2, 5]]
start = 1
solution = Solution()
solution.testAllPath(start, edges, 5)