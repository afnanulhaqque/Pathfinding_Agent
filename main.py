
import time
import csv
import os

from algorithms import bfs, dijkstra, astar
from visualization import visualize_path


# Grid configuration

grid = [
    [0, 0, 2, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)


# Calculate path length

def calculate_path_length(path):

    if path is None:
        return 0

    return len(path) - 1


# Calculate total path cost

def calculate_path_cost(grid, path):

    if path is None:
        return 0

    terrain_costs = {
        0: 1,
        2: 3,
        3: 5
    }

    total_cost = 0

    for row, col in path[1:]:

        total_cost += terrain_costs[grid[row][col]]

    return total_cost


# Run an algorithm and collect metrics

def run_algorithm(name, algorithm):

    start_time = time.perf_counter()

    path, expanded = algorithm(grid, start, goal)

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    result = {
        "name": name,
        "path": path,
        "length": calculate_path_length(path),
        "cost": calculate_path_cost(grid, path),
        "expanded": expanded,
        "time": execution_time
    }

    return result


# Select algorithms

algorithms = [
    ("BFS", bfs),
    ("Dijkstra", dijkstra),
    ("A Star", astar)
]


# Run experiments

results = []

for name, algorithm in algorithms:

    result = run_algorithm(name, algorithm)

    results.append(result)


# Display results

print("\nPATHFINDING COMPARISON")

print("=" * 60)

for result in results:

    print("\nAlgorithm:", result["name"])
    print("Path:", result["path"])
    print("Path Length:", result["length"])
    print("Path Cost:", result["cost"])
    print("Expanded Nodes:", result["expanded"])
    print("Execution Time:", round(result["time"], 4), "ms")

    visualize_path(
        grid,
        start,
        goal,
        result["path"],
        result["name"]
    )


# Save results as CSV

os.makedirs("results", exist_ok=True)

with open(
    "results/comparison.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Algorithm",
        "Path Length",
        "Path Cost",
        "Expanded Nodes",
        "Execution Time"
    ])

    for result in results:

        writer.writerow([
            result["name"],
            result["length"],
            result["cost"],
            result["expanded"],
            round(result["time"], 4)
        ])


print("\nResults saved in results/comparison.csv")
