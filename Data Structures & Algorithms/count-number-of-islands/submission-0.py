class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        row = len(grid)
        column = len(grid[0])
        num_islands = 0

        def sink_island(r,c):
            if r < 0 or c < 0 or r >=row or c>=column or grid[r][c] == '0':
                return;
            
            grid[r][c] = '0'

            sink_island(r + 1,c)
            sink_island(r - 1,c)
            sink_island(r,c + 1)
            sink_island(r,c - 1)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    num_islands += 1
                    sink_island(i,j)
        

        return num_islands
            
