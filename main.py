# Create a 5 by 5 grid

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Define starting and ending positions
start = (0, 0)
goal = (4, 4)

# Display the grid
for row_index, row in enumerate(grid):

    for col_index, cell in enumerate(row):

        position = (row_index, col_index)

        if position == start:
            print("S", end=" ")

        elif position == goal:
            print("G", end=" ")

        elif cell == 1:
            print("#", end=" ")

        else:
            print(".", end=" ")

    print()