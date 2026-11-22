class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = {0}
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        
        return len(visited) == n