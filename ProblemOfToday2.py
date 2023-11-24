
grid = [[0 for _ in range(4)] for _ in range(4)]


def print_grid():
    for row in grid:
        print(row)


counter = 1
last_number = None
direction = None
start_row, end_row, start_col, end_col = 0, 4, 0, 4


while start_row < end_row and start_col < end_col:
    
    for i in range(start_col, end_col):
        grid[start_row][i] = counter
        last_number = counter
        counter += 1
    start_row += 1
    direction = "top"

    
    for i in range(start_row, end_row):
        grid[i][end_col - 1] = counter
        last_number = counter
        counter += 1
    end_col -= 1
    direction = "right"

    
    if start_row < end_row:
        for i in range(end_col - 1, start_col - 1, -1):
            grid[end_row - 1][i] = counter
            last_number = counter
            counter += 1
        end_row -= 1
        direction = "bottom"

    
    if start_col < end_col:
        for i in range(end_row - 1, start_row - 1, -1):
            grid[i][start_col] = counter
            last_number = counter
            counter += 1
        start_col += 1
        direction = "left"


print_grid()


print("Last Number:", last_number)
print("Direction:", direction)
