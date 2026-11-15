
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import ListedColormap


def visualize_path(grid, start, goal, path, algorithm_name):

    colors = [
        "#E5E7EB",
        "#374151",
        "#F59E0B",
        "#DC6B28"
    ]

    cmap = ListedColormap(colors)

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.imshow(np.array(grid), cmap=cmap)

    if path is not None:

        path_rows = [position[0] for position in path]
        path_cols = [position[1] for position in path]

        ax.plot(
            path_cols,
            path_rows,
            color="green",
            linewidth=3,
            marker="o",
            markersize=8,
            label="Final Path"
        )

    ax.scatter(
        start[1],
        start[0],
        color="blue",
        s=250,
        label="Start"
    )

    ax.scatter(
        goal[1],
        goal[0],
        color="red",
        s=250,
        label="Goal"
    )

    ax.set_title(algorithm_name + " Pathfinding")

    ax.set_xticks(np.arange(-0.5, len(grid[0]), 1))
    ax.set_yticks(np.arange(-0.5, len(grid), 1))

    ax.grid(color="black", linewidth=1)

    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    ax.legend()

    plt.tight_layout()
    plt.show()
