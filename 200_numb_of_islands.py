class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        counter = 0
        offset = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    counter += 1
                    queue = []
                    queue.append([i, j])
                    while queue:
                        cur_row, cur_col = queue.pop(0)
                        for num in offset:
                            if 0 <= cur_row + num[0] < rows and 0 <= cur_col + num[1] < cols and grid[cur_row + num[0]][
                                cur_col + num[1]] == '1':
                                grid[cur_row + num[0]][cur_col + num[1]] = '0'
                                queue.append([cur_row + num[0], cur_col + num[1]])
        return counter