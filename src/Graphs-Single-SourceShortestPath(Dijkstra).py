from collections import defaultdict
import heapq

class Solution:

    def findShortestPath(self, start: int, end: int, edges: [[int]]):
        adjacency = defaultdict(list)
        for s, d, c in edges:
            adjacency[s].append((d, c))

        minHeap = [(0, start)] # (cost, node)
        visited = set()
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return cost # It should be added by previous path.
            for neighbor, new_cost in adjacency[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(minHeap, (cost + new_cost, neighbor))
        return -1
                
edges = [[1, 2, 2], [1, 3, 1], [3, 4, 2], [2, 5, 3]]
start = 1
end = 5
solution = Solution()
cost = solution.findShortestPath(start, end, edges)
print("result: {}".format(cost))