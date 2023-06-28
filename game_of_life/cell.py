def cellStatusUpdate(cell, alive_count):
    if cell == '█':
        if alive_count < 2:
            return '░'
        if alive_count > 3:
            return '░'
        if alive_count == 2 or alive_count == 3:
            return '█'
    else:
        if alive_count == 3:
            return '█'
        else:
            return '░'

alive_count = 0

def count(cell):
    global alive_count
    if cell == '█':
        alive_count += 1

def cellUpdate(grid, new_grid, i, j, n, m):
    global alive_count
    if i == 0:
        if j == 0:
            count(grid[i][j + 1])
            count(grid[i + 1][j])
            count(grid[i + 1][j + 1])
        elif j == m - 1:
            count(grid[i][j - 1])
            count(grid[i + 1][j - 1])
            count(grid[i + 1][j])
        else:
            count(grid[i][j - 1])
            count(grid[i][j + 1])
            count(grid[i + 1][j - 1])
            count(grid[i + 1][j])
            count(grid[i + 1][j + 1])
    elif i == n - 1:
        if j == 0:
            count(grid[i - 1][j])
            count(grid[i - 1][j + 1])
            count(grid[i][j + 1])
        elif j == m - 1:
            count(grid[i - 1][j - 1])
            count(grid[i - 1][j])
            count(grid[i][j - 1])
        else:
            count(grid[i - 1][j - 1])
            count(grid[i - 1][j])
            count(grid[i - 1][j + 1])
            count(grid[i][j - 1])
            count(grid[i][j + 1])
    else:
        if j == 0:
            count(grid[i - 1][j])
            count(grid[i - 1][j + 1])
            count(grid[i][j + 1])
            count(grid[i + 1][j])
            count(grid[i + 1][j + 1])
        if j == m - 1:
            count(grid[i - 1][j - 1])
            count(grid[i - 1][j])
            count(grid[i][j - 1])
            count(grid[i + 1][j - 1])
            count(grid[i + 1][j])
        else:
            count(grid[i - 1][j - 1])
            count(grid[i - 1][j])
            count(grid[i - 1][j + 1])
            count(grid[i][j - 1])
            count(grid[i][j + 1])
            count(grid[i + 1][j - 1])
            count(grid[i + 1][j])
            count(grid[i + 1][j + 1])
    new_grid[i][j] = cellStatusUpdate(grid[i][j], alive_count)
    #print(alive_count)
    alive_count = 0