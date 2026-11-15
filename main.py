
from collections import deque


# 1. Create the grid

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)


# 2. Check valid positions

def is_valid_position(grid, position):

    row, col = position

    if not (0 <= row < len(grid)):
        return False

    if not (0 <= col < len(grid[0])):
        return False

    if grid[row][col] == 1:
        return False

    return True


# 3. Find valid neighbors

def get_valid_neighbors(grid, position):

    row, col = position

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for dr, dc in directions:

        new_position = (row + dr, col + dc)

        if is_valid_position(grid, new_position):
            neighbors.append(new_position)

    return neighbors


# 4. Breadth First Search algorithm

def bfs(grid, start, goal):

    # Create a queue

    queue = deque([start])

    # Track visited positions

    visited = {start}

    # Remember the parent of each position

    parent = {start: None}

    # Continue while the queue is not empty

    while queue:

        # Remove the first position

        current = queue.popleft()

        print("Exploring:", current)

        # Check whether we reached the goal

        if current == goal:

            path = []

            while current is not None:

                path.append(current)

                current = parent[current]

            path.reverse()

            return path

        # Explore neighboring positions

        for neighbor in get_valid_neighbors(grid, current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    # No path found

    return None


# 5. Run BFS

path = bfs(grid, start, goal)


# 6. Display the final result

print("\nFinal Path:")

if path:

    print(path)

    print("\nTotal Steps:", len(path) - 1)

else:

    print("No path found.")
