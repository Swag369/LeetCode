
class Solution:

    def grid_infect(self, grid: List[List[str]], i, j):

        if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]):
            return

        # print("grid", i, j, "is", grid[i][j])

        if grid[i][j] != "1":
            return

        grid[i][j] = 2
        # print("painting", i, j)


        self.grid_infect(grid, i-1, j)
        self.grid_infect(grid, i, j-1)
        self.grid_infect(grid, i+1, j)
        self.grid_infect(grid, i, j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    num_islands += 1
                    self.grid_infect(grid, i, j)
                    # print(grid)

        return num_islands