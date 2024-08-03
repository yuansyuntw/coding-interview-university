from collections import defaultdict

class Solution:

    def countStronglyConnectedComponentes(self, edges: [int], n: int):
        outgoing = defaultdict(list)
        ingoing = defaultdict(list)
        for a, b in edges:
            outgoing[a].append(b)
            ingoing[b].append(a)
        
        # Pass 1: Get the stack
        stack = []
        visited = set()
        visiting = set()
        def passOne(node):
            if node in visited:
                return
            if node in visiting:
                print("Found cycling on the pass one")
                return # cycling
            
            visiting.add(node)
            for neighbor in outgoing[node]:
                passOne(neighbor)
            visiting.remove(node)
            visited.add(node)
            stack.append(node)
        for node in range(1, n + 1):
            passOne(node)

        print("pass one result: {}".format(stack))

        # Pass 2: Grouping.
        visited.clear()
        visiting.clear()
        newGroup = []
        def passTwo(node):
            if node in visited:
                return
            if node in visiting:
                print("Found cycling on the pass two")
                return # cycling
            visiting.add(node)
            for neighbor in ingoing[node]:
                passTwo(neighbor)
            visiting.remove(node)
            visited.add(node)
            newGroup.append(node)

        groups = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            newGroup = []
            passTwo(node)
            if len(newGroup) > 0:
                groups.append(newGroup)    
        print("groups: {}".format(groups))
        return len(groups)

# Test Case: https://www.youtube.com/watch?v=RpgcYiky7uw
solution = Solution()
n = 7
edges = [[1, 2], [2, 3], [3, 1], [3,5], [5, 6], [6, 4], [4, 5], [7, 6]]
result = solution.countStronglyConnectedComponentes(edges, n)
print("result: {}".format(result))