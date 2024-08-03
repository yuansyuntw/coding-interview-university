from collections  import defaultdict
from collections import deque

class Solution:

    def testAllPath(self, start: int, edges: [[int]]):
        adjacency = defaultdict(list)
        for s, d in edges:
            adjacency[s].append(d)
        
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.pop()
            if node in visited:
                continue
            visited.add(node)
            print("visit: {}".format(node))
            for neighbor in adjacency[node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)

edges = [[1, 2], [1, 3], [3, 4], [2, 5]]
start = 1
solution = Solution()
solution.testAllPath(start, edges)