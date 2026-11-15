
# Grid environment

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)


# Get grid dimensions

rows = len(grid)
cols = len(grid[0])


# Check whether a position is valid

def is_valid_position(grid, position):

    row, col = position

    # Check grid boundaries

    if not (0 <= row < len(grid)):
        return False

    if not (0 <= col < len(grid[0])):
        return False

    # Check obstacles

    if grid[row][col] == 1:
        return False

    return True


# Find all valid neighbors

def get_valid_neighbors(grid, position):

    row, col = position

    # Four possible directions

    import operator

    directions = [
        (operator.neg(1), 0),  # Up
        (1, 0),                # Down
        (0, operator.neg(1)),  # Left
        (0, 1)                 # Right
    ]

    neighbors = []

    # Check each direction

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        new_position = (new_row, new_col)

        if is_valid_position(grid, new_position):

            neighbors.append(new_position)

    return neighbors


# Display agent movement possibilities

print("Starting Position:", start)

print("Goal Position:", goal)

print("\nValid Neighbors of Starting Position:")

neighbors = get_valid_neighbors(grid, start)

for neighbor in neighbors:
    print(neighbor)


# Test another position

position = (2, 2)

print("\nCurrent Agent Position:", position)

print("Available Movements:")

for neighbor in get_valid_neighbors(grid, position):
    print(neighbor)
