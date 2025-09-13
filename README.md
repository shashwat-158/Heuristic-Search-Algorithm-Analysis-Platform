# Pathfinding Algorithm Visualizer

An interactive Python application for visualizing and comparing pathfinding algorithms like A*, Dijkstra's, and Breadth-First Search (BFS) using the Pygame library.

![Screenshot of the pathfinding visualizer in action]
*(A screenshot or GIF will be added here once the project is functional)*

---

## Key Features

- **Interactive Grid:** Create your own mazes by drawing barrier walls with the mouse.
- **Algorithm Selection:** Choose between A*, Dijkstra's, and BFS to find the shortest path.
- **Real-Time Visualization:** Watch the algorithms explore the grid step-by-step.
- **Performance Benchmarking:** Compare the efficiency of the algorithms by tracking the number of "nodes explored".

## Tech Stack

- **Python 3**
- **Pygame**

## Setup and Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/pathfinding-visualizer.git](https://github.com/your-username/pathfinding-visualizer.git)
    ```
2.  Navigate into the project directory:
    ```bash
    cd pathfinding-visualizer
    ```
3.  Install the required dependencies:
    ```bash
    pip install pygame
    ```

## How to Use

1.  Run the main application:
    ```bash
    python main.py
    ```
2.  **Left-click** on the grid to place the **start node** (orange), **end node** (purple), and **barrier walls** (black).
3.  **Right-click** to erase any node.
4.  Press the **spacebar** to start the selected pathfinding algorithm.
5.  Press the **'c' key** to clear the board and start over.