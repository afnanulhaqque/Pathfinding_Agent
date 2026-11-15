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


# Create an empty graph
graph = {}

# Add every free cell as a node
for r in range(rows):
    for c in range(cols):

        if grid[r][c] == 0:
            graph[(r, c)] = []


# Connect neighboring nodes
for r in range(rows):
    for c in range(cols):

        if grid[r][c] == 1:
            continue

        current = (r, c)

        # Check the right neighbor
        if c + 1 < cols and grid[r][c + 1] == 0:

            neighbor = (r, c + 1)

            graph[current].append(neighbor)
            graph[neighbor].append(current)

        # Check the bottom neighbor
        if r + 1 < rows and grid[r + 1][c] == 0:

            neighbor = (r + 1, c)

            graph[current].append(neighbor)
            graph[neighbor].append(current)


# Display graph information
print("Starting Node:", start)
print("Goal Node:", goal)

print("\nTotal Nodes:", len(graph))

print("\nGraph Connections:")

for node, neighbors in graph.items():
    print(node, ":", neighbors)
