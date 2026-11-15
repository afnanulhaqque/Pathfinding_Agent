
import heapq
from collections import deque


def get_neighbors(grid, position):

    row, col = position

    directions = [
        (1, 0),
        (0, 1),
        (0, -1),
        (-1, 0)
    ]

    neighbors = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if (
            0 <= new_row < len(grid)
            and 0 <= new_col < len(grid[0])
            and grid[new_row][new_col] != 1
        ):
            neighbors.append((new_row, new_col))

    return neighbors


def reconstruct_path(parent, goal):

    path = []
    current = goal

    while current is not None:

        path.append(current)
        current = parent[current]

    path.reverse()

    return path


def get_terrain_cost(grid, position):

    row, col = position

    terrain_costs = {
        0: 1,
        2: 3,
        3: 5
    }

    return terrain_costs[grid[row][col]]


def heuristic(position, goal):

    row_difference = abs(position[0] - goal[0])
    col_difference = abs(position[1] - goal[1])

    return row_difference + col_difference


def bfs(grid, start, goal):

    queue = deque([start])

    parent = {start: None}
    visited = {start}

    while queue:

        current = queue.popleft()

        if current == goal:
            return reconstruct_path(parent, goal), len(visited)

        for neighbor in get_neighbors(grid, current):

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None, len(visited)


def dijkstra(grid, start, goal):

    queue = [(0, start)]

    distance = {start: 0}
    parent = {start: None}

    visited = set()

    while queue:

        current_cost, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return reconstruct_path(parent, goal), len(visited)

        for neighbor in get_neighbors(grid, current):

            if neighbor in visited:
                continue

            new_cost = (
                current_cost
                + get_terrain_cost(grid, neighbor)
            )

            if new_cost < distance.get(neighbor, float("inf")):

                distance[neighbor] = new_cost
                parent[neighbor] = current

                heapq.heappush(
                    queue,
                    (new_cost, neighbor)
                )

    return None, len(visited)


def astar(grid, start, goal):

    queue = [(heuristic(start, goal), 0, start)]

    g_cost = {start: 0}
    parent = {start: None}

    visited = set()

    while queue:

        f_cost, current_cost, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return reconstruct_path(parent, goal), len(visited)

        for neighbor in get_neighbors(grid, current):

            if neighbor in visited:
                continue

            new_g = (
                current_cost
                + get_terrain_cost(grid, neighbor)
            )

            if new_g < g_cost.get(neighbor, float("inf")):

                g_cost[neighbor] = new_g
                parent[neighbor] = current

                new_f = new_g + heuristic(neighbor, goal)

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor)
                )

    return None, len(visited)
