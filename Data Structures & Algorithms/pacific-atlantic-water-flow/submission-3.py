class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        atls,pacs = set(),set()
        def dfs(r,c,visited):
            visited.add((r,c))
            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r+dr,c+dc
                if nr >=0 and nc>=0 and nc< cols and nr < rows and heights[r][c] <= heights[nr][nc] and (nr,nc) not in visited:
                    dfs(nr,nc,visited)
        
        for r in range(rows):
            dfs(r,cols-1,atls)
            dfs(r,0,pacs)    
        
        for c in range(cols):
            dfs(rows-1,c,atls)
            dfs(0,c,pacs)
        
        return [list(p) for p in atls& pacs]