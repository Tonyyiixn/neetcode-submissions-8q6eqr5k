class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        atls,pacs = set(),set()

        def dfs(r,c,visited):
            visited.add((r,c))
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc = r+dr,c+dc
                if (0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]):
                        dfs(nr,nc,visited)
        
        for c in range(cols):
            dfs(0,c,pacs)
            dfs(rows-1,c,atls)
        
        for r in range(rows):
            dfs(r,0,pacs)
            dfs(r,cols-1,atls)
        
        return [list(p) for p in pacs&atls]