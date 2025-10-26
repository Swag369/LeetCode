class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # if I move down -> 1 + total_paths_once_down
        # if I move right -> 1 + total_paths_once_right

        # defined at 1 above and 1 to left of finish

        grid = [[0 for _ in range(n)] for _ in range(m)]

        grid[m-1][n-1] = 1 #placeholder to init the other two without changing my loop
        # grid[m-1-1][n-1] = 1 #only one way from 1 left
        # grid[m-1][n-1-1] = 1 #only one way from 1 up

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j != n-1:
                    grid[i][j] += grid[i][j+1]
                if i != m-1:
                    grid[i][j] += grid[i+1][j]
        
        print(grid)
        return grid[0][0]