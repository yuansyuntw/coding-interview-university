from collections import defaultdict

class Solution:

    def minimumSpanningTree(self, start: int, edges: [[int]], n: int):
        N = n + 1
        costs = [] # (cost, s, d)
        for s, d, c in edges:
            costs.append((c, s, d))
        costs.sort()

        groups = [ 0 for _ in range(N) ]
        def get_root_group(target: int):
            if groups[target] != 0:
                groups[target] = get_root_group(groups[target]) # path compression O(logn)
                return groups[target]
            return target
        def is_same_group(source: int, target: int):
            return get_root_group(source) == get_root_group(target)
        def group(source: int, target: int):
            groups[get_root_group(source)] = get_root_group(target) # should set the new target on "the source's parent".

        result = 0
        count = 0
        for c, s, d in costs:
            if is_same_group(s, d):
                continue
            result += c
            count += 1
            if count == n:
                break
            group(d, s)
        return result

n = 5
edges = [[1, 2, 2], [1, 3, 1], [3, 4, 2], [2, 5, 3], [1, 5, 1]]
start = 1
solution = Solution()
cost = solution.minimumSpanningTree(start, edges, n)
print("result: {}".format(cost))