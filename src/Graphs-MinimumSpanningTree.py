from collections import defaultdict
import heapq

class Solution:

    def minimumSpanningTree(self, start: int, edges: [[int]]):
        adjacency = defaultdict(list)
        for s, d, c in edges:
            adjacency[s].append((d, c))

        minHeap = [(0, start)] # (cost, node)
        visited = set()
        result = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            result += cost
            for neighbor, path_cost in adjacency[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(minHeap, (path_cost, neighbor))
        return result

edges = [[1, 2, 2], [1, 3, 1], [3, 4, 2], [2, 5, 3], [1, 5, 1]]
start = 1
solution = Solution()
cost = solution.minimumSpanningTree(start, edges)
print("result: {}".format(cost))