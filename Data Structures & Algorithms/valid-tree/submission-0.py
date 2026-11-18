class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        adj = {i: [] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(num):
            visited.add(num)
            for nei in adj[num]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)

        return len(visited) == n
